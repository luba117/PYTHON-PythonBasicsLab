import unittest

if __name__ == "__main__":
    # This finds all files starting with 'test_' in the 'tests' directory
    loader = unittest.TestLoader()
    suite = loader.discover('tests')

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)