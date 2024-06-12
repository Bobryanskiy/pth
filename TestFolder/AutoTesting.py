import yaml
import unittest


def load_tests(loader, standard_tests, pattern):
    with open('D:\Projects\PyCharm\pythonProject1\\tests.yaml', 'r') as file:
        tests_to_run = yaml.safe_load(file)

        selected_tests = []
        for module in tests_to_run:
            for test_name in tests_to_run[module]['tests']:
                full_test_name = f'{module}.{test_name}'
                selected_tests.append(full_test_name)

    return selected_tests


suite = unittest.TestSuite()

for test_class in   load_tests(unittest.defaultTestLoader, suite, '. * '):
    suite.addTests(unittest.defaultTestLoader.loadTestsFromName(test_class))

runner = unittest.TextTestRunner()
result = runner.run(suite)

if result.wasSuccessful():
    print('All tests passed successfully.')
else:
    print('Some tests failed. Check the output above.')
