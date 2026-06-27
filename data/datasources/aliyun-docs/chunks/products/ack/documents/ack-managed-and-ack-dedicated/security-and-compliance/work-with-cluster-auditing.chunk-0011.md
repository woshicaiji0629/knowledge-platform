### 示例1：对容器执行命令时告警
某公司对于Kubernetes集群使用有严格限制，不允许用户登录容器或对容器执行命令。如果有用户执行命令时，告警需要立即被发送，并在告警信息中包含用户登录的具体容器、执行的命令、操作人、事件ID、时间、操作源IP等信息。
查询语句为：
verb : create and objectRef.subresource:exec and stage: ResponseStarted | SELECT auditID as "事件ID", date_format(from_unixtime(__time__), '%Y-%m-%d %T' ) as "操作时间", regexp_extract("requestURI", '([^\?]*)/exec\?.*', 1)as "资源", regexp_extract("requestURI", '\?(.*)', 1)as "命令" ,"responseStatus.code" as "状态码", CASE WHEN "user.username" != 'kubernetes-admin' then "user.username" WHEN "user.username" = 'kubernetes-admin' and regexp_like("annotations.authorization.k8s.io/reason", 'RoleBinding') then regexp_extract("annotations.authorization.k8s.io/reason", ' to User "(\w+)"', 1) ELSE 'kubernetes-admin' END as "操作账号", CASE WHEN json_array_length(sourceIPs) = 1 then json_format(json_array_get(sourceIPs, 0)) ELSE sourceIPs END as "源地址" order by "操作时间" desc limit 10000
条件表达式为：操作事件 =~ ".*"。
