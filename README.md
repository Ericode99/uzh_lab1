# Testing Framework for file_manager.py

This README provides an overview of the testing framework designed to test functions in the `file_manager.py` module.

## Features

1. **Three Test States**: The framework implements three states for a test: `PASS`, `FAIL`, and `ERROR`.
2. **Introspection**: The program uses introspection to discover and execute test functions automatically. Only functions with a `test_` prefix are considered.
3. **Timing**: The result of each test, along with its execution time, is printed.
4. **Setup and Teardown**: `setup` and `teardown` functions are called before and after each test, respectively. This ensures a clean environment for each test.
5. **Selective Test Execution**: The framework allows the user to specify a pattern to select which tests to run using the `--select pattern` command-line option.

## Running the Tests

To run the tests, execute the `run_tests.py` script:

```
python run_tests.py
```

To run specific tests based on a pattern in their name:

```
python run_tests.py --select read
```

This command will run only the tests that contain the string "read" in their names.

## Decisions Taken

-   **Error Handling**: The framework is designed to handle exceptions gracefully. If a test function raises an exception, it is caught, and the test is marked as `ERROR`.
-   **Environment Cleanup**: The `teardown` function deletes any test files created during test execution, ensuring no residual files are left.
-   **Command Line Argument Parsing**: The `argparse` module is used to parse command-line arguments, making it easy to extend the framework with additional options in the future.

## Documentation

The test functions are designed to validate the behavior of corresponding functions in the `file_manager.py` module. For instance, `test_read_file_existing` checks if the `read_file` function correctly reads the content of an existing file.

## Conclusion

This testing framework provides a robust way to validate the functionality of the `file_manager.py` module, ensuring that file operations are executed correctly.
