## 步骤二：创建应用时配置日志服务
可以在创建应用的同时配置日志服务，从而对ACK Edge集群的日志进行采集。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择工作负载>无状态。
在无状态页面上方的命名空间下拉框中设置命名空间，然后单击页面右上角的使用镜像创建。
在应用基本信息页签，设置应用名称、副本数量和类型，单击下一步，进入容器配置页面。
以下仅介绍日志服务相关的配置。关于其他的应用配置，请参见[创建无状态工作负载](../../ack-managed-and-ack-dedicated/user-guide/create-a-stateless-application-by-using-a-deployment.md)[Deployment](../../ack-managed-and-ack-dedicated/user-guide/create-a-stateless-application-by-using-a-deployment.md)。
在日志配置区域，配置日志相关信息。
设置采集配置。
重要
日志采集配置完成后，不支持修改。如需修改，请[通过](../../../../sls/documents/use-crds-to-collect-container-logs-in-daemonset-mode.md)[DaemonSet-CRD](../../../../sls/documents/use-crds-to-collect-container-logs-in-daemonset-mode.md)[方式采集容器日志](../../../../sls/documents/use-crds-to-collect-container-logs-in-daemonset-mode.md)。
单击采集配置，每个采集配置由日志库和容器内日志路径两项构成。
日志库：配置Logstore名称，用于指定所采集的日志存储于该Logstore。如果该Logstore不存在，ACK将会自动在集群关联的日志服务Project下创建相应的Logstore。
说明
新创建的Logstore中的日志默认保存时间为180天。
容器内日志路径：指定希望采集的日志所在的路径，例如使用/usr/local/tomcat/logs/catalina.*.log来采集Tomcat的文本日志。
说明
指定为stdout时，表示采集容器的标准输出和标准错误输出。
每一项采集配置都会被自动创建为对应Logstore的一个采集配置，默认采用极简模式（按行）进行采集。如果需要使用多行模式及更丰富的采集方式，请参见[通过](../../../../sls/docu
