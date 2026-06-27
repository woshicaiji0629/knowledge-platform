## Windows
[登录](connect-to-a-windows-instance-through-workbench.md)实例。
获取临时令牌（Token）。
$token = Invoke-RestMethod -Headers @{"X-aliyun-ecs-metadata-token-ttl-seconds" = "21600"} -Method PUT -Uri http://100.100.100.200/latest/api/token参数X-aliyun-ecs-metadata-token-ttl-seconds: 令牌有效期，取值范围1~21600（秒）。
携带令牌（Token）获取元数据。
Invoke-RestMethod -Headers @{"X-aliyun-ecs-metadata-token" = $token} -Method GET -Uri http://100.100.100.200/latest/meta-data/instance-id命令末尾的instance-id代表获取实例ID，可替换为其他需要获取的[元数据项](view-instance-metadata.md)。例如mac（获取MAC地址）或hostname（获取主机名）。
成功执行后，终端将仅输出实例ID字符串，例如：i-bp1******
