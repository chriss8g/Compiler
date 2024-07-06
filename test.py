import unittest
import subprocess
import filecmp
import os

class CompilerTestCase(unittest.TestCase):
    def setUp(self):
        self.compiler_path = 'hulk'  # Ajusta esto a la ubicación de tu compilador
        self.test_dir = os.path.dirname(__file__)
        self.inputs_dir = os.path.join(self.test_dir, 'tests/inputs')
        self.expected_outputs_dir = os.path.join(self.test_dir, 'tests/expected_outputs')
        self.actual_outputs_dir = os.path.join(self.test_dir, 'tests/actual_outputs')
        
        # Crea el directorio para los archivos de salida actuales si no existe
        if not os.path.exists(self.actual_outputs_dir):
            os.makedirs(self.actual_outputs_dir)

    def compile_and_compare(self, input_file, expected_output_file):
        input_path = os.path.join(self.inputs_dir, input_file)
        base_name = os.path.splitext(input_file)[0]
        expected_output_path = os.path.join(self.expected_outputs_dir, expected_output_file)
        actual_output_path = os.path.join(self.actual_outputs_dir, expected_output_file)
        
        # Ejecuta el compilador
        subprocess.run([self.compiler_path, input_path])

        # Ejecuta el programa generado y guarda la salida
        with open(actual_output_path, 'w') as output_file:
            subprocess.run(['./a.out'], stdout=output_file, stderr=subprocess.STDOUT)

        # Compara el archivo de salida generado con el archivo de salida esperado
        self.assertTrue(filecmp.cmp(expected_output_path, actual_output_path), 
                        f"Output for {input_file} does not match expected output")

    @staticmethod
    def generate_test_case(input_file, expected_output_file):
        def test_case(self):
            self.compile_and_compare(input_file, expected_output_file)
        return test_case

# Lista de tuplas con nombres de archivos de entrada y salida esperada
test_cases = [
    ('test1.uh', 'test1.output'),
    ('test2.uh', 'test2.output'),
    ('test6.uh', 'test6.output'),
    ('test8.uh', 'test8.output'),
    ('test13.uh', 'test13.output'),
    ('test14.uh', 'test14.output'),
    ('test16.uh', 'test16.output'),
]

# Generar dinámicamente los métodos de prueba
for i, (input_file, expected_output_file) in enumerate(test_cases, start=1):
    test_method = CompilerTestCase.generate_test_case(input_file, expected_output_file)
    setattr(CompilerTestCase, f'test_case_{i}', test_method)

if __name__ == '__main__':
    unittest.main()
