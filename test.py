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
        generated_c_file = f'{base_name}.c'
        generated_a_out = 'a.out'
        
        # Ejecuta el compilador
        subprocess.run([self.compiler_path, input_path])


        # Ejecuta el programa generado y guarda la salida
        with open(actual_output_path, 'w') as output_file:
            subprocess.run(['./a.out'], stdout=output_file, stderr=subprocess.STDOUT)

        # Compara el archivo de salida generado con el archivo de salida esperado
        self.assertTrue(filecmp.cmp(expected_output_path, actual_output_path), 
                        f"Output for {input_file} does not match expected output")

    def test_case_1(self):
        self.compile_and_compare('test1.uh', 'test1.output')

    def test_case_2(self):
        self.compile_and_compare('test2.uh', 'test2.output')

    def test_case_3(self):
        self.compile_and_compare('test3.uh', 'test3.output')

    # def test_case_4(self):
    #     self.compile_and_compare('test4.uh', 'test4.output')

    def test_case_5(self):
        self.compile_and_compare('test5.uh', 'test5.output')

    def test_case_6(self):
        self.compile_and_compare('test6.uh', 'test6.output')

    # def test_case_7(self):
    #     self.compile_and_compare('test7.uh', 'test7.output')
        
    def test_case_8(self):
        self.compile_and_compare('test8.uh', 'test8.output')
    
    def test_case_9(self):
        self.compile_and_compare('test9.uh', 'test9.output')
    
    # def test_case_10(self):
    #     self.compile_and_compare('test10.uh', 'test10.output')

    # Agrega más métodos de prueba para cada caso de prueba adicional

if __name__ == '__main__':
    unittest.main()
