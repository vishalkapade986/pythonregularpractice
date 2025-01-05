import os

# Function to print directory contents
def print_dir_contents(directory):
    try:
        # Get the list of files and directories
        contents = os.listdir(directory)
        
        print(f"Contents of the directory '{directory}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"Permission denied for accessing '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    print_dir_contents(directory)
