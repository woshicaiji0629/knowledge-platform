# 使用集群的API Server审计功能实现集群安全运维
审计（Auditing）产生于API Server内部，用于记录对Kubernetes API的请求以及请求结果。ACK集群提供API Server的审计日志，帮助集群管理人员排查“什么人在什么时间对什么资源做了什么操作”，可用于追溯集群操作历史、排查集群故障等，降低集群安全运维压力。
