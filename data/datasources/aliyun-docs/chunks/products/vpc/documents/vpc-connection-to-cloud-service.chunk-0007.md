在VPC内访问Bucket的账号。如果涉及多个Bucket，在每个Bucket里均需要进行操作。
绑定/解绑路由表
可以通过网关终端节点绑定/解绑路由表，控制VPC内哪些交换机通过网关终端节点访问云服务。
前往[专有网络控制台-网关终端节点](https://vpc.console.aliyun.com/endpoint/cn-hangzhou/vpcEndpoints)页面，单击目标网关终端节点实例ID。
在关联的路由表页签：
绑定新的路由表：单击关联路由表。绑定完成后，可以在关联路由表的自定义路由条目中，查看到一条系统自动添加的、下一跳指向网关终端节点的路由条目。
解绑已有路由表：单击已关联路由表右侧的解除关联。解绑后，系统添加的路由条目将会被自动移除。
删除网关终端节点
删除网关终端节点前，您需要先解绑所有已关联的路由表。
解绑所有已关联的路由表。
前往[专有网络控制台-网关终端节点](https://vpc.console.aliyun.com/endpoint/cn-hangzhou/vpcEndpoints)页面，单击目标网关终端节点实例右侧的删除。
（可选）由于Bucket中仍然存在Bucket授权策略，会限制其他VPC无法访问该Bucket。如需调整，可以前往[OSS](https://oss.console.aliyun.com/bucket)[控制台-Bucket](https://oss.console.aliyun.com/bucket)页面，单击目标Bucket名称，左侧导航选择权限控制 > Bucket授权策略，调整或删除仅允许从指定VPC访问的策略。
