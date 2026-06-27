## 适用范围
权限要求：部署使用的阿里云主账号或子账号需具备AliyunLogFullAccess权限。
Docker 版本与 LoongCollector 要求：
如果您的Docker Engine版本大于等于v29.0，或支持的最低Docker API版本大于等于1.42，请使用LoongCollector 3.2.4及以上版本，否则将无法采集容器标准输出或文件日志。
LoongCollector3.2.4及以上版本支持的Docker API版本范围为1.24 ~ 1.48。
LoongCollector3.2.3及以下版本支持的Docker API版本范围为1.18 ~ 1.41。
采集标准输出限制：
必须在Docker的配置文件daemon.json中添加"log-driver": "json-file"。
如果是CentOS 7.4及以上版本（除CentOS 8.0以外），需设置fs.may_detach_mounts=1。
采集文本日志限制：仅支持overlay、overlay2两种存储驱动（其他类型需手动挂载日志目录）。
