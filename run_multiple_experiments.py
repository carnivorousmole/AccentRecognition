import subprocess

# List of input arguments
input_args = ['arg1', 'arg2', 'arg3']

# Path to the Python file to run
python_file = '/path/to/python/file.py'

# Name of the Conda environment
env_name = 'myenv'

# Iterate over the list of input arguments
for arg in input_args:
  # Run the Python file with the current input argument in the specified Conda environment
  subprocess.run(['conda', 'run', '-n', env_name, 'python', python_file, arg])




# File: main.py
# This code defines a main function that takes a single string argument and stores it in the global input_arg variable. The if __name__ == '__main__': block is used to ensure that the main function is called only when the Python file is run directly, not when it is imported by another module.

# To pass a command line argument to the Python file, you can use the sys.argv list. The sys.argv[1] element represents the first command line argument after the Python file name.

# You can then use the global input_arg variable in your code to access the value of the input argument.

# For example, to run the main.py file with the input argument 'hello', you can use the following command:
# Global variable to store the input argument
input_arg = None

def main(arg: str) -> None:
  global input_arg
  input_arg = arg

if __name__ == '__main__':
  import sys
  # Get the first command line argument as the input string
  main(sys.argv[1])
