import utils.visitor as visitor
from nodes_types import hulk_types as hulk
from utils.semantic import TypeTree
from utils.semantic import VariableInfo


class TypeBuilder:
    def __init__(self, context, errors=[]):
        self.context = context
        self.current_type = None
        self.recurrent_type = None
        self.errors = errors
        self.var = {}
        self.types = TypeTree(None)

    @visitor.on('node')
    def visit(self, node, types=None):
        pass

    @visitor.when(hulk.ProgramNode)
    def visit(self, node, types):
        for statement in node.statements:
            self.visit(statement, self.types.create_child())
        self.visit(node.main, self.types.create_child())
        return self.errors

    @visitor.when(hulk.FuncDeclarationNode)
    def visit(self, node, types):

        for param in node.params: # Actualiza var con los parametros de la funcion
            self.var[param[0]] = param[1]
            self.types.dict[param[0]] = param[1]
        self.visit(node.body, self.types.create_child())

        self.context.get_func(node.name).params = [] # Inicializa la funcion del contexto con los params empty
        for param in self.var.keys():
            self.context.get_func(node.name).params.append(     # Actualiza la funcion del contexto con la info de var
                (param, self.var[param]))
        self.var = {}   # Limpia var
        if node.type:
            if node.type != node.body.type:
                self.errors.append(
                    f"La función '{node.name}' debe retornar un '{node.type}'")
        else:
            node.type = node.body.type

        self.context.get_func(node.name).type = node.type
        if not node.type:
            self.errors.append(
                f"No se pudo inferir el tipo de retorno de la función '{node.name}'")
        for param in self.context.get_func(node.name).params:
            if not param[1]:
                self.errors.append(f"No se pudo inferir el tipo del parámetro '{param[0]}' de la función '{node.name}'")
        node.params = self.context.get_func(node.name).params
        # print(node.args)
        return self.errors

    @visitor.when(hulk.TypeDeclarationNode)
    def visit(self, node, types):
        for param in node.params:
            self.var[param[0]] = param[1]
            self.types.dict[param[0]] = param[1]
        self.current_type = self.context.get_type(node.name)
        
        # if(node.base_type and node.base_type != hulk.OBJECT_TYPE):
        #     parent = self.context.get_type(node.base_type)
        #     for attr in parent.attributes:
        #         self.visit(attr, self.types.create_child())
        #         self.current_type.define_attribute(attr.name, attr.type)
        #     for meth in parent.methods:
        #         self.visit(meth, self.types.create_child())
        #         param_names = []
        #         param_types = []
        #         for param in meth.params:
        #             param_names.append(param[0])
        #             param_types.append(param[1])
        #         self.current_type.define_method(
        #             meth.name, param_names, param_types, meth.type)
        for attr in node.body.attributes:
            self.visit(attr, self.types.create_child())
            self.current_type.define_attribute(attr.id.name, attr.type)
        for meth in node.body.methods:
            self.visit(meth, self.types.create_child())
            param_names = []
            param_types = []
            for param in meth.params:
                param_names.append(param[0])
                param_types.append(param[1])
            self.current_type.define_method(
                meth.name, param_names, param_types, meth.type)
        


        for param in self.var.keys():
            self.current_type.params.append((param, self.var[param]))
        self.var = {}
        self.current_type = None
        return self.errors

    @visitor.when(hulk.TypeBodyDeclarationNode)
    def visit(self, node, types):
        
        return self.errors

    @visitor.when(hulk.AttributeNode)
    def visit(self, node, types):
        self.visit(node.value, self.types.create_child())
        if node.type:
            if node.type != node.value.type:
                self.errors.append(f"No se puede asignar un '{node.value.type}' a un '{node.type}'")
        else:
            node.type = node.value.type
        if not node.type:
            self.errors.append(
                f"No se pudo inferir el tipo del atributo '{node.id.name}'")
        return self.errors

    @visitor.when(hulk.MethodNode)
    def visit(self, node, types):
        self.var = {}
        for param in node.params:
            self.var[param[0]] = param[1]
        self.visit(node.body, self.types.create_child())

        node.params = [(param[0], self.var[param[0]]) for param in node.params]

        for param in node.params:
            if not self.var[param[0]]:
                self.errors.append(f"No se pudo inferir el tipo del parámetro '{node.name}' del método '{node.name}'")
        
        if node.type:
            if node.type != node.body.type:
                self.errors.append(
                    f"El método '{node.name}' debe retornar un '{node.type}'")
        else:
            node.type = node.body.type
        if not node.type:
            self.errors.append(
                f"No se pudo inferir el tipo de retorno del método '{node.name}'")
        return self.errors

    @visitor.when(hulk.AssignNode)
    def visit(self, node, types):
        self.visit(node.expr, self.types.create_child())
        try:
            if node.expr.child:
                node.type = self.recurrent_type.name
            else:
                node.type = node.expr.type
        except:
            node.type = node.expr.type
        if node.id.type:
            if node.id.type != node.type:
                self.errors.append(f"No se puede asignar un '{node.type}' a un '{node.id.type}'")
        else:
            node.id.type = node.type
            self.types.dict[node.id.name] = node.type
        return self.errors

    @visitor.when(hulk.BlockNode)
    def visit(self, node, types):
        for expr in node.body:
            self.visit(expr, self.types.create_child())
        try:
            if node.body[-1].child:
                node.type = self.recurrent_type.name
            else:
                node.type = node.body[-1].type
        except:
            node.type = node.body[-1].type
        # node.type = node.body[-1].type
        return self.errors

    @visitor.when(hulk.LetNode)
    def visit(self, node, types):
        for arg in node.args:
            self.visit(arg, self.types.create_child())
            self.types.dict[arg.id.name] = arg.id.type
        self.visit(node.body, self.types.create_child())
        try:
            if node.body.child:
                node.type = self.recurrent_type.name
            else:
                node.type = node.body.type
        except:
            node.type = node.body.type

        return self.errors

    @visitor.when(hulk.WhileNode)
    def visit(self, node, types):
        self.visit(node.condition, self.types.create_child())
        self.visit(node.body, self.types.create_child())
        try:
            if node.body.child:
                node.type = self.recurrent_type.name
            else:
                node.type = node.body.type
        except:
            node.type = node.body.type
        return self.errors

    @visitor.when(hulk.IfNode)
    def visit(self, node, types):
        self.visit(node.condition, self.types.create_child())
        self.visit(node.body, self.types.create_child())
        node.type = node.body.type
        self.visit(node.else_body, self.types.create_child())
        if node.else_body.type != node.type:
            self.errors.append(
                f"Todos los bloques del IF deben devolver el mismo tipo")
        for cond in node.elif_conditions:
            self.visit(cond, self.types.create_child())
        for body in node.elif_body:
            self.visit(body, self.types.create_child())
            if body.type != node.type:
                self.errors.append(
                    f"Todos los bloques del IF deben devolver el mismo tipo")
        return self.errors

    @visitor.when(hulk.DestructNode)
    def visit(self, node, types):
        self.visit(node.id, self.types.create_child())
        self.visit(node.expr, self.types.create_child())
        if node.id.type != node.expr.type:
            self.errors.append(f"No se puede asignar un '{node.expr.type}' a un '{node.id.type}'")
        else:
            node.type = node.id.type
        try:
            if node.expr.child:
                node.type = self.recurrent_type.name
            else:
                node.type = node.expr.type
        except:
            node.type = node.expr.type
        return self.errors

    @visitor.when(hulk.CallNode)
    def visit(self, node, types):
        if self.recurrent_type:
            try:
                fun = self.recurrent_type.get_method(node.name)
            except:
                self.errors.append(f"El método '{node.name}' no está definido en '{self.recurrent_type.name}'")
                return self.errors
            for i, arg in enumerate(node.args):
                self.visit(arg, self.types.create_child())
                if arg.type != fun.param_types[i]:
                    if not arg.type:
                        arg.type = fun.param_types[i]
                        self.vist(arg)
                    else:
                        self.errors.append(f"La función '{fun.name}' esperaba como argumento número {i + 1} un '{fun.param_types[i]}' y recibió un '{arg.type}'")
            node.type = fun.return_type
        else:
            try:
                fun = self.context.get_func(node.name)
            except:
                self.errors.append(
                    f"La función '{node.name}' no está definida")
                return self.errors
            for i, arg in enumerate(node.args):
                self.visit(arg, self.types.create_child())
                params = list(self.var.values()) if len(fun.params) == 0 else [i[1] for i in fun.params]
                if arg.type != params[i]:
                    if not arg.type:
                        arg.type = fun.params[i][1]
                        self.visit(arg, self.types.create_child())
                    else:
                        self.errors.append(f"La función '{fun.name}' esperaba como argumento número {i + 1} un '{fun.params[i][1]}' y recibió un '{arg.type}'")
            if fun.type:
                if node.type and fun.type != node.type:
                     self.errors.append(f"La función '{fun.name}' es de tipo '{fun.type}' pero un llamado a esta es de tipo '{node.type}' ")
                node.type = fun.type
            elif node.type:
                fun.type = node.type
        if node.child:
            self.recurrent_type = self.context.get_type(node.type)
            self.visit(node.child, self.types.create_child())
            self.recurrent_type = self.context.get_type(node.child.type)
        return self.errors

    @visitor.when(hulk.PlusNode)
    def visit(self, node, types):
        self.visit(node.left, self.types.create_child())
        self.visit(node.right, self.types.create_child())
        try:
            if node.left.child:
                if self.recurrent_type.name != hulk.NUMBER_TYPE:
                    self.errors.append(
                        f"La operación + solo esta definida entre números")
        except:
            pass
        try:
            if node.right.child:
                if self.recurrent_type.name != hulk.NUMBER_TYPE:
                    self.errors.append(
                        f"La operación + solo esta definida entre números")
        except:
            pass
        if not node.left.type:
            node.left.type = hulk.NUMBER_TYPE
            self.visit(node.left, self.types.create_child())
        if not node.right.type:
            node.right.type = hulk.NUMBER_TYPE
            self.visit(node.right, self.types.create_child())
        if node.left.type != hulk.NUMBER_TYPE or node.right.type != hulk.NUMBER_TYPE:
            self.errors.append(
                f"La operación + solo esta definida entre números")
        node.type = hulk.NUMBER_TYPE
        node.left.type = hulk.NUMBER_TYPE
        node.right.type = hulk.NUMBER_TYPE
        return self.errors

    @visitor.when(hulk.MinusNode)
    def visit(self, node, types):
        self.visit(node.left, self.types.create_child())
        self.visit(node.right, self.types.create_child())
        try:
            if node.left.child:
                if self.recurrent_type.name != hulk.NUMBER_TYPE:
                    self.errors.append(
                        f"La operación - solo esta definida entre números")
        except:
            pass
        try:
            if node.right.child:
                if self.recurrent_type.name != hulk.NUMBER_TYPE:
                    self.errors.append(
                        f"La operación - solo esta definida entre números")
        except:
            pass
        if not node.left.type:
            node.left.type = hulk.NUMBER_TYPE
            self.visit(node.left, self.types.create_child())
        if not node.right.type:
            node.right.type = hulk.NUMBER_TYPE
            self.visit(node.right, self.types.create_child())
        if node.left.type != hulk.NUMBER_TYPE or node.right.type != hulk.NUMBER_TYPE:
            self.errors.append(
                f"La operación - solo esta definida entre números")
        node.type = hulk.NUMBER_TYPE
        node.left.type = hulk.NUMBER_TYPE
        node.right.type = hulk.NUMBER_TYPE
        return self.errors

    @visitor.when(hulk.StarNode)
    def visit(self, node, types):
        self.visit(node.left, self.types.create_child())
        self.visit(node.right, self.types.create_child())
        try:
            if node.left.child:
                if self.recurrent_type.name != hulk.NUMBER_TYPE:
                    self.errors.append(
                        f"La operación * solo esta definida entre números")
        except:
            pass
        try:
            if node.right.child:
                if self.recurrent_type.name != hulk.NUMBER_TYPE:
                    self.errors.append(
                        f"La operación * solo esta definida entre números")
        except:
            pass
        if not node.left.type:
            node.left.type = hulk.NUMBER_TYPE
            self.visit(node.left, self.types.create_child())
        if not node.right.type:
            node.right.type = hulk.NUMBER_TYPE
            self.visit(node.right, self.types.create_child())
        if node.left.type != hulk.NUMBER_TYPE or node.right.type != hulk.NUMBER_TYPE:
            self.errors.append(
                f"La operación * solo esta definida entre números")
        node.type = hulk.NUMBER_TYPE
        node.left.type = hulk.NUMBER_TYPE
        node.right.type = hulk.NUMBER_TYPE
        return self.errors

    @visitor.when(hulk.DivNode)
    def visit(self, node, types):
        self.visit(node.left, self.types.create_child())
        self.visit(node.right, self.types.create_child())
        try:
            if node.left.child:
                if self.recurrent_type.name != hulk.NUMBER_TYPE:
                    self.errors.append(
                        f"La operación / solo esta definida entre números")
        except:
            pass
        try:
            if node.right.child:
                if self.recurrent_type.name != hulk.NUMBER_TYPE:
                    self.errors.append(
                        f"La operación / solo esta definida entre números")
        except:
            pass
        if not node.left.type:
            node.left.type = hulk.NUMBER_TYPE
            self.visit(node.left, self.types.create_child())
        if not node.right.type:
            node.right.type = hulk.NUMBER_TYPE
            self.visit(node.right, self.types.create_child())
        if node.left.type != hulk.NUMBER_TYPE or node.right.type != hulk.NUMBER_TYPE:
            self.errors.append(
                f"La operación / solo esta definida entre números")
        node.type = hulk.NUMBER_TYPE
        return self.errors

    @visitor.when(hulk.PrintNode)
    def visit(self, node, types):
        self.visit(node.expr, self.types.create_child())
        if node.expr.type:
            try:
                if node.expr.child:
                    node.type = self.recurrent_type.name
                else:
                    node.type = node.expr.type
            except:
                node.type = node.expr.type
        return self.errors

    @visitor.when(hulk.PowNode)
    def visit(self, node, types):
        self.visit(node.left, self.types.create_child())
        self.visit(node.right, self.types.create_child())
        try:
            if node.left.child:
                if self.recurrent_type.name != hulk.NUMBER_TYPE:
                    self.errors.append(
                        f"La operación ^ solo esta definida entre números")
        except:
            pass
        try:
            if node.right.child:
                if self.recurrent_type.name != hulk.NUMBER_TYPE:
                    self.errors.append(
                        f"La operación ^ solo esta definida entre números")
        except:
            pass
        if not node.left.type:
            node.left.type = hulk.NUMBER_TYPE
            self.visit(node.left, self.types.create_child())
        if not node.right.type:
            node.right.type = hulk.NUMBER_TYPE
            self.visit(node.right, self.types.create_child())
        if node.left.type != hulk.NUMBER_TYPE or node.right.type != hulk.NUMBER_TYPE:
            self.errors.append(
                f"La operación ^ solo esta definida entre números")
        node.type = hulk.NUMBER_TYPE
        return self.errors

    @visitor.when(hulk.ModNode)
    def visit(self, node, types):
        self.visit(node.left, self.types.create_child())
        self.visit(node.right, self.types.create_child())
        try:
            if node.left.child:
                if self.recurrent_type.name != hulk.NUMBER_TYPE:
                    self.errors.append(
                        f"La operación % solo esta definida entre números")
        except:
            pass
        try:
            if node.right.child:
                if self.recurrent_type.name != hulk.NUMBER_TYPE:
                    self.errors.append(
                        f"La operación % solo esta definida entre números")
        except:
            pass
        if not node.left.type:
            node.left.type = hulk.NUMBER_TYPE
            self.visit(node.left, self.types.create_child())
        if not node.right.type:
            node.right.type = hulk.NUMBER_TYPE
            self.visit(node.right, self.types.create_child())
        if node.left.type != hulk.NUMBER_TYPE or node.right.type != hulk.NUMBER_TYPE:
            self.errors.append(
                f"La operación % solo esta definida entre números")
        node.type = hulk.NUMBER_TYPE
        return self.errors

    @visitor.when(hulk.EQNode)
    def visit(self, node, types):
        self.visit(node.left, self.types.create_child())
        self.visit(node.right, self.types.create_child())
        try:
            if node.left.child:
                if self.recurrent_type.name != hulk.NUMBER_TYPE:
                    self.errors.append(
                        f"La operación == solo esta definida entre números")
        except:
            pass
        try:
            if node.right.child:
                if self.recurrent_type.name != hulk.NUMBER_TYPE:
                    self.errors.append(
                        f"La operación == solo esta definida entre números")
        except:
            pass
        if not node.left.type:
            node.left.type = hulk.NUMBER_TYPE
            self.visit(node.left, self.types.create_child())
        if not node.right.type:
            node.right.type = hulk.NUMBER_TYPE
            self.visit(node.right, self.types.create_child())
        if node.left.type != hulk.NUMBER_TYPE or node.right.type != hulk.NUMBER_TYPE:
            self.errors.append(
                f"La operación == solo esta definida entre números")
        node.type = hulk.BOOL_TYPE
        return self.errors

    @visitor.when(hulk.GTNode)
    def visit(self, node, types):
        self.visit(node.left, self.types.create_child())
        self.visit(node.right, self.types.create_child())
        try:
            if node.left.child:
                if self.recurrent_type.name != hulk.NUMBER_TYPE:
                    self.errors.append(
                        f"La operación > solo esta definida entre números")
        except:
            pass
        try:
            if node.right.child:
                if self.recurrent_type.name != hulk.NUMBER_TYPE:
                    self.errors.append(
                        f"La operación > solo esta definida entre números")
        except:
            pass
        if not node.left.type:
            node.left.type = hulk.NUMBER_TYPE
            self.visit(node.left, self.types.create_child())
        if not node.right.type:
            node.right.type = hulk.NUMBER_TYPE
            self.visit(node.right, self.types.create_child())
        if node.left.type != hulk.NUMBER_TYPE or node.right.type != hulk.NUMBER_TYPE:
            self.errors.append(
                f"La operación > solo esta definida entre números")
        node.type = hulk.BOOL_TYPE
        return self.errors

    @visitor.when(hulk.LTNode)
    def visit(self, node, types):
        self.visit(node.left, self.types.create_child())
        self.visit(node.right, self.types.create_child())
        try:
            if node.left.child:
                if self.recurrent_type.name != hulk.NUMBER_TYPE:
                    self.errors.append(
                        f"La operación < solo esta definida entre números")
        except:
            pass
        try:
            if node.right.child:
                if self.recurrent_type.name != hulk.NUMBER_TYPE:
                    self.errors.append(
                        f"La operación < solo esta definida entre números")
        except:
            pass
        if not node.left.type:
            node.left.type = hulk.NUMBER_TYPE
            self.visit(node.left, self.types.create_child())
        if not node.right.type:
            node.right.type = hulk.NUMBER_TYPE
            self.visit(node.right, self.types.create_child())
        if node.left.type != hulk.NUMBER_TYPE or node.right.type != hulk.NUMBER_TYPE:
            self.errors.append(
                f"La operación < solo esta definida entre números")
        node.type = hulk.BOOL_TYPE
        return self.errors

    @visitor.when(hulk.GENode)
    def visit(self, node, types):
        self.visit(node.left, self.types.create_child())
        self.visit(node.right, self.types.create_child())
        try:
            if node.left.child:
                if self.recurrent_type.name != hulk.NUMBER_TYPE:
                    self.errors.append(
                        f"La operación >= solo esta definida entre números")
        except:
            pass
        try:
            if node.right.child:
                if self.recurrent_type.name != hulk.NUMBER_TYPE:
                    self.errors.append(
                        f"La operación >= solo esta definida entre números")
        except:
            pass
        if not node.left.type:
            node.left.type = hulk.NUMBER_TYPE
            self.visit(node.left, self.types.create_child())
        if not node.right.type:
            node.right.type = hulk.NUMBER_TYPE
            self.visit(node.right, self.types.create_child())
        if node.left.type != hulk.NUMBER_TYPE or node.right.type != hulk.NUMBER_TYPE:
            self.errors.append(
                f"La operación >= solo esta definida entre números")
        node.type = hulk.BOOL_TYPE
        return self.errors

    @visitor.when(hulk.LENode)
    def visit(self, node, types):
        self.visit(node.left, self.types.create_child())
        self.visit(node.right, self.types.create_child())
        try:
            if node.left.child:
                if self.recurrent_type.name != hulk.NUMBER_TYPE:
                    self.errors.append(
                        f"La operación <= solo esta definida entre números")
        except:
            pass
        try:
            if node.right.child:
                if self.recurrent_type.name != hulk.NUMBER_TYPE:
                    self.errors.append(
                        f"La operación <= solo esta definida entre números")
        except:
            pass
        if not node.left.type:
            node.left.type = hulk.NUMBER_TYPE
            self.visit(node.left, self.types.create_child())
        if not node.right.type:
            node.right.type = hulk.NUMBER_TYPE
            self.visit(node.right, self.types.create_child())
        if node.left.type != hulk.NUMBER_TYPE or node.right.type != hulk.NUMBER_TYPE:
            self.errors.append(
                f"La operación <= solo esta definida entre números")
        node.type = hulk.BOOL_TYPE
        return self.errors

    @visitor.when(hulk.NENode)
    def visit(self, node, types):
        self.visit(node.left, self.types.create_child())
        self.visit(node.right, self.types.create_child())
        try:
            if node.left.child:
                if self.recurrent_type.name != hulk.NUMBER_TYPE:
                    self.errors.append(
                        f"La operación != solo esta definida entre números")
        except:
            pass
        try:
            if node.right.child:
                if self.recurrent_type.name != hulk.NUMBER_TYPE:
                    self.errors.append(
                        f"La operación != solo esta definida entre números")
        except:
            pass
        if not node.left.type:
            node.left.type = hulk.NUMBER_TYPE
            self.visit(node.left, self.types.create_child())
        if not node.right.type:
            node.right.type = hulk.NUMBER_TYPE
            self.visit(node.right, self.types.create_child())
        if node.left.type != hulk.NUMBER_TYPE or node.right.type != hulk.NUMBER_TYPE:
            self.errors.append(
                f"La operación != solo esta definida entre números")
        node.type = hulk.BOOL_TYPE
        return self.errors

    @visitor.when(hulk.AndNode)
    def visit(self, node, types):
        self.visit(node.left, self.types.create_child())
        self.visit(node.right, self.types.create_child())
        try:
            if node.left.child:
                if self.recurrent_type.name != hulk.BOOL_TYPE:
                    self.errors.append(
                        f"La operación & solo esta definida entre números")
        except:
            pass
        try:
            if node.right.child:
                if self.recurrent_type.name != hulk.BOOL_TYPE:
                    self.errors.append(
                        f"La operación & solo esta definida entre números")
        except:
            pass
        if not node.left.type:
            node.left.type = hulk.BOOL_TYPE
            self.visit(node.left, self.types.create_child())
        if not node.right.type:
            node.right.type = hulk.BOOL_TYPE
            self.visit(node.right, self.types.create_child())
        if node.left.type != hulk.BOOL_TYPE or node.right.type != hulk.BOOL_TYPE:
            self.errors.append(
                f"La operación & solo esta definida entre booleanos")
        node.type = hulk.BOOL_TYPE
        return self.errors

    @visitor.when(hulk.OrNode)
    def visit(self, node, types):
        self.visit(node.left, self.types.create_child())
        self.visit(node.right, self.types.create_child())
        try:
            if node.left.child:
                if self.recurrent_type.name != hulk.BOOL_TYPE:
                    self.errors.append(
                        f"La operación | solo esta definida entre números")
        except:
            pass
        try:
            if node.right.child:
                if self.recurrent_type.name != hulk.BOOL_TYPE:
                    self.errors.append(
                        f"La operación | solo esta definida entre números")
        except:
            pass
        if not node.left.type:
            node.left.type = hulk.BOOL_TYPE
            self.visit(node.left, self.types.create_child())
        if not node.right.type:
            node.right.type = hulk.BOOL_TYPE
            self.visit(node.right, self.types.create_child())
        if node.left.type != hulk.BOOL_TYPE or node.right.type != hulk.BOOL_TYPE:
            self.errors.append(
                f"La operación | solo esta definida entre booleanos")
        node.type = hulk.BOOL_TYPE
        return self.errors

    @visitor.when(hulk.NotNode)
    def visit(self, node, types):
        self.visit(node.lex, self.types.create_child())
        try:
            if node.lex.child:
                if self.recurrent_type.name != hulk.BOOL_TYPE:
                    self.errors.append(
                        f"La operación ! solo esta definida entre números")
        except:
            pass
        if not node.lex.type:
            node.lex.type = hulk.BOOL_TYPE
            self.visit(node.lex, self.types.create_child())
        if node.lex.type != hulk.BOOL_TYPE:
            self.errors.append(
                f"La operación ! solo esta definida para booleanos")
        node.type = hulk.BOOL_TYPE
        return self.errors

    @visitor.when(hulk.ConcatNode)
    def visit(self, node, types):
        self.visit(node.left, self.types.create_child())
        self.visit(node.right, self.types.create_child())
        # if node.left.type != hulk.STRING_TYPE or node.right.type != hulk.STRING_TYPE:
        #     self.errors.append(f"La operación @ solo esta definida entre cadenas")
        node.type = hulk.STRING_TYPE
        return self.errors

    @visitor.when(hulk.ConcatSpaceNode)
    def visit(self, node, types):
        self.visit(node.left, self.types.create_child())
        self.visit(node.right, self.types.create_child())
        # if node.left.type != hulk.STRING_TYPE or node.right.type != hulk.STRING_TYPE:
        #     self.errors.append(f"La operación @@ solo esta definida entre cadenas")
        node.type = hulk.STRING_TYPE
        return self.errors

    @visitor.when(hulk.IdentifierNode)
    def visit(self, node, types):
            
        if not node.type:
            node.type = self.types.get_variable_info(node.name)
        else:
            if(node.name in self.var.keys()):
                self.var[node.name] = node.type
            self.types.dict[node.name] = node.type

        if node.child:
            if node.type:
                # self.recurrent_type = self.context.get_type(node.type)
                # self.visit(node.child, self.types.create_child())
                # self.recurrent_type = self.context.get_type(node.child.type)
                # self.recurrent_type = None
                pass
            else:
                if node.name == 'self':
                    try:
                        node.type = self.current_type.get_attribute(node.child.name).type
                    except:
                        node.type = self.current_type.get_method(node.child.name).return_type
        return self.errors

    # self

    @visitor.when(hulk.SinNode)
    def visit(self, node, types):
        self.visit(node.expr, self.types.create_child())
        if not node.expr.type:
            node.expr.type = hulk.NUMBER_TYPE
            self.visit(node.expr, self.types.create_child())
        if node.expr.type != hulk.NUMBER_TYPE:
            self.errors.append(
                f"La función seno solo está definida en números")
        node.type = hulk.NUMBER_TYPE
        return self.errors

    @visitor.when(hulk.CosNode)
    def visit(self, node, types):
        self.visit(node.expr, self.types.create_child())
        if not node.expr.type:
            node.expr.type = hulk.NUMBER_TYPE
            self.visit(node.expr, self.types.create_child())
        if node.expr.type != hulk.NUMBER_TYPE:
            self.errors.append(
                f"La función coseno solo está definida en números")
        node.type = hulk.NUMBER_TYPE

        return self.errors

    @visitor.when(hulk.SqrtNode)
    def visit(self, node, types):
        self.visit(node.expr, self.types.create_child())
        if not node.expr.type:
            node.expr.type = hulk.NUMBER_TYPE
            self.visit(node.expr, self.types.create_child())
        if node.expr.type != hulk.NUMBER_TYPE:
            self.errors.append(
                f"La función raíz cuadrada solo está definida en números")
        node.type = hulk.NUMBER_TYPE
        return self.errors

    @visitor.when(hulk.ExpNode)
    def visit(self, node, types):
        self.visit(node.expr, self.types.create_child())
        if not node.expr.type:
            node.expr.type = hulk.NUMBER_TYPE
            self.visit(node.expr, self.types.create_child())
        if node.expr.type != hulk.NUMBER_TYPE:
            self.errors.append(
                f"La función exponencial solo está definida en números")
        node.type = hulk.NUMBER_TYPE
        return self.errors

    @visitor.when(hulk.LogNode)
    def visit(self, node, types):
        self.visit(node.base, self.types.create_child())
        self.visit(node.arg, self.types.create_child())
        try:
            if node.base.child:
                if self.recurrent_type.name != hulk.NUMBER_TYPE:
                    self.errors.append(
                        f"La operación log solo esta definida entre números")
        except:
            pass
        try:
            if node.arg.child:
                if self.recurrent_type.name != hulk.NUMBER_TYPE:
                    self.errors.append(
                        f"La operación log solo esta definida entre números")
        except:
            pass
        if not node.base.type:
            node.base.type = hulk.NUMBER_TYPE
            self.visit(node.base, self.types.create_child())
        if not node.arg.type:
            node.arg.type = hulk.NUMBER_TYPE
            self.visit(node.arg, self.types.create_child())
        if node.base.type != hulk.NUMBER_TYPE or node.arg.type != hulk.NUMBER_TYPE:
            self.errors.append(
                f"La operación log solo esta definida entre números")
        node.type = hulk.NUMBER_TYPE
        return self.errors
