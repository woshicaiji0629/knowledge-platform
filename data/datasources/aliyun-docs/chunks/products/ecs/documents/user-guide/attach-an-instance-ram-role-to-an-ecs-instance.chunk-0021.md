### 手动获取STS临时凭证（用于脚本或调试）
在Shell脚本等非SDK环境中，可手动调用元数据服务接口获取凭证。
方式一：通过Shell命令获取
元数据服务提供HTTP访问地址获取临时访问凭据。
加固模式
Linux实例
#获取元数据服务器的访问凭证用于鉴权TOKEN=`curl -X PUT "http://100.100.100.200/latest/api/token" -H "X-aliyun-ecs-metadata-token-ttl-seconds:元数据服务器访问凭证有效期"`#获取实例RAM角色的临时凭证curl -H "X-aliyun-ecs-metadata-token: $TOKEN" http://100.100.100.200/latest/meta-data/ram/security-credentials/实例RAM角色名称
Windows实例（Powershell）
