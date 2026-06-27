### 分隔符解析
通过分隔符将日志内容结构化，解析为多个键值对形式，支持单字符分隔符和多字符分隔符。
效果示例：

| 未经任何处理的原始日志 | 按指定字符 , 切割字段 |
| --- | --- |
| 05/May/2025:13:30:28,10.10.*.*,"POST /PutData?Category=YunOsAccountOpLog&AccessKeyId=****************&Date=Fri%2C%2028%20Jun%202013%2006%3A53%3A30%20GMT&Topic=raw&Signature=******************************** HTTP/1.1",200,18204,aliyun-sdk-java | ip:10.10.*.* request:POST /PutData?Category=YunOsAccountOpLog&AccessKeyId=****************&Date=Fri%2C%2028%20Jun%202013%2006%3A53%3A30%20GMT&Topic=raw&Signature=******************************** HTTP/1.1 size:18204 status:200 time:05/May/2025:13:30:28 user_agent:aliyun-sdk-java |

配置步骤：在Logtail配置页面的处理配置区域，单击添加处理插件，选择原生处理插件>分隔符解析：
分隔符：指定用于切分日志内容的字符。
示例：对于CSV格式文件，选择自定义，输入半角逗号（,）。
引用符：当某个字段值中包含分隔符时，需要指定引用符包裹该字段，避免错误切割。
日志提取字段：按分隔顺序依次为每一列设置对应的字段名称（Key）。规则要求如下：
字段名只能包含：字母、数字、下划线（_）。
必须以字母或下划线（_）开头。
最大长度：128字节。
其他参数请参考[场景二：结构化日志](host-text-log-collection-auto-install.md)中的通用配置参数说明。
