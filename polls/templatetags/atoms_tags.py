""" This module contains the template tags for the atoms components"""

from django import template

register = template.Library()

@register.inclusion_tag("gui/components/atoms/text.html")
def text(k_text="Text", **kwargs):
    """
    Renders a text component with the specified size, text, and style.

    Args:
        size (str): The size of the text component. Defaults to "1".
        k_text (str): The text to be displayed. Defaults to "Text".
        style (str): The style of the text component. Defaults to "default".

    Returns:
        dict: A dictionary containing the size, style, and text to be passed to the template.
    
    Example:
        ```
        # importing
        {% load atoms_tags %}

        # using
        {% text 'Some text' type='Default' size='1' %}
        ```
    """

    size = kwargs.get('size', "1")
    style = kwargs.get('style', "default")

    return { "size": size, "text": k_text, "style": style }

@register.inclusion_tag("gui/components/atoms/title.html")
def title(k_title="Title", **kwargs):
    """
    Renders a title component with the specified size, text, and style.

    Parameters:
        size (str): The size of the title. Default is "1".
        k_title (str): The text to be displayed in the title. Default is "Title".
        style (str): The style of the title. Default is "default".

    Returns:
        dict: A dictionary containing the size, style, and text to be used in the template.

        Example:
        ```
        # importing
        {% load atoms_tags %}

        # using
        {% title 'Some title' type='default' size='2' %}
    """

    size = kwargs.get('size', "1")
    style = kwargs.get('style', "default")

    return { "size": size, "title": k_title, "style": style }
