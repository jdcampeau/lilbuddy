import os
from config import *

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    abspath = os.path.abspath(full_path)
    working_abspath = os.path.abspath(working_directory)

    if abspath.startswith(working_abspath) == False:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if os.path.isfile(abspath) == False:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    with open(abspath, "r") as f:
        file_content_string = f.read(MAX_CHARS)

    return file_content_string
