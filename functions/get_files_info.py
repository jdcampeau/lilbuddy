import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    abspath = os.path.abspath(full_path)
    working_abspath = os.path.abspath(working_directory)
    file_info = []
    if directory == ".":
        file_info.append("Results for current directory:")
    else:
        file_info.append(f"Results for '{directory}' directory:")
    if abspath.startswith(working_abspath) == False:
        file_info.append(f'    Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return "\n".join(file_info)
    if os.path.isdir(abspath) == False:
        file_info.append(f'    Error: "{directory}" is not a directory')
        return "\n".join(file_info)
    dir_contents = os.listdir(abspath)
    for cont in dir_contents:
        cont_path = os.path.join(abspath, cont)
        file_size = os.path.getsize(cont_path)
        is_dir = os.path.isdir(cont_path)
        file_info.append(f" - {cont}: file_size={file_size} bytes, is_dir={is_dir}")
    formatted_info = "\n".join(file_info)
    return formatted_info




