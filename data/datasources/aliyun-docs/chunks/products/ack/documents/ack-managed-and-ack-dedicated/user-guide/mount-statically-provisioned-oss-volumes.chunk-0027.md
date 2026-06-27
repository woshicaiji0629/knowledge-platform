## 控制台
在[ACK](https://cs.console.aliyun.com)[集群列表](https://cs.console.aliyun.com)页面，单击目标集群名称，在集群详情页左侧导航栏，选择工作负载>无状态。
在无状态页面，单击使用镜像创建。
单击使用镜像创建，按照页面提示配置应用参数。
关键参数如下，其他参数保持默认即可。详见[创建无状态工作负载](create-a-stateless-application-by-using-a-deployment.md)[Deployment](create-a-stateless-application-by-using-a-deployment.md)。

| 配置页 | 参数 | 说明 |
| --- | --- | --- |
| 应用基本信息 | 副本数量 | Deployment 副本数量。 |
| 容器配置 | 镜像名称 | 用于部署应用的镜像地址，如 anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/nginx:1.14.1-8.6 。 |
| 所需资源 | 所需的 vCPU 和内存资源。 |  |
| 数据卷 | 单击 增加云存储声明（PersistentVolumeClaim） ，然后完成参数配置。 挂载源 ：选择之前创建的 PVC。 容器路径 ：输入 OSS 要挂载到的容器路径，如 /data 。 |  |
| 标签和注解 | Pod 标签 | 如名称为 app，值为 nginx。 |

查看应用部署状态。
在无状态页面，单击应用名称，在容器组页签下，确认Pod已正常运行（状态为Running）。
