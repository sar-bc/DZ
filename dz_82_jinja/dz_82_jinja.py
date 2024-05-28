from jinja2 import Template


menu = [
    {"url": "/index", "name": "Главная"},
    {"url": "/news", "name": "Новости"},
    {"url": "/about", "name": "О компании"},
    {"url": "/shop", "name": "Магазин"},
    {"url": "/contacts", "name": "Контакты"}
]

link = """
<ul>
    {% for m in menu -%}
        {% if m.name == "Главная" -%}
        <li><a href="{{m.url}}" class="active">{{m.name}}</a></li>
        {% else -%}
        <li><a href="{{m.url}}">{{m.name}}</a></li>
        {% endif -%}
        
    {%- endfor -%}
</ul>
"""

tm = Template(link)
msg = tm.render(menu=menu)

print(msg)
