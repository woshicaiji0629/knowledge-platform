, "logtail_version" : "0.16.13", "os" : "Linux; 3.10.0-693.2.2.el7.x86_64; #1 SMP Tue Sep 12 22:26:13 UTC 2017; x86_64", "update_time" : "2018-09-04 09:28:36" }

| 字段 | 说明 |
| --- | --- |
| UUID | 服务器序列号。 |
| hostname | 主机名。 |
| instance_id | 随机生成的 Logtail 唯一标识。 |
| ip | Logtail 获取到的 IP 地址。该字段为空时表示 Logtail 没有获取到 IP 地址，Logtail 无法正常运行，请为服务器设置 IP 地址并重启 Logtail。 说明 如果您创建了 IP 地址机器组，请确保机器组中配置的 IP 与此处显示的 IP 地址一致。若不一致，请确认主机 IP 的正确值，选择在 日志服务 控制台上修改机器组内 IP 地址，或者在 [设置](select-a-network-type.md) [Logtail](select-a-network-type.md) [启动参数](select-a-network-type.md) 中修改参数 working_ip 的值。 |
| logtail_version | Logtail 客户端版本。 |
| os | 操作系统版本。 |
| update_time | Logtail 最近一次启动时间。 |
