from jinja2 import Template


html = """
{%- macro get_input(type='text', name='', placeholder='') -%}
    <input type="{{type}}" name="{{name}}"  placeholder="{{placeholder}}">
{%- endmacro -%}

<p>{{get_input(name='firstname', placeholder='Имя')}}</p>
<p>{{get_input(name='lastname', placeholder='Фамилия')}}</p>
<p>{{get_input(name='address', placeholder='Адрес')}}</p>
<p>{{get_input(type='tel', name='phone', placeholder='Телефон')}}</p>
<p>{{get_input(type='email', name='email', placeholder='Почта')}}</p>
"""

tm = Template(html)
msg = tm.render()

print(msg)
