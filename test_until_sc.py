import unittest
from my_parser1 import CodeToAST
from semantic_checker_visitor import SemanticCheckerVisitor

class TestSemanticChecker(unittest.TestCase):

    def check_semantics(self, code):
        ast = CodeToAST(code)
        checker = SemanticCheckerVisitor()
        errors = checker.visit(ast.ast)
        return errors

    def test_undeclared_variable(self):
        code = 'x + 5;'
        errors = self.check_semantics(code)
        self.assertIn('Variable x no declarada!', errors)

    def test_double_declaration_variable(self):
        code = 'let x = 5 in let x = 10 in x + 1;'
        errors = self.check_semantics(code)
        self.assertIn('Variable x doblemente declarada!', errors)

    def test_undeclared_function(self):
        code = 'let x = f(5) in x + 1;'
        errors = self.check_semantics(code)
        self.assertIn('Funcion f no declarada!', errors)

    def test_double_declaration_function(self):
        code = '''
            function f(a) => a + 1;
            function f(b) => b + 2;
        '''
        errors = self.check_semantics(code)
        self.assertIn('Funcion f doblemente declarada!', errors)

    def test_incompatible_types_arithmetic(self):
        code = '''
            let x = 5 in
            let y = "hello" in
            x + y;
        '''
        errors = self.check_semantics(code)
        self.assertIn('Tipos incompatibles en operación aritmética: int y string', errors)

    def test_incompatible_types_logic(self):
        code = '''
            let x = true in
            let y = 5 in
            x and y;
        '''
        errors = self.check_semantics(code)
        self.assertIn('Tipos incompatibles en operación lógica: bool y int', errors)

    def test_incompatible_types_comparison(self):
        code = '''
            let x = 5 in
            let y = "hello" in
            x == y;
        '''
        errors = self.check_semantics(code)
        self.assertIn('Tipos incompatibles en operación comparativa: int y string', errors)

    def test_correct_if_condition(self):
        code = '''
            let x = 5 in
            if (x > 3) {
                print(x);
            } else {
            0;
            }
        '''
        errors = self.check_semantics(code)
        self.assertEqual(errors, [])

    def test_incorrect_if_condition(self):
        code = '''
            let x = 5 in
            if (x + "hello") {
                print(x);
            } else
            {
            0;
            }
        '''
        errors = self.check_semantics(code)
        self.assertIn('Condición de if debe ser booleana, no int', errors)

    def test_correct_while_condition(self):
        code = '''
            let x = 0 in
            while (x < 10) {
                x := x + 1;
            }
        '''
        errors = self.check_semantics(code)
        self.assertEqual(errors, [])

    def test_incorrect_while_condition(self):
        code = '''
            let x = 0 in
            while (x + "hello") {
                x := x + 1;
            }
        '''
        errors = self.check_semantics(code)
        self.assertIn('Condición de while debe ser booleana, no int', errors)

    def test_correct_for_loop(self):
        code = '''
            for (i in range(0, 10)) {
                print(i);
            }
        '''
        errors = self.check_semantics(code)
        self.assertEqual(errors, [])

    def test_incorrect_for_loop(self):
        code = '''
            for (i in range("a", "z")) {
                print(i);
            }
        '''
        errors = self.check_semantics(code)
        self.assertIn('Iterador de for debe ser numérico, no string', errors)

if __name__ == '__main__':
    unittest.main()
