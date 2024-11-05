""" This module contains utility functions to be used in building templatetags """

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

print('BASE_DIR: ', BASE_DIR)

def get_static_paths(app_name="gui", folder_name="css", file_extension=".css", components=None):
    """
    Retrieve the paths of static files with a specific file extension in a given folder.
    It also receives a tuple with the name of the components to be filtered, the empty component 
    list indicates that all components must be taken into account

    Args:
        app_name (str): The name of the Django app. Defaults to "gui".
        folder_name (str): The name of the folder within the app's static directory. Defaults to "css".
        file_extension (str): The file extension to filter the static files. Defaults to ".css".
        components (list): A list of specific components to include. If None, include all components. Defaults to None.

    Returns:
        list: A list of paths to the static files.

    Raises:
        FileNotFoundError: If the static folder or any of its subfolders does not exist.
    """
    
    try:
        absolute_static_path = os.path.join(BASE_DIR, f"{app_name}/static/")
        absolute_folder_path = absolute_static_path + folder_name
        print('absolute_static_path: ', absolute_static_path)
        print('absolute_folder_path: ', absolute_folder_path)
        stylesheets_href = []

        for root, _, files in os.walk(absolute_folder_path):
            print('files: ', files)
            for absolute_filename in files:
                if absolute_filename.endswith(file_extension):
                    base_href = root.replace(absolute_static_path, '')
                    href = os.path.join(base_href, absolute_filename)
                    print('absolute_filename: ', absolute_filename)
                    filename = absolute_filename.replace(file_extension, '')

                    if not components or filename in components:
                        stylesheets_href.append(href)

        return stylesheets_href
        
    except FileNotFoundError:
        return []

def get_html_attrs_from_kwargs(kwargs, exception_list=None):
    """
    Returns a list of HTML attribute strings generated from the given keyword arguments.

    Args:
        kwargs (dict): The keyword arguments to generate HTML attributes from.
        exception_list (list, optional): A list of attribute names to exclude from the generated HTML attributes. Defaults to ['placeholder', 'value', 'error', 'disabled'].

    Returns:
        list: A list of HTML attribute strings.

    """
    if exception_list is None:
        exception_list = ['placeholder', 'value', 'error', 'disabled']
        
    html_attrs = []

    for key, value in kwargs.items():
        if key not in exception_list:
            if isinstance(value, bool) and value:
                html_attrs.append(key)
            elif isinstance(value, str):
                html_attrs.append(f'{key}="{value}"')
    
    return html_attrs