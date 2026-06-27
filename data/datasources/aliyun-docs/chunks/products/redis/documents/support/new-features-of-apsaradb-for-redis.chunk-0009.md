## Redis开源版4.0（已停售）
展开查看详情
新特性
关于Redis4.0的新特性请参见[4.0 release note](https://raw.githubusercontent.com/redis/redis/4.0/00-RELEASENOTES)。
支持[审计日志](../user-guide/enable-the-new-audit-log-feature.md)。
支持[实时热](../user-guide/use-the-real-time-key-statistics-feature.md)[Key](../user-guide/use-the-real-time-key-statistics-feature.md)[统计](../user-guide/use-the-real-time-key-statistics-feature.md)。
开通VPC免密后，可通过设置#no_loose_check-whitelist-always参数，选择是否对同一VPC的网络连接进行白名单验证，更多信息请参见[参数支持](../user-guide/supported-parameters.md)。
支持[Sentinel](../user-guide/use-the-sentinel-compatible-mode-to-connect-to-an-apsaradb-for-redis-instance.md)[兼容模式](../user-guide/use-the-sentinel-compatible-mode-to-connect-to-an-apsaradb-for-redis-instance.md)，需开通VPC免密，仅支持SENTINEL和get-master-addr-by-name两个子命令。
支持创建多个账号（账号名称大小写不敏感），并可以对账号设置读写、只读权限，您可以通过AUTH user:password切换账号。
默认账号为实例名（例如r-bp1857n194kiuv****）。
若未指定账号或者账号不存在，则自动转为默认账号鉴权（实例名）。
若开通VPC免密，免密连接无需鉴权，将使用默认账号，且无法切换账号。
集群架构支持开通[直连模式地址](../user-guide/enable-the-direct-connection-mode.md)。
集群架构支持通过设置ptod_enabled参数，将客户端IP透传给DB节点，更多信息请参见[参数支持](../user-guide/supported-parameters.md)。
兼容性
关于社区演进的Breaking change请参见[4.0 release note](https://raw.githubusercontent.com/redis/red
