""" This file is used to add support for multi-line template tags. """

import re
from django.template import base as template_base

template_base.tag_re = re.compile(template_base.tag_re.pattern, re.DOTALL)