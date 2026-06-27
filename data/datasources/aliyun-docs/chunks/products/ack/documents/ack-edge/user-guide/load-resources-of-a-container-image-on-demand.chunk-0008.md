## 其它类型集群
您需要为节点添加镜像加速标签alibabacloud.com/image-accelerate-enabled: true，以在节点初始化时自动开启镜像加速功能并安装镜像存储插件。
不同类型集群的标签设置方式如下：

| 集群类型 | 配置方式及文档链接 |
| --- | --- |
| ACK Serverless 集群 | [创建节点池](../../serverless-kubernetes/developer-reference/api-cs-2015-12-15-createclusternodepool-serverless.md) [修改节点池配置](../../serverless-kubernetes/developer-reference/api-cs-2015-12-15-modifyclusternodepool-serverless.md) |
| ACK Edge 集群 | 云端节点池请参见 [创建和管理节点池](create-a-node-pool.md) 边缘节点池请参见 [创建边缘节点池](edge-node-pool-management.md) |
| ACK 灵骏集群 | [灵骏节点池](../../ack-lingjun-managed-clusters/user-guide/overview-of-lingjun-node-pools.md) |
| 容器计算服务 ACS | [节点标签和污点管理](https://help.aliyun.com/zh/cs/user-guide/node-label-and-taint-management) |

安装镜像加速组件。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，单击组件管理。
在组件管理页面的其他区域找到aliyun-acr-acceleration-suite，单击右侧的安装。
在提示对话框中单击确认。
在左侧导航栏，选择工作负载>守护进程集，在守护进程集页面，查看组件守护进程安装详情。
在左侧导航栏，选择工作负载>无状态，在无状态页面查看组件无状态应用安装详情。
当目标组件的容器组数量显示全部启动完成，表示组件安装成功。
