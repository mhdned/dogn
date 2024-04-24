import os

from dotenv import dotenv_values

run_environment: str = os.environ.get("ENV")
current_directory = os.getcwd()
path_environment: str

if run_environment == "DEV":
    path_environment = os.path.join(current_directory, "configs\envs\.env.dev")
elif run_environment == "PROD":
    path_environment = os.path.join(current_directory, "configs\envs\.env.prod")
else:
    path_environment = os.path.join(current_directory, "configs\envs\.env")

config = dotenv_values(path_environment)
