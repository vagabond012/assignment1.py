import unittest
from intercept_algo import intercept

class TestInterceptEdgeCases(unittest.TestCase):
    def test_never(self):
        roads = [(0, 1, 1, 1), (1, 0, 1, 1), (2, 1, 5, 1)]
        stations = [(0, 1), (1, 1)]
        start = 2
        friendStart = 0
        expected_output = (5, 1, [2, 1])
        result = intercept(roads, stations, start, friendStart)
        self.assertEqual(result, expected_output)

    def test_gonna(self):
        roads = [(0, 1, 35, 3), (1, 0, 1, 1), (2, 0, 10, 5)]
        stations = [(0, 3), (1, 2)]
        start = 2
        friendStart = 0
        expected_output = (10, 5, [2, 0])
        result = intercept(roads, stations, start, friendStart)
        self.assertEqual(result, expected_output)

    def test_give(self):
        roads = [(0, 1, 1, 2), (1, 2, 1, 3), (2, 0, 1, 5), (3, 0, 10, 10)]
        stations = [(0, 2), (1, 3), (2, 5)]
        start = 3
        friendStart = 0
        expected_output = (10, 10, [3, 0])
        result = intercept(roads, stations, start, friendStart)
        self.assertEqual(result, expected_output)

    def test_you(self):
        roads = [(0, 1, 1, 1), (1, 0, 5, 2)]
        stations = [(0, 1), (1, 1)]
        start = 1
        friendStart = 0
        expected_output = (5, 2, [1, 0])
        result = intercept(roads, stations, start, friendStart)
        self.assertEqual(result, expected_output)

    def test_up(self):
        roads = [(0, 1, 1, 2), (1, 2, 1, 3), (2, 0, 1, 5), (3, 2, 10, 5), (3, 0, 5, 1)]
        stations = [(0, 2), (1, 3), (2, 5)]
        start = 3
        friendStart = 0
        expected_output = (10, 5, [3, 2])
        result = intercept(roads, stations, start, friendStart)
        self.assertEqual(result, expected_output)

    def test_never_(self):
        roads = [(0, 1, 1, 1), (1, 2, 1, 2), (2, 0, 1, 3), (3, 2, 10, 3), (3, 0, 5, 1)]
        stations = [(0, 1), (1, 2), (2, 3)]
        start = 3
        friendStart = 0
        expected_output = (10, 3, [3, 2])
        result = intercept(roads, stations, start, friendStart)
        self.assertEqual(result, expected_output)

    def test_gonna_(self):
        roads = [(3, 2, 5, 2), (0, 1, 1, 1), (1, 2, 1, 1), (2, 0, 1, 1), (3, 0, 10, 1)]
        stations = [(0, 1), (1, 1), (2, 1)]
        start = 3
        friendStart = 0
        expected_output = (5, 2, [3, 2])
        result = intercept(roads, stations, start, friendStart)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestInterceptEdgeCases)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    print("\nSummary:")
    print("Run:", result.testsRun)
    print("Failures:", len(result.failures))
    print("Errors:", len(result.errors))
    if result.failures:
        print("Failure details:")
        for case, traceback in result.failures:
            print("-", case)
    if result.errors:
        print("Error details:")
        for case, traceback in result.errors:
            print("-", case)
