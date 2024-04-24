import os

# Get all environment variables
# env_vars = os.environ

# # Print all environment variables
# for var in env_vars:
#     print(f"{var}: {env_vars[var]}")

# Get the value of the PYTHONPATH variable
pythonpath = os.getenv("PYTHONPATH")

# Check if PYTHONPATH is set and print its value
if pythonpath:
    print(f"PYTHONPATH: {pythonpath}")
else:
    print("PYTHONPATH is not set.")
