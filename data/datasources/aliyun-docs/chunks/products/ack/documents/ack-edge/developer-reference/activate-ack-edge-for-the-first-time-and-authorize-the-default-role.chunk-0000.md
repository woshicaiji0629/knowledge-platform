# 使用Terraform首次开通ACK Edge并授权默认角色
首次使用容器服务ACK Edge集群时，需要为服务账号授予系统默认角色。只有在该角色正确授权后，ACK Edge集群才能正常调用相关服务（如 ECS、OSS、NAS、SLB 等）、创建集群并保存日志。本文将介绍如何通过Terraform为容器服务授权默认角色。
