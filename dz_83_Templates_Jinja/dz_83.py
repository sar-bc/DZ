from jinja2 import Template


html = """
{% macro get_input(type='text', name='', placeholder='') %}
    <input type="{{type}}" name="{{name}}"  placeholder="{{placeholder}}">
{% endmacro %}

<p>{{get_input('username')}}</p>
"""

tm = Template(html)
msg = tm.render()

print(msg)
