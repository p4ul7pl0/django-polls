"""" This module is used to import style sheets dynamically """

from django import template
from .utils import get_static_paths

register = template.Library()

@register.inclusion_tag("polls/scripts.html")
def get_scripts(*args):
    """
    Receives a list with the name of the components to have their scripts (.js) imported into the template

    Args:
        *args: Variable number of arguments representing the names of the JavaScript files.

    Returns:
        A dictionary containing the paths of the JavaScript files.
        
    Example:
        ```
        # importing
        {% load scripts_tags %}

        # 1 - using all
        {% get_scripts %}

        # 2 - using some
        {% get_scripts 'input_password' 'transfer' %}
        ```
    """
    path = get_static_paths("polls", "polls/js", ".js", args)
    print('path: ', path)

    return { "path": path }
