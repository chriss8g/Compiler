class TACInstruction:
    pass

class TACOperation(TACInstruction):
    def __init__(self, operation, arg1, arg2, result, data_type):
        self.operation = operation
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result
        self.data_type = data_type

    def __str__(self):
        return f"{self.result} = {self.arg1} {self.operation} {self.arg2}"

class TACFunctionCall(TACInstruction):
    def __init__(self, function_name, args, result):
        self.function_name = function_name
        self.args = args
        self.result = result

    def __str__(self):
        args_str = ", ".join(self.args)
        return f"{self.result} = {self.function_name}({args_str})"

class TACPrint(TACInstruction):
    def __init__(self, arg, data_type):
        self.arg = arg
        self.data_type = data_type

    def __str__(self):
        return f"print {self.arg} of type {self.data_type}"

class TACConcat(TACInstruction):
    def __init__(self, arg1, arg2, result):
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result

    def __str__(self):
        return f"{self.result} = {self.arg1} @ {self.arg2}"