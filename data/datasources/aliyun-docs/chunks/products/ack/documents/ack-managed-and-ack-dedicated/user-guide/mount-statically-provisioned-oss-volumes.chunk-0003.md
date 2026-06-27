### 1. 在集群中启用RRSA
在[ACK](https://cs.console.aliyun.com)[集群列表](https://cs.console.aliyun.com)页面，单击目标集群名称，选择集群信息。
在基本信息页签的安全与审计区域，单击RRSA OIDC右侧的开启，按照页面提示在业务低峰期完成RRSA的启用。
当集群状态由更新中变为运行中，表明RRSA已成功启用。
重要
启用RRSA功能后，集群内新创建的ServiceAccount Token的最大有效期将限制为12小时。
