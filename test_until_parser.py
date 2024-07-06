import unittest
from my_parser import CodeToAST

class TestCodeToAST(unittest.TestCase):

# work
    def test_simple_print(self):
        code = 'print(42);'
        ast = CodeToAST(code)
        self.assertIsNotNone(ast)
        self.assertIn('PrintNode', repr(ast))

# work
    def test_var_declaration(self):
        code = 'let x = 5 in x + 3;'
        ast = CodeToAST(code)
        self.assertIsNotNone(ast)
        self.assertIn('LetNode', repr(ast))

# work 3
    def test_function_declaration(self):
        code = '''
                function add(a, b) => a + b;
                
                print(a);
            '''
        ast = CodeToAST(code)
        self.assertIsNotNone(ast)
        self.assertIn('FuncDeclarationNode', repr(ast))

# work 4
    def test_while_loop(self):
        code = '''
                let a = 10 in while (a >= 0) {
                        print(a);
                        a := a - 1;
                        };
                '''
        ast = CodeToAST(code)
        self.assertIsNotNone(ast.ast)
        self.assertIn('WhileNode', repr(ast))

# work 5
    def test_for_loop(self):
        code = 'for (x in range(0, 10)) print (x);'
        ast = CodeToAST(code)
        self.assertIsNotNone(ast.ast)
        self.assertIn('LetNode', repr(ast))

# work 6
    def test_if_else(self):
        code = 'if (x == 10) print("less"); else print("more");'
        ast = CodeToAST(code)
        self.assertIsNotNone(ast.ast)
        self.assertIn('IfNode', repr(ast))

# work 7
    def test_complex_expression(self):
        code = '''let x = 5 in
                                 let y = 6 in
                                         x + y * (x - y);'''
        ast = CodeToAST(code)
        self.assertIsNotNone(ast.ast)
        self.assertIn('LetNode', repr(ast))

# work 8
    def test_function_call(self):
        code = 'let x = f(5, 7) in x + 1;'
        ast = CodeToAST(code)
        self.assertIsNotNone(ast.ast)
        self.assertIn('CallNode', repr(ast))

# work 9
    def test_object_creation(self):
        code = 'new MyClass(5, "hello");'
        ast = CodeToAST(code)
        self.assertIsNotNone(ast.ast)
        self.assertIn('ObjectCreationNode', repr(ast))

# work 10
    def test_method_call(self):
        code = 'obj.method(1, 2);'
        ast = CodeToAST(code)
        self.assertIsNotNone(ast.ast)
        self.assertIn('MethodCallNode', repr(ast))

# work 11
    def test_type_declaration_simple(self):
        code = '''
            type MyClass {
                a = 5 ;
                method(x) => x + self.a;
            }
            print("hello");
        '''
        ast = CodeToAST(code)
        self.assertIsNotNone(ast.ast)
        self.assertIn('TypeNode', repr(ast))

# work 12
    def test_type_declaration(self):
        code = '''
            type MyClass {
                a = 5 ;
                method(x) => x + self.a;
            }
            new MyClass(5, "hello");
        '''
        ast = CodeToAST(code)
        self.assertIsNotNone(ast.ast)
        self.assertIn('TypeNode', repr(ast))
        
# work 13
    def test_super(self):
        code = '''
                type MyClass {
                    x = 0;
                    
                    my_method(a, b) => {
                        a+b;
                    };
                }

                let a = 10, b = 20, c = 30 in {
                    print(a + b * c);
                    
                    if (a > b) {
                        print(a);
                    } else {
                        print(b);
                    };
                    
                    while (a < c) {
                        print(a);
                        a := a + 1;
                    };
                    
                    for (i in range(3, 4)) {
                        print(i);
                    };
                    
                    let d = new MyClass(5, 10) in {
                        print(d);
                    };
                };
        '''
        ast = CodeToAST(code)
        self.assertIsNotNone(ast.ast)

if __name__ == '__main__':
    unittest.main()
