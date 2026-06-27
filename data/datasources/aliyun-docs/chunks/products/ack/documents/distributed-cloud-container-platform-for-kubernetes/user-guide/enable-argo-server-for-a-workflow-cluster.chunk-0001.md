## 前提条件
目前仅阿里云账号和工作流集群的创建者（RAM用户）可以运行CLI（kubectl、Argo)，通过访问Argo Server或Argo UI的方式操作工作流集群。如果其他的RAM用户需要访问工作流集群，请先为RAM用户授权。具体操作，请参见[用户授权](https://help.aliyun.com/zh/document_detail/2252086.html#task-2322675)。
Argo Server默认使用VPC内网IP暴露服务，您的操作终端需要支持访问VPC的内网地址。
