### Pod创建失败，报错信息包含no providers available to validate pod request
问题现象
Pod创建失败，报错信息包含no providers available to validate pod request或者unable to validate against any pod security policy。
解决方案
当前集群内预置的Pod安全策略被误删除，需手动恢复对应资源。详见[配置或恢复](use-pod-security-policies.md)[ACK](use-pod-security-policies.md)[默认的](use-pod-security-policies.md)[Pod](use-pod-security-policies.md)[安全策略](use-pod-security-policies.md)。
