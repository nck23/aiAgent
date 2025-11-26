import os
import subprocess

from utils.tools import setup_paths, validate_scope


def run_python_file(working_directory, file_path, args=[]):
    try:
        project_boundaries, target_path = setup_paths(working_directory, file_path)
        scope_error  = validate_scope(project_boundaries, target_path, file_path)
        if scope_error:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(target_path):
            return f'Error: File "{file_path}" not found.'
        file_extension = file_path.split('.')[1]
        if file_extension != 'py':
            return f'Error: "{file_path}" is not a Python file.'
        result = subprocess.run(
            ["python3", target_path] + args,
            capture_output=True,
            text=True,
            timeout=30
        )
        output = f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        process_status_code = result.returncode
        if process_status_code!= 0:
            output += f"\nProcess exited with code {process_status_code}"
        return output
    except Exception as e:
        print(f"Error: executing Python file: {e}")