## 常见问题
- 什么是SSRF攻击？仅加固模式防御SSRF攻击原理是什么？
SSRF（Server-Side Request Forgery，服务端请求伪造）是一种安全漏洞，攻击者通过诱导服务器发起任意网络请求，从而访问受保护的内部系统（如元数据服务、数据库等）。例如，攻击者提交包含http://100.100.100.200/latest/meta-data/的URL，诱使应用抓取并返回元数据中的敏感信息，造成元数据泄露。
默认情况下，ECS实例支持无令牌访问元数据（普通模式）。开启仅加固模式后，会强制启用令牌验证机制：客户端必须先发送PUT请求获取临时令牌，并在后续GET请求中携带该令牌。由于SSRF攻击难以发起PUT请求，无法获取令牌，从而有效阻断访问，提升元数据安全。
- 加固模式下，使用命令无法访问实例元数据，如何处理？
常见错误命令如下：
实例元数据访问凭证的有效期超出范围（400 - Missing or Invalid Parameters）
实例元数据访问凭证有效期范围为1秒~21600秒，超过这个限制，会报错400 - Missing or Invalid Parameters。
curl -X PUT "http://100.100.100.200/latest/api/token" -H "X-aliyun-ecs-metadata-token-ttl-seconds: 21700"
请求中存在X-Forwarded-For标头（403 - Forbidden）
curl -X PUT "http://100.100.100.200/latest/api/token" -H "X-Forwarded-For: www.ba****.com"
指定的实例元数据访问凭证无效（401 - Unauthorized）
curl -H "X-aliyun-ecs-metadata-token: aaa" -v http://100.100.100.200/latest/meta-data/
- 高频访问元数据服务被限流怎么办？
元数据服务存在访问频率限制。最佳实践是在应用启动时获取一次基本不变的元数据项（如instance-id），然后将其缓存在本地内存或文件中，并设置合理的缓存过期时间。
- 将实例元数据访问模式修改为仅加固模式后，应用无法正常工作如何排查？
可能是实例中应用或脚本中仍在使用旧的普通模式。请按照[升级到仅加固模式](view-instance-metadata.md)彻底排查并升级依赖普通模式的应用。
- 能否从本地主机访问这个元数据地址？
不能。100.100.100.200是一个本地地址，仅在ECS实例内部的虚拟网络接口上有效。任何从实例外部发往该地址的请求都无法路由，这是保障元数据安全的基础设计之一。
- 使自定义镜
