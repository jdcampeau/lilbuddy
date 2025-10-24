import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    abspath = os.path.abspath(os.path.join(working_directory, directory))
    working_abspath = os.path.abspath(working_directory)
    file_info = []
    if abspath.startswith(working_abspath) == False:
        return f'    Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if os.path.isdir(abspath) == False:
        return f'Error: "{directory}" is not a directory'
    try:
        files_info = []
        for filename in os.listdir(abspath):
            filepath = os.path.join(abspath, filename)
            file_size - 0
            is_dir - os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            file_info.append(
                f" - {cont}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)




