import nodes_types.cil as cil
from semantic_checker.scope import VariableInfo


class BaseHULKToCILVisitor:
    def __init__(self, context):
        self.dottypes = []
        self.dotdata = []
        self.dotcode = []
        self.current_type = None
        self.current_method = None
        self.current_function = None
        self.context = context
    
    @property
    def params(self):
        return self.current_function.params

    @property
    def localvars(self):
        return self.current_function.localvars

    @property
    def instructions(self):
        return self.current_function.instructions

    def register_local(self, vinfo):
        vinfo.name = f'local_{self.current_function.name[9:]}_{vinfo.name}_{len(self.localvars)}'
        local_node = cil.LocalNode(vinfo.name, vinfo.type)
        self.localvars.append(local_node)
        return vinfo.name

    def define_internal_local(self, type=None):
        vinfo = VariableInfo('internal', type)
        return self.register_local(vinfo)

    def register_instruction(self, instruction):
        self.instructions.append(instruction)
        return instruction
    
    def register_param(self, param):
        self.current_function.params.append(param)
        return param
    
    def to_function_name_in_type(self, method_name, type_name):
        return f'function_{method_name}_at_{type_name}'

    def to_function_name(self, method_name):
        return f'function_{method_name}_{len(self.dotcode)}'
    
    def to_param_name(self, param_name):
        return f'param_{param_name}_{len(self.params)}'
    
    def register_function(self, function_name, typex, params=None):
        params = params if params else []
        function_node = cil.FunctionNode(function_name, params, [], [], typex)
        self.dotcode.append(function_node)
        return function_node
    
    def register_type(self, name):
        type_node = cil.TypeNode(name)
        self.dottypes.append(type_node)
        return type_node

    def register_data(self, value):
        vname = f'data_{len(self.dotdata)}'
        data_node = cil.DataNode(vname, value)
        self.dotdata.append(data_node)
        return vname