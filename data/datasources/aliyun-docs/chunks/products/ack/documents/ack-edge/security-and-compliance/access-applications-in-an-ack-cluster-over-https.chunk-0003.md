## 在SLB上配置HTTPS证书
该方式具有如下特点：
优点：证书配置在SLB上，为应用外部访问的入口，在集群内部进行应用的访问仍然使用HTTP访问方式。
缺点：需要维护较多的域名与IP地址的对应关系。
适用场景：应用不使用Ingress暴露访问方式，通过LoadBalancer类型的Service进行应用访问的暴露。
准备工作：
您已在该ACK集群中创建一个Nginx应用，该应用采用LoadBalancer类型的服务（Service）对外提供访问。更多信息，请参见[创建无状态工作负载](../../ack-managed-and-ack-dedicated/user-guide/create-a-stateless-application-by-using-a-deployment.md)[Deployment](../../ack-managed-and-ack-dedicated/user-guide/create-a-stateless-application-by-using-a-deployment.md)。
示例：
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择网络>服务。
选择集群的命名空间和服务，在服务列表查看其外部 IP 地址（External IP），您可通过<SLB IP>:<Port>的方式访问该应用。
成功访问后，浏览器显示 nginx 默认欢迎页面，页面标题为Welcome to nginx!，表明应用已正常运行。
登录[负载均衡管理控制台](https://slb.console.aliyun.com/)。
配置SSL证书。
如果您是通过命令方式创建集群的服务器证书，您需要使用前提条件中创建的公钥证书和私钥上传非阿里云签发证书。具体操作，请参见[创建证书](../../../../slb/documents/classic-load-balancer/user-guide/create-certificate.md)。
如果您是通过购买方式获取阿里云签发证书，请跳过此步骤。关于创建阿里云签发证书的操作，请参见[创建证书](../../../../slb/documents/classic-load-balancer/user-guide/create-certificate.md)。
在证书列表中，找到目标证书名称下面的证书ID。
在容器服务管理控制台的服务列表中，找到之前创建的服务，单击右侧操作列下的更新。
在更新服务对话框中的注解区域，添加以下两个注解内容。
请勿复用集群 APIServer 的 SLB，否则将导致集群访问异常。
