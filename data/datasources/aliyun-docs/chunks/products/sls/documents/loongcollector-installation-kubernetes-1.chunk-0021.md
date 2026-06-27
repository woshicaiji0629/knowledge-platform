账号 ID，多个账号之间使用半角逗号（,）相隔。 |
| region ：Project 所在地域的 [RegionID](loongcollector-installation-kubernetes-1.md) 。 |  |
| net ：Internet，不同地域之间无法通过内网互通，请使用公网传输数据。 |  |

创建机器组：
登录[日志服务控制台](https://sls.console.aliyun.com/)，单击目标Project。
在左侧导航栏中，选择资源>>>机器组，单击机器组右侧的>>>创建机器组。
在创建机器组对话框中，配置如下参数，然后单击确定。
设置机器组名称。
机器组标识：选择用户自定义标识。
用户自定义标识：k8s-group-${cluster_id}，请将${cluster_id}替换集群实际的clusterID。
创建完成后，在机器组列表，单击新建的机器组，在机器组配置>>>机器组状态区域，查看心跳状态。如果心跳为OK则表示创建成功。若心跳失败，请检查用户标识与用户自定义标识内容是否正确。
修改完成后，单击更新使配置生效。
