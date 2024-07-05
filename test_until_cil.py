import unittest
from my_parser import CodeToAST
from CIL_generator_visitor import HULKToCILVisitor
import cil as cil

class TestCodeToCIL(unittest.TestCase):
    def setUp(self):
        # Configura el entorno para cada test, como el contexto y el visitante
        self.context = None  # Configurar el contexto adecuado
        self.visitor = HULKToCILVisitor(self.context)
        self.formatter = cil.get_formatter()

    def test_simple_print(self):
        code = 'print(42);'
        ast = CodeToAST(code).ast
        self.assertIsNotNone(ast)
        cil_ast = self.visitor.visit(ast)
        self.assertIsInstance(cil_ast, cil.ProgramNode)
        self.assertIn('PRINT', self.formatter(cil_ast))

    # def test_var_declaration(self):
    #     code = 'let x = 5 in x + 3;'
    #     ast = CodeToAST(code).ast
    #     self.assertIsNotNone(ast)
    #     cil_ast = self.visitor.visit(ast)
    #     self.assertIsInstance(cil_ast, cil.ProgramNode)
    #     self.assertIn('AssignNode', self.formatter(cil_ast))

    # def test_function_declaration(self):
    #     code = '''
    #         function add(a, b) => a + b;
    #         print(add(3, 4));
    #     '''
    #     ast = CodeToAST(code).ast
    #     self.assertIsNotNone(ast)
    #     cil_ast = self.visitor.visit(ast, None)
    #     self.assertIsInstance(cil_ast, cil.ProgramNode)
    #     self.assertIn('FunctionNode', repr(cil_ast))
    #     self.assertIn('StaticCallNode', repr(cil_ast))

    # def test_while_loop(self):
    #     code = '''
    #         let a = 10 in while (a >= 0) {
    #             print(a);
    #             a := a - 1;
    #         };
    #     '''
    #     ast = CodeToAST(code).ast
    #     self.assertIsNotNone(ast)
    #     cil_ast = self.visitor.visit(ast, None)
    #     self.assertIsInstance(cil_ast, cil.ProgramNode)
    #     self.assertIn('WhileNode', repr(cil_ast))

    # def test_for_loop(self):
    #     code = 'for (x in range(0, 10)) print (x);'
    #     ast = CodeToAST(code).ast
    #     self.assertIsNotNone(ast)
    #     cil_ast = self.visitor.visit(ast, None)
    #     self.assertIsInstance(cil_ast, cil.ProgramNode)
    #     self.assertIn('ForRangeNode', repr(cil_ast))

    # def test_if_else(self):
    #     code = 'if (x < 10) print("less"); else print("more");'
    #     ast = CodeToAST(code).ast
    #     self.assertIsNotNone(ast)
    #     cil_ast = self.visitor.visit(ast, None)
    #     self.assertIsInstance(cil_ast, cil.ProgramNode)
    #     self.assertIn('IfNode', repr(cil_ast))

    # def test_complex_expression(self):
    #     code = '''
    #         let x = 5 in
    #         let y = 6 in
    #         x + y * (x - y);
    #     '''
    #     ast = CodeToAST(code).ast
    #     self.assertIsNotNone(ast)
    #     cil_ast = self.visitor.visit(ast, None)
    #     self.assertIsInstance(cil_ast, cil.ProgramNode)
    #     self.assertIn('AssignNode', repr(cil_ast))

    # def test_function_call(self):
    #     code = 'let x = f(5, 7) in x + 1;'
    #     ast = CodeToAST(code).ast
    #     self.assertIsNotNone(ast)
    #     cil_ast = self.visitor.visit(ast, None)
    #     self.assertIsInstance(cil_ast, cil.ProgramNode)
    #     self.assertIn('CallNode', repr(cil_ast))

    # def test_object_creation(self):
    #     code = 'new MyClass(5, "hello");'
    #     ast = CodeToAST(code).ast
    #     self.assertIsNotNone(ast)
    #     cil_ast = self.visitor.visit(ast, None)
    #     self.assertIsInstance(cil_ast, cil.ProgramNode)
    #     self.assertIn('ObjectCreationNode', repr(cil_ast))

    # def test_type_declaration(self):
    #     code = '''
    #         type MyClass {
    #             a = 5 ;
    #             method(x) => x + self.a;
    #         }
    #         new MyClass(5, "hello");
    #     '''
    #     ast = CodeToAST(code).ast
    #     self.assertIsNotNone(ast)
    #     cil_ast = self.visitor.visit(ast, None)
    #     self.assertIsInstance(cil_ast, cil.ProgramNode)
    #     self.assertIn('TypeNode', repr(cil_ast))

    # def test_super(self):
    #     code = '''
    #         type MyClass {
    #             x = 0;
    #             my_method(a, b) => {
    #                 a + b;
    #             };
    #         }
    #         let a = 10, b = 20, c = 30 in {
    #             print(a + b * c);
    #             if (a > b) {
    #                 print(a);
    #             } else {
    #                 print(b);
    #             };
    #             while (a < c) {
    #                 print(a);
    #                 a := a + 1;
    #             };
    #             for (i in range(3, 4)) {
    #                 print(i);
    #             };
    #             let d = new MyClass(5, 10) in {
    #                 print(d);
    #             };
    #         };
    #     '''
    #     ast = CodeToAST(code).ast
    #     self.assertIsNotNone(ast)
    #     cil_ast = self.visitor.visit(ast, None)
    #     self.assertIsInstance(cil_ast, cil.ProgramNode)
    #     self.assertIn('TypeNode', repr(cil_ast))

if __name__ == '__main__':
    unittest.main()
