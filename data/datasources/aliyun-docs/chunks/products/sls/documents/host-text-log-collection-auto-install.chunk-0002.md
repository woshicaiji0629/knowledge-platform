## 适用范围
支持的操作系统与架构：
LoongCollector 当前仅支持 Linux 系统；Windows 主机请使用 Logtail。新接入场景建议优先选用 LoongCollector。
LoongCollector 是阿里云日志服务推出的新一代日志采集 Agent，是 Logtail 的升级版。用户在使用时，只需安装LoongCollector或Logtail其中之一，无需重复安装。
计算资源要求：
CPU：最少预留0.4 Core。
内存：最少需要 300 MB。
使用率建议：为保证稳定运行，建议LoongCollector（Logtail）的实际资源使用率低于限制值的80%。实际使用量与采集速率、监控目录和文件数量、发送阻塞程度等因素相关。
权限要求：
若使用 RAM 用户操作，需授予AliyunLogFullAccess和AliyunECSFullAccess权限。如需精细化授权，请参考[附录：自定义权限策略](host-text-log-collection-auto-install.md)。
