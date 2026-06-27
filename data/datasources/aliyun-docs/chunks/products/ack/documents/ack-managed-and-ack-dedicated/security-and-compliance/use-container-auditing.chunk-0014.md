| 配置项 | 描述 |
| --- | --- |
| 规则名称 | Kubernetes 进入容器后执行风险程序告警 |
| 检查频率 | 固定间隔 ：1 分钟。 |
| 查询统计 | 单击右侧 添加 ，然后单击 高级配置 页签，配置如下信息。配置完成后，单击 确认 。 日志库 ：搜索并选中 advaudit-${cluster_id} ，例如 advaudit-c76da730c08ca45adb90fad86fb74**** 。 查询区间 ：选中 1 分钟（相对） 。 查询 ：设置 日志库 后，才会显示该字段。代码配置为： kind: Command | select "clusterid", "time", "traceId", "eventId", "k8s.user.aliuid", "k8s.user.username", json_extract(k8s, '$.user.groups') as "k8s.user.groups", "host.hostip", "host.nodename", "k8s.pod.namespace", "k8s.pod.name", json_extract(k8s, '$.pod.labels') as "k8s.pod.labels", "k8s.container.name", "k8s.container.image", "process.cwd", "process.name", "process.cmdline", json_extract(process, '$.pid') as "process.pid", "process.user.uid", json_extract(process, '$.parentPid') as "process.parentpid", "process.parentname" from log where "process.name" in ('rm', 'sudo', 'su', 'nsenter', 'curl', 'wget', 'yum', 'apt-get', 'apt', 'apk', 'dpkg', 'nc', 'ncat', 'ssh', 'scp', 'nmap', 'docker', 'crictl', 'nerdctl', 'podman', 'kubectl', 'helm', 'mysql', 'redis', 'psql', 'redis-cli', 'pip', 'npm', 'gem') |
| 触发条件 | 当 有数据 时，严重程度： 中 。 |
| 输出目标 | 选择 SLS 通知 。 |
| 开启 | 打开开关。 |
| 告警策略 | 选择 极简模式 ，并配置如下信息。 渠道 ：选择 钉钉 。 选择 Webhook ：选
