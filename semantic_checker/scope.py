class VariableInfo:
    def __init__(self, name, type=None):
        self.name = name
        self.type = type

class FunctionInfo:
    def __init__(self, name, params):
        self.name = name
        self.params = params

import itertools as itl

class Scope:
    def __init__(self, parent=None):
        self.local_vars = []
        self.local_funcs = []
        self.parent = parent
        self.children = []
        self.var_index_at_parent = 0 if parent is None else len(parent.local_vars)
        self.func_index_at_parent = 0 if parent is None else len(parent.local_funcs)
        self.dict = {}
        
    def create_child_scope(self):
        child_scope = Scope(parent=self)
        self.children.append(child_scope)
        return child_scope

    def define_variable(self, vname, type=None):
        variable = VariableInfo(vname, type)
        self.local_vars.append(variable)
        self.var_index_at_parent += 1
        return variable
    
    def define_function(self, fname, params):
        my_function = FunctionInfo(fname, params)
        self.local_funcs.append(my_function)
        self.func_index_at_parent += 1
        return my_function

    def is_var_defined(self, vname):
        # print([x.name for x in self.local_vars])
        if vname in [i.name for i in self.local_vars]:
            return True
        elif self.parent:
            return self.parent.is_var_defined(vname)
        
        return False
    
    def get_variable_info(self, vname):    
        if self.is_local_var(vname) or self.parent:
            if self.is_local_var(vname):
                # print(self.parent.get_variable_info(vname))
                if(vname in self.dict.keys()):
                    return self.dict[vname], False
                else:
                    return vname, True
            else:
                # print(self.parent.get_variable_info(vname))
                return self.parent.get_variable_info(vname)
        else:
            # print(vname)
            return vname, True
    
    def is_func_defined(self, fname, n):
        if (fname, n) in [(i.name, i.params) for i in self.local_funcs]:
            return True
        elif self.parent:
            return self.parent.is_func_defined(fname, n)
        
        return False


    def is_local_var(self, vname):
        return self.get_local_variable_info(vname) is not None
    
    def is_local_func(self, fname, n):
        return self.get_local_function_info(fname, n) is not None

    def get_local_variable_info(self, vname):
        for i in self.local_vars:
            if vname == i.name:
                return i
        return None
    
    def get_local_function_info(self, fname, n):
        return self.local_funcs[fname] if (fname, n) in [(i.name, i.params) for i in self.local_funcs] else None
    