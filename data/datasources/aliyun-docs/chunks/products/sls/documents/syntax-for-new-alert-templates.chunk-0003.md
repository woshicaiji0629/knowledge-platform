### 分隔符

| 分隔符 | 使用场景 | 示例 |
| --- | --- | --- |
| {{ }} | 在变量或表达式中使用。 | 数字： {{ 123 }} 字符串： {{ "abc" }}或{{ 'xyz' }} 需要使用双引号（""）或单引号（''）。 变量： {{ alert.alert_name }} 表达式： {{ alert.project + '/' + alert.alert_id }} |
| {% %} | 用于控制语句。 | {% if alert.status == 'firing' %}FIRING{% else %}RESOLVED{% endif % } |
| {# #} | 用于注释，不会出现在通知内容中。 | {# this is a comment #} |
