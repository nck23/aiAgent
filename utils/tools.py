import os


def setup_paths(working_directory, directory):
    project_boundaries = os.path.abspath(working_directory)
    joined_paths = os.path.join(project_boundaries, directory)
    target_path = os.path.abspath(joined_paths)
    return project_boundaries, target_path


def validate_scope(project_boundaries, target_path, directory):
    if not target_path.startswith(project_boundaries):
        return (f'Error: Cannot access "{directory}" as it is outside the permitted working directory')
    return None





    
    