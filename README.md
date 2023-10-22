# Testing Framework for file_manager.py

This README provides an overview of the testing framework designed to test functions in the `file_manager.py` module.

## Features

1. **Three Test States**: Three states for a test were implemented by the framework: `PASS`, `FAIL` and `ERROR`.
2. **Introspection**: The program uses introspection to discover and execute test functions automatically. Only the functions with a `test_` prefix are considered for to be executed.
3. **Timing**: For each test, the result and its execution time is printed.
4. **Setup and Teardown**: The `setup` and `teardown` functions are called before and after each test, individually. This guarantees a clean environment for each test.
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

- **Error Handling**: The framework is designed to handle exceptions. If a test function raises an exception, it is caught, and the test is marked as `ERROR`.
- **Environment Cleanup**: The `teardown` function deletes any test files created during test execution, ensuring no residual files are left.
- **Command Line Argument Parsing**: The `argparse` module is used to parse command-line arguments.

## Documentation

The test functions are designed to validate the behavior of corresponding functions in the `file_manager.py` module.

- **test_read_file_existing**: Tests if the read_file function correctly reads an existing file and returns True.
- **test_read_file_non_existing**: Tests if the read_file function correcly returns False if promted to read a non existing file.
- **test_create_file**: Tests if the create_file function successfully creates an empty file and returns True.
- **test_create_file_for_invalid_name**: Tests if the create_file function correctly returns False if it fails to create the file.
- **test_create_file_w_functionality**: Tests if the create_file function successfully creates a file and writes content to it.
- **test_write_file**: Tests if the write_file function successfully writes content to an existing file and returns True.
- **test_write_file_for_non_existent**: Tests if the write_file function returns False if it fails to write to a file.
- **test_delete_file**: Tests if the delete_file function successfully deletes a file and returns True.
- **test_delete_file_for_non_existent**: Tests if the delete_file function correctly returns False if it fails to delete the file.

- **run_selected_tests**: Runs all tests by default or only certain tests if the command-line select option is applied. It works by creating a list of functions. If there is a pattern selected, it overwrites the function list and only the remaining functions, that have the selected pattern in their name are executed. Then the function list is passed into a for loop in which each test function is exexuted. Before each test execution the setup function is called and after each test execution the teardown function is called.
