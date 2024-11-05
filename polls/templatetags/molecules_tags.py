""" This module contains the template tags for the molecules components"""

from django import template
from .utils import get_html_attrs_from_kwargs

register = template.Library()

@register.inclusion_tag("polls/components/molecules/divider.html")
def divider(title=None, **kwargs):
    """
    Renders a divider component with the specified type, title, and orientation.

    Parameters:
        type (str): The type of the divider. Default is "horizontal".
        title (str): The title of the divider. Default is "Title".
        orientation (str): The orientation of the divider. Default is "center".

    Returns:
        dict: A dictionary containing the type, title, and orientation of the divider.

    Example:
        ```
        # importing
        {% load molecules_tag %}

        # using
        {% divider 'Divider' orientation='center' type='horizontal' %}
        ```
    """

    k_type = kwargs.get('type', "horizontal")
    orientation = kwargs.get('orientation', "center")

    return { "type": k_type, "title": title, "orientation": orientation }

@register.inclusion_tag("polls/components/molecules/input_checkbox.html")
def input_checkbox(**kwargs):
    """
    Renders an input checkbox component with the specified properties.

    Args:
        label (str): The label text for the checkbox.
        checked (bool, optional): Specifies whether the checkbox is checked. Defaults to False.
        disabled (bool, optional): Specifies whether the checkbox is disabled. Defaults to False.
        indeterminate (bool, optional): Specifies whether the checkbox is in an indeterminate state. Defaults to False.

    Returns:
        dict: A dictionary containing the properties of the checkbox component.

    Example:
        ```
        # importing
        {% load molecules_tags %}

        # using
        {% input_checkbox label='Checkbox' checked=False disabled=False indeterminate=False %}
        {% input_checkbox label='Checkbox' checked=False disabled=True indeterminate=False %}
        {% input_checkbox label='Checkbox' checked=False disabled=False indeterminate=True %}
        {% input_checkbox label='Checkbox' checked=False disabled=True indeterminate=True %}
        
        {% input_checkbox label='Checkbox' checked=True disabled=False indeterminate=False %}
        {% input_checkbox label='Checkbox' checked=True disabled=True indeterminate=False %}
        {% input_checkbox label='Checkbox' checked=True disabled=False indeterminate=True %}
        {% input_checkbox label='Checkbox' checked=True disabled=True indeterminate=True %}

        {% input_checkbox %}
        ```
    """

    label = kwargs.get('label')
    checked = kwargs.get('checked', False)
    disabled = kwargs.get('disabled', False)
    indeterminate = kwargs.get('indeterminate', False)

    return { "label": label, "checked": checked, "disabled": disabled, "indeterminate": indeterminate}

@register.inclusion_tag("polls/components/molecules/breadcrumb.html")
def breadcrumb(item1="Home", item2="Overview", **kwargs):
    """
    Renders a breadcrumb component with item1 and item2 menu.

    Parameters:
        item1 (str): The first item of the breadcrumb. Default is "Home".
        item2 (str): The second item of the breadcrumb. Default is "Overview".
        type (str): The type of the breadcrumb. Default is "2".
        item3 (str): The third item of the breadcrumb. Default is "Info".        

    Returns:
        dict: A dictionary containing the crumb and crumb menu of the breadcrumb.

    Example:
        ```
        # importing
        {% load molecules_tags %}

        # using
        {% breadcrumbs item1="Home" item2="General" type="2" %}
        {% breadcrumbs item1="Home" item2="General" type="3" item3="Info" %}

        ```
    """
    k_type = kwargs.get('type', "2")
    item3 = kwargs.get('item3', "Info")

    return { "item1": item1, "item2": item2 , "type": k_type, "item3": item3 }

@register.inclusion_tag("polls/components/molecules/dropdown.html")
def dropdown(title=None, **kwargs):
    """
    Renders a dropdown component with the specified properties.

    Parameters:
        title (str): The title of the dropdown. Default is "Title".
        type (str): The type of the dropdown. Default is "default".
        items (list): The items of the dropdown. Items type: [{"label": "Item 1","active": True}, {"label": "Item 1"}, {"label": "Item 1", "disabled": True}].

    Returns:
            dict: A dictionary containing the properties of the dropdown component.

    Example:
        ```
        # importing
        {% load molecules_tags %}

        # using
        {% dropdown title="English" type="secondary" items=items %}
        {% dropdown title="English" type="primary" items=items %}
        {% dropdown title="English" type="borderless" items=items %}
        {% dropdown title="English" type="icon" items=items %}
        ```

    """
    k_type = kwargs.get('type', "secondary")
    items = kwargs.get('items', None)

    return { "title": title, "type": k_type, "items": items }

@register.inclusion_tag('polls/components/molecules/input_text.html')
def input_text(**kwargs):
    """
    Renders an input text component with the specified attributes.

    Args:
        placeholder (str, optional): The placeholder text to display in the input field. Defaults to "Placeholder".
        left_icon (str, optional): The classes of the left icon to display (Bootstrap icon classes). Defaults to None.
        value (str, optional): The initial value of the input field. Defaults to None.
        disabled (bool, optional): Whether the input field should be disabled.  Defaults to False.
        error (bool, optional): Whether the input field should display an error state. Defaults to False.

    Returns:
        dict: A dictionary containing the attributes to be passed to the template.

    Example:
        ```
        # importing
        {% load molecules_tags %}

        # using
        {% input_text placeholder="Enter your text ..." value="Some text" left_icon="bi bi-person" disabled=True %}
        ```
    """
    placeholder = kwargs.get('placeholder', 'Placeholder')
    left_icon = kwargs.get('left_icon', None)
    value = kwargs.get('value', None)
    disabled = kwargs.get('disabled', False)
    error = kwargs.get('error', False)

    return { 
        'placeholder': placeholder, 
        'left_icon': left_icon, 
        'value': value, 
        'disabled': disabled,
        'error': error
    }

@register.inclusion_tag('polls/components/molecules/base_input.html')
def base_input(*args, **kwargs):
    """
    Renders a base input component with the specified attributes.

    Args:
        k_type (str, optional): The type of the input field. Defaults to "text".
        placeholder (str, optional): The placeholder text for the input field. Defaults to "Placeholder".
        left_icon (str, optional): The classes of the left icon. Defaults to None (Bootstrap icon classes).
        right_icon (str, optional): The classes of the right icon. Defaults to None (Bootstrap icon classes).
        value (str, optional): The initial value of the input field. Defaults to None.
        disabled (bool, optional): Whether the input field is disabled. Defaults to False.
        error (bool, optional): Whether the input field has an error. Defaults to False.

    Returns:
        dict: A dictionary containing the input field properties.

    Example:
        ```
        # importing
        {% load molecules_tags %}

        # using
        {% base_input 
            html_attrs|safeseq|join:" " 
            type="number" 
            placeholder=placeholder 
            left_icon=left_icon
            value=value 
            disabled=disabled 
            error=error 
        %}
        ```
    """
    placeholder = kwargs.get('placeholder', 'Placeholder')
    left_icon = kwargs.get('left_icon', None)
    right_icon = kwargs.get('right_icon', None)
    on_right_icon_click = kwargs.get('on_right_icon_click', None)
    value = kwargs.get('value', None)
    disabled = kwargs.get('disabled', False)
    error = kwargs.get('error', False)
    k_type = kwargs.get('type', 'text')
    widget = kwargs.get('widget', None)

    return { 
        'placeholder': placeholder,     
        'left_icon': left_icon, 
        'right_icon': right_icon, 
        'on_right_icon_click': on_right_icon_click, 
        'value': value, 
        'disabled': disabled, 
        'error': error, 
        'type':  k_type,
        'html_attrs': args,
        'widget': widget
    }

@register.inclusion_tag('polls/components/molecules/input_password.html')
def input_password(**kwargs):
    """
    Renders an input field for a password with optional attributes.

    Args:
        placeholder (str, optional): The placeholder text for the input field. Default is 'Placeholder'.
        left_icon (str, optional): The classes of the left icon to display. Default is None (Bootstrap icon classes).
        value (str, optional): The initial value of the input field. Default is None.
        disabled (bool, optional): Whether the input field is disabled. Default is False.
        error (bool, optional): Whether the input field has an error. Default is False.

    Returns:
        dict: A dictionary containing the attributes to be rendered in the template.

    Example:
        ```
        # importing
        {% load molecules_tags %}

        # using
        {% input_password placeholder="Enter your text ..." left_icon='bi bi-lock' error=True %}
        {% input_password placeholder="Enter your text ..." %}
        {% input_password placeholder="Enter your text ..." left_icon="bi bi-lock" %}
        {% input_password placeholder="Enter your text ..." value="Some text" left_icon="bi bi-lock" %}
        {% input_password placeholder="Enter your text ..." value="Some text" left_icon="bi bi-lock" disabled=True %}
        {% input_password placeholder="Enter your text ..." left_icon="bi bi-lock" disabled=True %}
        ```
    """

    placeholder = kwargs.get('placeholder', 'Placeholder')
    left_icon = kwargs.get('left_icon', None)
    value = kwargs.get('value', None)
    disabled = kwargs.get('disabled', False)
    error = kwargs.get('error', False)

    return { 
        'placeholder': placeholder, 
        'left_icon': left_icon, 
        'value': value, 
        'disabled': disabled,
        'error': error, 
    }

@register.inclusion_tag('polls/components/molecules/input_number.html')
def input_number(**kwargs):
    """
    Renders an input number component with the specified attributes.

    Args:
        **kwargs: Keyword arguments for configuring the input number component.
            - placeholder (str, optional): The placeholder text for the input. Default is 'Placeholder'.
            - left_icon (str, optional): The classes of the left icon to display. Default is None (Bootstrap icon classes).
            - value (str, optional): The initial value of the input. Default is None.
            - disabled (bool, optional): Whether the input is disabled or not. Default is None.
            - error (bool, optional): Whether the input has an error or not. Default is None.

    Returns:
        dict: A dictionary containing the attributes to render the input number component.
            - placeholder (str): The placeholder text for the input.
            - left_icon (str): The name of the left icon to display.
            - value (str): The initial value of the input.
            - disabled (bool): Whether the input is disabled or not.
            - error (bool): Whether the input has an error or not.
            - html_attrs (list): A list of HTML attributes to apply to the input.

    Example:
        ```
        # importing
        {% load molecules_tags %}

        # using
        {% input_number min="2" max="10" step="2" placeholder="Enter a number" %}
        {% input_number min="2" max="10" step="2" value="2" placeholder="Enter a number" disabled=True %}
        {% input_number min="2" max="10" step="2" value="2" placeholder="Enter a number" error=True %}
        {% input_number min="2" max="10" step="2" value="2" placeholder="Enter a number" %}
        {% input_number min="2" max="10" step="2" placeholder="Enter a number" disabled=True %}
        ```
    """

    placeholder = kwargs.get('placeholder', 'Placeholder')
    left_icon = kwargs.get('left_icon', None)
    value = kwargs.get('value', None)
    disabled = kwargs.get('disabled', False)
    error = kwargs.get('error', False)


    return {
        'placeholder': placeholder, 
        'left_icon': left_icon, 
        'value': value, 
        'disabled': disabled,
        'error': error, 
        'html_attrs': get_html_attrs_from_kwargs(kwargs)
    }

@register.inclusion_tag("polls/components/molecules/input_search.html")
def input_search(**kwargs):
    """
    Renders an input search component with the specified attributes.

    Args:
        **kwargs: Keyword arguments to customize the input search component.
            - placeholder (str, optional): The placeholder text for the input field. Defaults to 'Placeholder'.
            - left_icon (str, optional): The classes of the left icon to display. Default is None (Bootstrap icon classes).
            - value (str, optional): The initial value of the input field. Defaults to None.
            - error (bool, optional): Indicates if the input field has an error. Defaults to False.
            - disabled (bool, optional): Indicates if the input field is disabled. Defaults to False.

    Returns:
        dict: A dictionary containing the attributes and values to render the input search component.
            - html_attrs (dict): The HTML attributes generated from the keyword arguments.
            - error (bool): Indicates if the input field has an error.
            - placeholder (str): The placeholder text for the input field.
            - value (str): The initial value of the input field.
            - disabled (bool): Indicates if the input field is disabled.
            - left_icon (str): The name of the left icon to display.
    Examples:
        ```
        # importing
        {% load molecules_tags %}

        # using
        {% input_search placeholder="Search by ..." value="test" error=True %}<br>
        {% input_search placeholder="Search by ..." value="test" disabled=True %}<br>
        {% input_search placeholder="Search by ..." disabled=True %}<br>
        {% input_search disabled=True %}<br>
        {% input_search left_icon="bi bi-person" %}<br>
        ```
    """

    placeholder = kwargs.get('placeholder', 'Placeholder')
    left_icon = kwargs.get('left_icon', None)
    value = kwargs.get('value', None)
    error = kwargs.get('error', False)
    disabled = kwargs.get('disabled', False)

    return { 
        "html_attrs": get_html_attrs_from_kwargs(kwargs),
        "error": error,
        "placeholder": placeholder,
        "value": value,
        "disabled": disabled,
        "left_icon": left_icon
    }
