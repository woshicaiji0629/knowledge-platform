### IIS日志解析
根据IIS日志格式定义将日志内容结构化，解析为多个键值对形式。
对比示例：

| 原始日志 | 微软 IIS 服务器专用格式适配 |
| --- | --- |
| #Fields: date time s-sitename s-ip cs-method cs-uri-stem cs-uri-query s-port cs-username c-ip cs(User-Agent) sc-status sc-substatus sc-win32-status sc-bytes cs-bytes time-taken | c-ip: cs-username cs-bytes: sc-substatus cs-method: cs-method cs-uri-query: cs-uri-query cs-uri-stem: cs-uri-stem cs-username: s-port date: #Fields: s-computername: s-sitename s-ip: s-ip s-sitename: time sc-bytes: sc-status sc-status: c-ip sc-win32-status: cs (User-Agent) time: date time-taken: sc-win32-status |

配置步骤：在Logtail配置页面的处理配置区域，单击添加处理插件，选择原生处理插件>IIS模式解析：
日志格式：选择您的IIS服务器日志采用的日志格式。
IIS：Microsoft IIS日志文件格式。
NCSA：NCSA公用日志文件格式。
W3C：W3C扩展日志文件格式。
IIS配置字段：选择IIS或NCSA时，日志服务已默认设置了IIS配置字段，选择W3C时，设置为您的IIS配置文件中logExtFileFlags参数中的内容。例如：
logExtFileFlags="Date, Time, ClientIP, UserName, SiteName, ComputerName, ServerIP, Method, UriStem, UriQuery, HttpStatus, Win32Status, BytesSent, BytesRecv, TimeTaken, ServerPort, UserAgent, Cookie, Referer, ProtocolVersion, Host, HttpSubStatus"
其他参数请参考[场景二：结构化日志](one-time-collection-of-host-text-logs.md)中的通用配置参数说明。
