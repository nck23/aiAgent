# functions/get_files_info.py

import os
from utils.tools import setup_paths, validate_scope

def get_files_info(working_directory, directory="."):
    try:
        project_boundaries, target_path = setup_paths(working_directory, directory)
        scope_error  = validate_scope(project_boundaries, target_path, directory)
        if scope_error:
            return scope_error 

        files_inside = os.listdir(target_path)
        result = {
            "directory": directory,
            "files": []
        }
        for file in files_inside:
            full_path = os.path.join(target_path, file)
            is_dir = os.path.isdir(full_path)
            file_size = os.path.getsize(full_path)
            file_info = {
                "name": file,
                "file_size": file_size,
                "is_dir": is_dir
            }
            result["files"].append(file_info)
        output = pretty_print(result)
        return output
    except Exception as e:
        return f"ERROR: {e}"
        


def pretty_print(file_dictionary):
    output = ""
    for file in file_dictionary['files']:
        output += f" - {file['name']}: file_size={file['file_size']} bytes, is_dir={file['is_dir']}\n"
    return output
    

    
