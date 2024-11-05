from django.forms import Widget, TextInput
from django.template import loader
from django.utils.safestring import mark_safe

class CustomTextInput(Widget):
    name = 'Name Test'
    is_hidden = False
    is_required = False
    value = 'Value Test'
    template_name = "custom_text_input.html"

class CustomTextInput2(TextInput):
    icon = 'icon'
    def render(self, name, value, attrs=None, renderer=None):
        if self.icon:
            final_attrs = self.build_attrs(attrs)
            return f'\
            <div class="input-group">\
                <span class="input-group-addon">\
                    <img src="{self.icon}" />\
                </span>\
                {super().render(name, value, final_attrs)}\
            </div>'
        
        return super().render(name, value, attrs)

class PasswordInput(Widget):
    input_type = "text"
    template_name = "polls/components/molecules/input_password.html"

    def __init__(self, attrs=None, left_icon=None):
        super().__init__(attrs)
        self.left_icon = left_icon

    def get_context(self, name, value, attrs=None):
        # return super().get_context(name, value, attrs)
        return {
            'widget': {
                "name": name,
                "is_hidden": self.is_hidden,
                "required": self.is_required,
                "value": self.format_value(value),
                "attrs": self.build_attrs(self.attrs, attrs),
                "template_name": self.template_name,
            },
            'left_icon': self.left_icon,
        }

    # def render(self, name, value, attrs=None, renderer=None):
    #     context = self.get_context(name, value, attrs)
    #     template = loader.get_template(self.template_name).render(context)
    #     return mark_safe(template)