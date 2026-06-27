## 快速开始
通过新版内容模板定义通知内容的示例如下：
告警内容
{ "alert_id": "test-alert", "alert_name": "PV/UV Alert", "project": "project-1", "status": "firing", "severity": 6, "labels": { "app": "nginx", "host": "host-1" }, "results": [ { "project": "project-1", "logstore": "logstore-1", "query": "* | select count(*) as pv" }, { "project": "project-2", "logstore": "logstore-2", "query": "* | select count(distinct user_id) as uv" } ] }
内容模板配置
- Alert ID: {{ alert.alert_id }} - Alert Name: {{ alert.alert_name }} - Project: {{ alert.project }} - Status: {% if alert.status == "firing" %}FIRING{% else %}RESOLVED{% endif %} - Labels: {%- for key, val in alert.labels.items() %} - {{ key }}: {{ val }} {%- endfor %} - Query: {{ alert.results[0].query }}
输出结果
- Alert ID: test-alert - Alert Name: PV/UV Alert - Project: project-1 - Status: FIRING - Labels: - app: nginx - host: host-1 - Query: * | select count(*) as pv
