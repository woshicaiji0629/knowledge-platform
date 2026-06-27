# Kubernetes启用HTTPS安全访问-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/security-and-compliance/access-applications-in-an-ack-cluster-over-https

# 在Kubernetes中实现HTTPS安全访问
容器服务ACK集群支持多种应用访问的形式，最常见的形式如<SLB-Instance-IP>:<Port>、<NodeIP>:<NodePort>和域名访问等。ACK集群默认不支持HTTPS访问，如果您希望能够通过HTTPS进行应用的访问，容器服务ACK和阿里云负载均衡服务为您提供安全的HTTPS访问。本文通过实际案例演示的HTTPS访问配置，帮助您在容器服务ACK中配置自己的证书。
## 前提条件
[创建](../../ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[ACK](../../ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[托管集群](../../ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)。
创建集群的服务器证书，包括公钥证书和私钥。
您可以通过执行以下命令填写证书信息，快速创建集群的服务器证书。
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt
输出：
Generating a 2048 bit RSA private key .......+++ .......+++ writing new private key to 'tls.key' ----- You are about to be asked to enter information that will be incorporated into your certificate request. What you are about to enter is what is called a Distinguished Name or a DN. There are quite a few fields but you can leave some blank For some fields there will be a default value, If you enter '.', the field will be left blank. ----- Country Name (2 letter code) []:CN State or Province Name (full name) []:zhejiang Locality Name (eg, city) []:hangzhou Organization Name (eg, company) []:alibaba Organizational Unit Name (eg, section) []:test Common Name (eg, fully qualified host name) []:foo.bar.com # 注意，您需要正确配置域名 Email Address []:te**@alibaba.com
创建的证书以及私钥文件会保存在当前目录下的tls.crt和tls.key文件中。
您也可以选择购买阿里云签发证书。具体操作，请参见[创建证书](../../../../slb/documents/classic-load-balancer/user-guide/create-certificate.md)。
## 背景信息
根据访问方式的不同，当前可以分为两种配置证书的方式：
在前端SLB上配置证书。
在Ingress中配置证书。
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
| 注解 | 名称 | 值 |
| --- | --- | --- |
| 注解一 | service.beta.kubernetes.io/alibaba-cloud-loadbalancer-protocol-port | https:443 |
| 注解二 | service.beta.kubernetes.io/alibaba-cloud-loadbalancer-cert-id | ${YOUR_CERT_ID} |
说明
将${YOUR_CERT_ID}替换成[步骤](access-applications-in-an-ack-cluster-over-https.md)[7](access-applications-in-an-ack-cluster-over-https.md)[配置](access-applications-in-an-ack-cluster-over-https.md)[SSL](access-applications-in-an-ack-cluster-over-https.md)[证书](access-applications-in-an-ack-cluster-over-https.md)生成的证书ID。
您还可以使用YAML方式添加注解内容，完整YAML示例如下：
apiVersion: v1 kind: Service metadata: annotations: service.beta.kubernetes.io/alibaba-cloud-loadbalancer-protocol-port: "https:443" service.beta.kubernetes.io/alibaba-cloud-loadbalancer-cert-id: "${YOUR_CERT_ID}" name: nginx namespace: default spec: ports: - name: https port: 443 protocol: TCP targetPort: 80 - name: http port: 80 protocol: TCP targetPort: 80 selector: run: nginx type: LoadBalancer
说明
HTTPS的443端口对应的targetPort端口需要配置成HTTP的端口80。
访问HTTPS的Nginx应用，在浏览器中输入https://<slb-instance-ip>并进行访问。
页面成功显示 nginx 默认欢迎页面，标题为Welcome to nginx!，表明 Nginx 应用已正常运行，HTTPS 访问配置生效。
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
apiVersion: networking.k8s.io/v1 kind: Ingress metadata: name: tomcat-https spec: tls: - hosts: - foo.bar.com secretName: secret-https rules: - host: foo.bar.com http: paths: - path: / pathType: Prefix backend: service: name: tomcat-svc port: number: 8080
返回路由列表，查看创建的路由（Ingress），本例中域名为foo.bar.com，并查看端点和域名，您也可进入路由详情页进行查看。
说明
本例中以foo.bar.com作为测试域名，您需要在hosts文件中创建一条记录。
47.110.119.203 foo.bar.com #其中IP地址即是路由的端点。
在路由（Ingress）列表中，可以看到已创建的tomcat-https路由条目，其端点列显示的 IP 地址即为路由端点。
在浏览器中访问https://foo.bar.com。
说明
由于创建了TLS证书访问，所以要用HTTPS来进行域名访问，针对该应用，本例以foo.bar.com为示例，在本地进行解析。在具体使用场景中，请使用备案过的域名。
在浏览器中访问https://foo.bar.com，页面成功显示 Apache Tomcat/8.5.34 默认欢迎页面，表明 Tomcat 服务已正常部署且通过 Ingress 路由可达。
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
