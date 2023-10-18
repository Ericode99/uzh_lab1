
import os
import time
import argparse

# Import the functions from file_manager
from file_manager import read_file, create_file, write_file, delete_file

# Constants for test results
PASS = "PASS"
FAIL = "FAIL"
ERROR = "ERROR"

def setup():
    with open("test_read_file.txt", "w") as f:
      f.write("Hello, World!")

    with open("test_write.txt", "w") as f:
      pass

    with open("test_delete_file.txt", "w") as f:
      f.write("File to delete.")

def teardown():
    test_files = ["test_read_file.txt", "test_create.txt", "test_write.txt", "test_delete_file.txt", "test_create_write_functionality.txt"]
    for fname in test_files:
        if os.path.exists(fname):
            os.remove(fname)


#-----------------------------------------------------------------------
#---------------- TESTS FOR THE read_file FUNCTION ---------------------
#-----------------------------------------------------------------------

def test_read_file_existing():
    # Test the read_file function with an existing file.
        content = read_file("test_read_file.txt")
        assert content == "Hello, World!", f"Expected 'Hello, World!' but got {content}"



def test_read_file_non_existing():
    # Test the read_file function with a non-existing file.
        content = read_file("non_existent_file.txt")
        assert content is None, f"Expected None but got {content}"

    

#-----------------------------------------------------------------------
#---------------- TESTS FOR THE create_file FUNCTION -------------------
#-----------------------------------------------------------------------

def test_create_file():
    # Test the create_file function.
        result = create_file("test_create.txt", "")
        assert result is True, f"Expected True but got {result}"
        assert os.path.exists("test_create.txt"), "File was not created"



def test_create_file_for_invalid_name():
    # Test the create_file function.
        result = create_file(".", "")
        assert result is False, f"Expected False but got {result}"



def test_create_file_w_functionality():
    # Test the create_file function.
        # Ensure the file exists and content is correct
        create_file("test_create_write_functionality.txt", "Testing create_file's write functionality")
        with open("test_create_write_functionality.txt", "r") as f:
            content = f.read()
        assert content == "Testing create_file's write functionality", f"Expected 'Testing create_file's write functionality' but got {content}"
        

    
#-----------------------------------------------------------------------
#--------------- TESTS FOR THE write_file FUNCTION ---------------------
#-----------------------------------------------------------------------

def test_write_file():
    # Test the write_file function.
        # Write new content to the file
        result = write_file("test_write.txt", "New content after write.")
        assert result == True, f"Expected True but got {result}"
        
        # Ensure the content is updated
        with open("test_write.txt", "r") as f:
            content = f.read()
        assert content == "New content after write.", f"Expected 'New content after write.' but got {content}"
        


def test_write_file_for_non_existent():
    # Test the write_file function.
        # Try to write content to impossible file
        result = write_file(".", "New content after write.")
        assert result == False, f"Expected False but got {result}"
        


#-----------------------------------------------------------------------
#---------------- TESTS FOR THE delete_file FUNCTION -------------------
#-----------------------------------------------------------------------

def test_delete_file():
    # Test the delete_file function.
        result = delete_file("test_delete_file.txt")
        assert result == True, f"Expected True but got {result}"

        # Ensure the file is deleted
        assert not os.path.exists("test_delete_file.txt"), "File was not deleted"
        


def test_delete_file_for_non_existent():
    # Test the delete_file function, for the case that the file does not exist
        result = delete_file("trying_to_delete_non_existent_file.txt")
        assert result == False, f"Expected False but got {result}"
        


#-----------------------------------------------------------------------
#---------------------- TEST FUNCTIONS EXECUTION -----------------------
#-----------------------------------------------------------------------

def run_selected_tests(select_pattern=None):
    test_functions = [func for name, func in globals().items() if name.startswith('test_')]
    
    if select_pattern:
        test_functions = [func for func in test_functions if select_pattern in func.__name__]

    for test_func in test_functions:
        setup()
        result = None
        start_time = time.time()
        try:
            test_func()   
            result = PASS
        except AssertionError as e:
            result = f"{FAIL}: {e}"
        except Exception as e:
            result = f"{ERROR}: {e}"

        end_time = time.time()
        total_time = end_time - start_time
        print(f"{test_func.__name__}: {result} (Executed in {total_time:.4f} seconds)")
        teardown()

#-----------------------------------------------------------------------
#---------------------- ADDING COMMAND LINE ARGUMENTS ------------------
#-----------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--select", type=str, help="Pattern to select which tests to run.")
    args = parser.parse_args()

    run_selected_tests(args.select)
