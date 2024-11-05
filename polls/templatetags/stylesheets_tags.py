"""" This module is used to import style sheets dynamically """

from django import template
from .utils import get_static_paths

register = template.Library()

@register.inclusion_tag("polls/stylesheets.html")
def get_stylesheets(*args):
    """
    Receives a list with the name of the components to have their styles (.css) imported into the template

    Args:
        *args: Variable number of arguments representing the names of the CSS files.

    Returns:
        A dictionary containing the paths of the CSS stylesheets.

    Example:
        ```
        # importing
        {% load scripts_tags %}

        # 1 - using all
        {% get_stylesheets %}

        # 2 - using some
        {% get_stylesheets 'text' 'divider' %}
        ```
    """
    path = get_static_paths("polls", "polls/css", ".css", args)

    return { "path": path }
