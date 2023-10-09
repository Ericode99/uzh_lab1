
import os
import time

# Import the functions from file_manager
from file_manager import read_file, create_file, write_file, delete_file

# Constants for test results
PASS = "PASS"
FAIL = "FAIL"
ERROR = "ERROR"

def setup():
    with open("test_file.txt", "w") as f:
      f.write("Hello, World!")
    create_file("test_create.txt", "Testing create_file function.")

def teardown():
    test_files = ["test_file.txt", "test_create.txt", "test_write.txt"]
    for fname in test_files:
        if os.path.exists(fname):
            os.remove(fname)

# Test functions...

def test_read_file_existing():
    """Test the read_file function with an existing file."""
    setup()
    try:
        content = read_file("test_file.txt")
        assert content == "Hello, World!", f"Expected 'Hello, World!' but got {content}"
        return PASS
    except AssertionError as e:
        return f"{FAIL}: {e}"
    except Exception as e:
        return f"{ERROR}: {e}"
    finally:
        teardown()


def test_read_file_non_existing():
    """Test the read_file function with a non-existing file."""
    setup()
    try:
        content = read_file("non_existent_file.txt")
        assert content is None, f"Expected None but got {content}"
        return PASS
    except AssertionError as e:
        return f"{FAIL}: {e}"
    except Exception as e:
        return f"{ERROR}: {e}"
    finally:
        teardown()


def test_create_file():
    """Test the create_file function."""
    setup()
    try:
        # Ensure the file exists and content is correct
        with open("test_create.txt", "r") as f:
            content = f.read()
        assert content == "Testing create_file function.", f"Expected 'Testing create_file function.' but got {content}"
        
        return PASS
    except AssertionError as e:
        return f"{FAIL}: {e}"
    except Exception as e:
        return f"{ERROR}: {e}"
    finally:
        teardown()


def test_write_file():
    """Test the write_file function."""
    setup()
    try:
        # Create an initial file
        with open("test_write.txt", "w") as f:
            f.write("Initial content.")
        
        # Write new content to the file
        result = write_file("test_write.txt", "New content after write.")
        assert result == True, "Expected True but got False"
        
        # Ensure the content is updated
        with open("test_write.txt", "r") as f:
            content = f.read()
        assert content == "New content after write.", f"Expected 'New content after write.' but got {content}"
        
        return PASS
    except AssertionError as e:
        return f"{FAIL}: {e}"
    except Exception as e:
        return f"{ERROR}: {e}"
    finally:
        teardown()


def test_delete_file():
    """Test the delete_file function."""
    setup()
    try:
        # Create a file to delete
        with open("test_file.txt", "w") as f:
            f.write("Content to be deleted.")
        
        result = delete_file("test_file.txt")
        assert result == True, "Expected True but got False"
        
        # Ensure the file is deleted
        assert not os.path.exists("test_file.txt"), "File was not deleted"
        
        return PASS
    except AssertionError as e:
        return f"{FAIL}: {e}"
    except Exception as e:
        return f"{ERROR}: {e}"
    finally:
        teardown()


# Function to run the tests
def run_selected_tests(select_pattern=None):
    test_results = []
    test_functions = [func for name, func in globals().items() if name.startswith('test_')]
    
    if select_pattern:
        test_functions = [func for func in test_functions if select_pattern in func.__name__]

    for test_func in test_functions:
        start_time = time.time()
        result = test_func()
        end_time = time.time()
        elapsed_time = end_time - start_time
        test_results.append((test_func.__name__, result, elapsed_time))
        print(f"{test_func.__name__}: {result} (Executed in {elapsed_time:.4f} seconds)")

    return test_results

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run tests for file_manager functions.")
    parser.add_argument("--select", type=str, help="Pattern to select which tests to run.")
    args = parser.parse_args()

    run_selected_tests(args.select)
