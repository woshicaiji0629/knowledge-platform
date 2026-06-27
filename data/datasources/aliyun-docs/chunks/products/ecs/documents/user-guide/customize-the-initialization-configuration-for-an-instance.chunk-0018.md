## 通过元数据服务获取（加固模式）
Linux实例
TOKEN=`curl -X PUT "http://100.100.100.200/latest/api/token" -H "X-aliyun-ecs-metadata-token-ttl-seconds:180"` curl -H "X-aliyun-ecs-metadata-token: $TOKEN" http://100.100.100.200/latest/user-data
Windows实例
$token = Invoke-RestMethod -Headers @{"X-aliyun-ecs-metadata-token-ttl-seconds" = "180"} -Method PUT -Uri http://100.100.100.200/latest/api/token Invoke-RestMethod -Headers @{"X-aliyun-ecs-metadata-token" = $token} -Method GET -Uri http://100.100.100.200/latest/user-data
说明
在上述示例中，设置的token有效期为180秒，实际应用时可根据具体使用场景进行调整。
本示例使用元数据服务的加固模式来获取元数据，关于元数据服务获取信息的更多内容，请参见[实例元数据](view-instance-metadata.md)。
关于元数据的更多说明，请参见[实例元数据](view-instance-metadata.md)。
