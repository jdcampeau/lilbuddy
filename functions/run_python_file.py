import os
import subprocess
from pathlib import Path

def run_python_file(working_directory, file_path, args=[]):
    abspath = os.path.abspath(os.path.join(working_directory, file_path))
    working_abspath = os.path.abspath(working_directory)

    if abspath.startswith(working_abspath) == False:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if os.path.exists(abspath) == False:
        return f'Error: File "{file_path}" not found.'

    if abspath.endswith(".py") == False:
        return f'Error: "{file_path}" is not a Python file.'

    argslist = ["python", abspath]

    if len(args) >= 1:
        for arg in args:
            argslist.append(arg)

    try:
        result = subprocess.run(
                argslist,
                cwd = working_directory,
                capture_output=True, 
                text=True, 
                timeout=30
        )
        out = result.stdout or ""
        err = result.stderr or ""
        parts = []
        if out:
            parts.append(f"STDOUT:{out}")
        if err:
            parts.append(f"STDERR:{err}")
        if result.returncode != 0:
            parts.append(f"Process exited with code {completed.returncode}")
        return "\n".join(parts) if parts else "no output produced."
    
    except Exception as e:
        return f"Error: executing Python file: {e}"
