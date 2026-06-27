# 获取元数据服务器的访问凭证用于鉴权$token=Invoke-RestMethod-Headers@{"X-aliyun-ecs-metadata-token-ttl-seconds"="元数据服务器的访问凭证有效期"} -MethodPUT-Urihttp://100.100.100.200/latest/api/token# 获取实例RAM角色的临时凭证Invoke-RestMethod-Headers@{"X-aliyun-ecs-metadata-token"=$token} -MethodGET-Urihttp://100.100.100.200/latest/meta-data/ram/security-credentials/实例RAM角色名称
<元数据服务器的访问凭证有效期>：在获取实例RAM角色的临时授权访问凭证之前，先获取元数据服务器的访问凭证并设置其有效期，以加强数据安全。超过有效期后，需要重新获取凭证，否则无法获取实例RAM角色的临时授权访问凭证。取值范围为1~21600，单位为秒。详细说明，请参见[实例元数据](view-instance-metadata.md)。
<实例RAM角色名称>：需替换为具体的实例RAM角色名称。例如EcsRamRole。
若使用云助手执行上述命令时，云助手Agent的最低版本要求如下：

| 平台 | 云助手 Agent 版本号 |
| --- | --- |
| windows | 2.1.3.857 |
| linux | 2.2.3.857 |
| linux arm | 2.4.3.857 |
| freebsd | 2.3.3.857 |
