import os
from google.genai import types
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abspath = os.path.abspath(os.path.join(working_directory, file_path))
    working_abspath = os.path.abspath(working_directory)

    if abspath.startswith(working_abspath) == False:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if os.path.isfile(abspath) == False:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(abspath, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if os.path.getsize(abspath) > MAX_CHARS:
                file_content_string += (
                        f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                    )
        return file_content_string
    except Exception as e:
        return f'Error reading file {file_path}"'

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns the contents of a specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path is the file to read from, relative to the working directory. If not provided, return the error given in in the function itself.",
            ),
        },
    ),
)


