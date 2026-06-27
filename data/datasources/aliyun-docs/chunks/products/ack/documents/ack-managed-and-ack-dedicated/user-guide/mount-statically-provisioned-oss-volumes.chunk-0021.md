## 控制台
将[步骤一](mount-statically-provisioned-oss-volumes.md)获取的AccessKey存储为Secret，供PV使用。
在[ACK](https://cs.console.aliyun.com)[集群列表](https://cs.console.aliyun.com)页面，单击目标集群名称，在集群详情页左侧导航栏，选择配置管理>保密字典。
单击使用YAML创建资源，按照页面提示，完成Secret的创建。
apiVersion: v1 kind: Secret metadata: name: oss-secret # 需与应用所在的命令空间保持一致 namespace: default stringData: # 替换为此前获取的AccessKey ID akId: <your AccessKey ID> # 替换为此前获取的AccessKey Secret akSecret: <your AccessKey Secret>
在[ACK](https://cs.console.aliyun.com)[集群列表](https://cs.console.aliyun.com)页面，单击目标集群名称，在集群详情页左侧导航栏，选择存储>存储卷。
在存储卷页面，单击创建，选择存储卷类型为OSS，按照页面配置并提交参数。
关键参数如下。
