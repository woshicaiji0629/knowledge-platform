### 转义
如果您希望特殊字符串（例如{{）不被内容模板解析和渲染，可对特殊字符串进行转义。例如：根据如下配置表示保留{% raw %}和{% endraw %}之间所有的内容。
内容模板配置
{% raw %} {% for result in alert.results %} {{ result }} {% endfor %} {% endraw %}
结果
{% for result in alert.results %} {{ result }} {% endfor %}
