s-related-to-logtail-machine-groups.md)[Logtail](troubleshoot-the-errors-related-to-logtail-machine-groups.md)。
Project地域信息请参见[开服地域](sls-supported-regions1.md)。

| 场景 | 网络类型 | <config_region> | <endpoint> |
| --- | --- | --- | --- |
| 服务器为 ECS，且与 Project 属于同一地域 | 阿里云内网 | <project 地域>-intranet | <project 地域>-intranet.log.aliyuncs.com |
| 其它情况 | 公网 | <project 地域> | <project 地域>.log.aliyuncs.com |
| 传输加速 | log-global.aliyuncs.com |  |  |
