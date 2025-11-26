import os
from google.genai import types

def setup_paths(working_directory, directory):
        project_boundaries = os.path.abspath(working_directory)
        joined_paths = os.path.join(project_boundaries, directory)
        target_path = os.path.abspath(joined_paths)
        return project_boundaries, target_path

def validate_scope(project_boundaries, target_path, directory):
    if not target_path.startswith(project_boundaries):
            return (f'Error: Cannot access "{directory}" as it is outside the permitted working directory')
    return None

def setup_available_funcs():
        schema_get_files_info = types.FunctionDeclaration(
        name="get_files_info",
        description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
        parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                "working_directory": types.Schema(
                        type=types.Type.STRING,
                        description="The directory where you are.",
                        ),
                "directory": types.Schema(
                        type=types.Type.STRING,
                        description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),      
                },
        ),
        )

        schema_get_file_content = types.FunctionDeclaration(
        name="get_file_content",
        description="Reads file content upto 10k chars and returns as a string.",
        parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                "working_directory": types.Schema(
                        type=types.Type.STRING,
                        description="The directory where you are.",
                ),
                "file_path": types.Schema(
                        type=types.Type.STRING,
                        description="Path to the file you want list content from.",
                ),
                },
        ),
        )

        schema_run_python_file = types.FunctionDeclaration(
        name="run_python_file",
        description="Executes python file and returns an output",
        parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                "working_directory": types.Schema(
                        type=types.Type.STRING,
                        description="The directory where you are.",
                ),
                "file_path": types.Schema(
                        type=types.Type.STRING,
                        description="Path to the file you want to execute.",
                ),
                "args": types.Schema(
                        type=types.Type.STRING,
                        description="Additional arguments to pass if necessary.",
                ),
                },
        ),
        )

        schema_write_file = types.FunctionDeclaration(
        name="write_file",
        description="Creates file with content or overwrites when exists, path is created if it doesn't exist",
        parameters=types.Schema(
                type=types.Type.OBJECT,
                properties={
                "working_directory": types.Schema(
                        type=types.Type.STRING,
                        description="The directory where you are.",
                ),
                "file_path": types.Schema(
                        type=types.Type.STRING,
                        description="Path to the file you want to create.",
                ),
                "content": types.Schema(
                        type=types.Type.STRING,
                        description="Content to fill file with.",
                ),
                },
        ),
        )

        available_functions = types.Tool(
        function_declarations=[
                schema_get_files_info,
                schema_get_file_content,
                schema_run_python_file,
                schema_write_file
        ]
        )
        return available_functions