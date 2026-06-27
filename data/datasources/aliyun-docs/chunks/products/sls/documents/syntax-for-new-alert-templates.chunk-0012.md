## 配置示例
示例1：根据告警状态展示不同内容
触发告警后，展示告警状态、告警严重度和触发结果等信息；告警恢复时，只展示告警状态。
不使用函数
{% if alert.status == "firing" %} - 状态: <font color="#E03C39">触发</font> - 严重度：{{ alert.severity | format_severity }} - Results: {{ alert.results | to_json }} {% else %} - 状态: <font color="#72C140">恢复</font> {% endif %}
使用函数
使用format_status函数和format_severity函数简化配置。
- 状态: {{ alert.status | format_status }} {% if alert.status == "firing" %} - 严重度：{{ alert.severity | format_severity }} - Results: {{ alert.results | to_json }} {% endif %}
结构化数据展示
将告警标签的内容转换为列表形式，内容为Markdown格式。
不使用函数
- 项目: {{ alert.project }} - 告警名称: {{ alert.alert_name }} - 告警标签: {%- for key, val in alert.labels.items() %} > - {{ key }}: {{ val }} {%- endfor %}
使用函数
使用to_list函数和blockquote函数简化配置。
- 项目: {{ alert.project }} - 告警名称: {{ alert.alert_name }} - 告警标签: {{ alert.labels | to_list | blockquote }}
该文章对您有帮助吗？
反馈
