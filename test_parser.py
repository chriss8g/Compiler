import unittest
from my_parser import CodeToAST

class TestCodeToAST(unittest.TestCase):

    def setUp(self):
        self.test = 'test_14'
        """Configura el entorno antes de cada prueba."""
        # Abre y lee el contenido del archivo donde se espera que esté el resultado correcto
        with open(f'tests/parser/inputs/{self.test}.uh', 'r') as file:
            self.text = file.read()
        self.code_to_ast = CodeToAST(self.text)
        
    def test_init(self):
        """Prueba la inicialización de la clase CodeToAST."""
        # self.assertIsInstance(self.code_to_ast, CodeToAST)
        # self.assertEqual(self.code_to_ast.ast, None)  # Reemplaza expected_ast con lo que esperas obtener
        pass

    def test_repr(self):
        """Prueba el método __repr__ de la clase CodeToAST leyendo el resultado esperado de un archivo."""
        actual_output = repr(self.code_to_ast)
       
        # Abre y lee el contenido del archivo donde se espera que esté el resultado correcto
        with open(f'tests/parser/expected_out/{self.test}.txt', 'r') as file:
            expected_output = file.read()
        
        # Abre el archivo en modo de escritura ('w')
        with open(f'tests/parser/actual_out/{self.test}.txt', 'w') as archivo:
            # Escribe el string en el archivo
            archivo.write(actual_output)
            
        self.assertEqual(actual_output, expected_output)

# Función principal para ejecutar todas las pruebas en una sola corrida
def run_all_tests():
    suite = unittest.TestSuite()
    
    # Itera sobre todos los archivos en la carpeta inputs
    for filename in os.listdir('tests/parser/inputs'):
        if filename.endswith('.uh'):  # Asume que todos los archivos relevantes son .txt
            test = TestCodeToAST(filename)
            suite.addTest(test)
    
    runner = unittest.TextTestRunner()
    results = runner.run(suite)

if __name__ == '__main__':
    unittest.main()
    # run_all_tests()
