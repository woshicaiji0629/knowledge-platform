## 在Ingress上配置证书
该方法具有以下特点：
优点：无需改动SLB的配置。每一个应用都可以通过Ingress管理自己的证书，互不干扰。
适用场景：每个应用都需要单独的证书进行访问，或者集群中存在需要证书才能访问的应用。
准备工作：
您已在该Kubernetes集群中创建一个Tomcat应用，该应用的服务（Service）采用ClusterIP的方式提供访问。本例中准备使用Ingress对外提供HTTPS访问服务。更多信息，请参见[创建无状态工作负载](../../ack-managed-and-ack-dedicated/user-guide/create-a-stateless-application-by-using-a-deployment.md)[Deployment](../../ack-managed-and-ack-dedicated/user-guide/create-a-stateless-application-by-using-a-deployment.md)。
示例：
根据前提条件中准备好的证书执行以下命令创建Secret。
说明
在这里需要正确配置域名，否则后续通过HTTPS访问会有问题。
kubectl create secret tls secret-https --key tls.key --cert tls.crt
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择网络>路由。
在路由页面单击创建 Ingress。
在创建 Ingress对话框中，配置可HTTPS访问的路由，完成后单击确定。
更多详细的路由配置信息，请参见[创建路由（Ingress）](../../ack-managed-and-ack-dedicated/user-guide/create-an-nginx-ingress-1.md)。本例中进行如下配置。
名称：输入该路由的名称。
域名：即是前面配置的正确域名，与SSL证书中配置的保持一致。
服务名称：选择Tomcat应用对应的Service，端口为8080。
TLS配置：开启TLS后，选择已创建的保密字典。
您也可采用YAML文件的方式创建路由（Ingress），本例对应的YAML示例文件如下。
apiVersion: networking.k8s.io/v1 kind: Ingress metadata: name: tomcat-https spec: tls: - hosts: - foo.bar.com secretName: secret-https rules: - host: foo.bar.com http: paths: - path: / pathTy
