## Linux
[登录](connect-to-a-linux-instance-by-using-a-password-or-key.md)实例。
获取临时令牌（Token）。
TOKEN=`curl -X PUT "http://100.100.100.200/latest/api/token" -H "X-aliyun-ecs-metadata-token-ttl-seconds:21600"`参数X-aliyun-ecs-metadata-token-ttl-seconds: 令牌有效期，取值范围：1~21600（秒）
携带令牌（Token）获取元数据。
curl -H "X-aliyun-ecs-metadata-token: $TOKEN" http://100.100.100.200/latest/meta-data/instance-id命令末尾的instance-id代表获取实例ID，可替换为其他需要获取的[元数据项](view-instance-metadata.md)。例如mac（获取MAC地址）或hostname（获取主机名）。
成功执行后，终端将仅输出实例ID字符串，例如：i-bp1******
