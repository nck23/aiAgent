# functions/get_file_content.py
import os
from utils.tools import setup_paths, validate_scope

def get_file_content(working_directory, file_path):
    MAX_CHARS = 10000
    try:
        project_boundaries, target_path = setup_paths(working_directory, file_path)
        scope_error  = validate_scope(project_boundaries, target_path, file_path)
        if scope_error:
            return scope_error 

        is_file = os.path.isfile(target_path)
        if is_file:
            with open(target_path, "r") as f:
                file_content = f.read(MAX_CHARS)
                return file_content
        else:
            return f'Error: File not found or is not a regular file: "{file_path}"'
    except Exception as e:
        return f"ERROR: {e}"