### 标准JSON解析
将Object类型的JSON日志结构化，解析为键值对形式。
效果示例：

| 未经任何处理的原始日志 | 标准 JSON 键值自动提取 |
| --- | --- |
| {"url": "POST /PutData?Category=YunOsAccountOpLog&AccessKeyId=U0Ujpek********&Date=Fri%2C%2028%20Jun%202013%2006%3A53%3A30%20GMT&Topic=raw&Signature=pD12XYLmGxKQ%2Bmkd6x7hAgQ7b1c%3D HTTP/1.1", "ip": "10.200.98.220", "user-agent": "aliyun-sdk-java", "request": {"status": "200", "latency": "18204"}, "time": "05/Jan/2025:13:30:28"} | ip: 10.200.98.220 request: {"status": "200", "latency" : "18204" } time: 05/Jan/2025:13:30:28 url: POST /PutData?Category=YunOsAccountOpLog&AccessKeyId=U0Ujpek******&Date=Fri%2C%2028%20Jun%202013%2006%3A53%3A30%20GMT&Topic=raw&Signature=pD12XYLmGxKQ%2Bmkd6x7hAgQ7b1c%3D HTTP/1.1 user-agent:aliyun-sdk-java |

配置步骤：在Logtail配置页面的处理配置区域，单击添加处理插件，选择原生处理插件>JSON解析：
原始字段：默认值为content（此字段用于存放待解析的原始日志内容）。
其他参数请参考[场景二：结构化日志](host-text-log-collection-auto-install.md)中的通用配置参数说明。
