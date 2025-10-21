import os

def write_file(working_directory, file_path, content):
    abspath = os.path.abspath(os.path.join(working_directory, file_path))
    working_abspath = os.path.abspath(working_directory)

    if abspath.startswith(working_abspath) == False:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if os.path.exists(abspath) == False:
        try:
            os.makedirs(os.path.dirname(abspath), exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"
    
    if os.path.exists(abspath) and os.path.isdir(abspath):
        return f'Error: "{file_path}" is a directory, not a file.'
    try:
        with open(abspath, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: writing to file: {e}"
