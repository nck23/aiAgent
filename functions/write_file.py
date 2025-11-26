import os
from utils.tools import setup_paths, validate_scope

def write_file(working_directory, file_path, content):
    try:
        project_boundaries, target_path = setup_paths(working_directory, file_path)
        last_dir_path = os.path.dirname(target_path)
        scope_error  = validate_scope(project_boundaries, target_path, file_path)
        print(project_boundaries)
        print(target_path)
        if scope_error:
            return scope_error
        if not os.path.exists(last_dir_path):
            os.makedirs(last_dir_path)
        with open(target_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{target_path}" ({len(content)} characters written)'
    except Exception as e:
        print(f"ERROR: {e}")
