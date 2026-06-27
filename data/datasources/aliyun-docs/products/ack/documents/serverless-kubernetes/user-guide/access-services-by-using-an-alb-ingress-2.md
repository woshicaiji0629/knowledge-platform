# 使用ALB Ingress访问集群内服务-容器服务 Kubernetes 版 ACK-阿里云

Source: https://help.aliyun.com/zh/ack/serverless-kubernetes/user-guide/access-services-by-using-an-alb-ingress-2

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/serverless-kubernetes/product-overview.md)

- [快速入门](products/ack/documents/serverless-kubernetes/getting-started.md)

- [操作指南](products/ack/documents/serverless-kubernetes/user-guide.md)

- [实践教程](products/ack/documents/serverless-kubernetes/use-cases.md)

- [安全合规](products/ack/documents/serverless-kubernetes/security-and-compliance.md)

- [开发参考](products/ack/documents/serverless-kubernetes/developer-reference.md)

- [服务支持](products/ack/documents/serverless-kubernetes/support.md)

[首页](https://help.aliyun.com/zh)

# 通过ALB Ingress访问服务

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

ALB Ingress支持HTTP、HTTPS和QUIC协议，满足云原生应用在需要高度弹性和大规模七层流量管理时的各种需求，与Nginx Ingress兼容。同时，支持复杂的业务路由配置和TLS证书的自动管理，提供灵活的流量管理机制。您可以通过配置转发规则，实现不同URL访问集群内不同的Service。

## 前提条件

- 

已创建ACK Serverless集群，且Kubernetes版本为1.18及以上版本。具体操作，请参见[容器服务 Serverless 版使用快速入门](products/ack/documents/serverless-kubernetes/getting-started/ask-quick-start.md)。

- 

已创建两个不同可用区的交换机，并且与集群处于同一VPC。具体操作，请参见[创建和管理交换机](products/vpc/documents/user-guide/create-and-manage-vswitch.md)。

- 

已为集群安装ALB Ingress Controller组件。具体操作，请参见[管理](products/ack/documents/serverless-kubernetes/user-guide/manage-the-alb-ingress-controller.md)[ALB Ingress Controller](products/ack/documents/serverless-kubernetes/user-guide/manage-the-alb-ingress-controller.md)[组件](products/ack/documents/serverless-kubernetes/user-guide/manage-the-alb-ingress-controller.md)。

- 您已通过kubectl连接到集群。具体操作，请参见[通过](products/ack/documents/serverless-kubernetes/user-guide/connect-to-an-ack-cluster-by-using-kubectl.md)[kubectl](products/ack/documents/serverless-kubernetes/user-guide/connect-to-an-ack-cluster-by-using-kubectl.md)[连接](products/ack/documents/serverless-kubernetes/user-guide/connect-to-an-ack-cluster-by-using-kubectl.md)[Kubernetes](products/ack/documents/serverless-kubernetes/user-guide/connect-to-an-ack-cluster-by-using-kubectl.md)[集群](products/ack/documents/serverless-kubernetes/user-guide/connect-to-an-ack-cluster-by-using-kubectl.md)。

## 注意事项

- 

如果您使用的是Flannel网络插件，则ALB Ingress后端Service服务仅支持NodePort和LoadBalancer类型。

- 

AlbConfig、Namespace、Ingress和Service这些资源的名称不能以aliyun开头。

- 

低版本Nginx Ingress Controller无法识别Ingress资源中的spec：ingressClassName字段。如果集群中同时存在Nginx Ingress和ALB Ingress，会存在ALB Ingress被低版本Nginx Ingress Controller调谐的风险。因此，请及时升级Nginx Ingress Controller版本，或通过Annotation注解项指定ALB Ingress对应的ingressClass。具体操作，请参见[升级](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/update-the-nginx-ingress-controller.md)[Nginx Ingress Controller](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/update-the-nginx-ingress-controller.md)[组件](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/update-the-nginx-ingress-controller.md)或[ALB Ingress](products/ack/documents/serverless-kubernetes/user-guide/advanced-alb-ingress-settings.md)[服务高级用法](products/ack/documents/serverless-kubernetes/user-guide/advanced-alb-ingress-settings.md)。

## 步骤一：创建AlbConfig

- 

拷贝以下内容到alb-test.yaml文件中，用于创建AlbConfig。

apiVersion: alibabacloud.com/v1 kind: AlbConfig metadata: name: alb-demo spec: config: name: alb-test addressType: Internet zoneMappings: - vSwitchId: vsw-uf6ccg2a9g71hx8go**** - vSwitchId: vsw-uf6nun9tql5t8nh15**** listeners: - port: 80 protocol: HTTP

- 

- 

| 参数 | 说明 |
| --- | --- |
| spec.config.name | （可选）表示 ALB 实例的名称。 |
| spec.config.addressType | （必选）表示负载均衡的地址类型。取值如下： Internet（默认值）：负载均衡具有公网 IP 地址，DNS 域名被解析到公网 IP，因此可以在公网环境访问。 Intranet：负载均衡只有私网 IP 地址，DNS 域名被解析到私网 IP，因此只能被负载均衡所在 VPC 的内网环境访问。 |
| spec.config.zoneMappings | （必选）用于设置 ALB Ingress 交换机 ID，您需要至少指定两个不同可用区交换机 ID，指定的交换机必须在 ALB 当前所支持的可用区内，且与集群处于同一 VPC。关于 ALB Ingress 支持的地域与可用区，请参见 [ALB](products/slb/documents/application-load-balancer/product-overview/supported-regions-and-zones.md) [支持的地域与可用区](products/slb/documents/application-load-balancer/product-overview/supported-regions-and-zones.md) 。 |


- 

执行以下命令，创建AlbConfig。

kubectl apply -f alb-test.yaml

预期输出：

albconfig.alibabacloud.com/alb-demo created

- 

创建并拷贝以下内容到alb.yaml文件中，用于创建IngressClass。

## 1.19及之后版本集群

apiVersion: networking.k8s.io/v1 kind: IngressClass metadata: name: alb spec: controller: ingress.k8s.alibabacloud/alb parameters: apiGroup: alibabacloud.com kind: AlbConfig name: alb-demo

## 1.19版本之前集群

apiVersion: networking.k8s.io/v1beta1 kind: IngressClass metadata: name: alb spec: controller: ingress.k8s.alibabacloud/alb parameters: apiGroup: alibabacloud.com kind: AlbConfig name: alb-demo

- 

执行以下命令，创建IngressClass。

kubectl apply -f alb.yaml

预期输出：

ingressclass.networking.k8s.io/alb created

## 步骤二：部署服务

- 

创建并拷贝以下内容到cafe-service.yaml文件中，用于部署两个名称分别为coffee和tea的Deployment，以及两个名称分别为coffee和tea的Service。

展开查看完整的YAML文件

apiVersion: apps/v1 kind: Deployment metadata: name: coffee spec: replicas: 2 selector: matchLabels: app: coffee template: metadata: labels: app: coffee spec: containers: - name: coffee image: registry.cn-hangzhou.aliyuncs.com/acs-sample/nginxdemos:latest ports: - containerPort: 80 --- apiVersion: v1 kind: Service metadata: name: coffee-svc spec: ports: - port: 80 targetPort: 80 protocol: TCP selector: app: coffee clusterIP: None --- apiVersion: apps/v1 kind: Deployment metadata: name: tea spec: replicas: 1 selector: matchLabels: app: tea template: metadata: labels: app: tea spec: containers: - name: tea image: registry.cn-hangzhou.aliyuncs.com/acs-sample/nginxdemos:latest ports: - containerPort: 80 --- apiVersion: v1 kind: Service metadata: name: tea-svc labels: spec: ports: - port: 80 targetPort: 80 protocol: TCP selector: app: tea clusterIP: None

- 

执行以下命令，部署两个Deployment和两个Service。

kubectl apply -f cafe-service.yaml

预期输出：

deployment "coffee" created service "coffee-svc" created deployment "tea" created service "tea-svc" created

- 

查看创建的应用和服务的状态。

- 

执行以下命令，查看应用的状态。

kubectl get deploy

预期输出：

NAME READY UP-TO-DATE AVAILABLE AGE coffee 1/2 2 1 2m26s tea 1/1 1 1 2m26s

- 

执行以下命令，查看服务的状态。

kubectl get svc

预期输出：

NAME TYPE CLUSTER-IP EXTERNAL-IP PORT(S) AGE coffee-svc NodePort 172.16.XX.XX <none> 80:32056/TCP 9m38s tea-svc NodePort 172.16.XX.XX <none> 80:31696/TCP 9m38s

## 步骤三：配置ALB Ingress

- 

创建并拷贝以下内容到cafe-ingress.yaml文件中。

## 1.19及之后版本集群

apiVersion: networking.k8s.io/v1 kind: Ingress metadata: name: cafe-ingress spec: ingressClassName: alb rules: - host: demo.domain.ingress.top http: paths: # 配置Context Path - path: /tea pathType: ImplementationSpecific backend: service: name: tea-svc port: number: 80 # 配置Context Path - path: /coffee pathType: ImplementationSpecific backend: service: name: coffee-svc port: number: 80

## 1.19版本之前集群

apiVersion: networking.k8s.io/v1beta1 kind: Ingress metadata: name: cafe-ingress spec: ingressClassName: alb rules: - host: demo.domain.ingress.top http: paths: # 配置Context Path。 - path: /tea backend: serviceName: tea-svc servicePort: 80 # 配置Context Path。 - path: /coffee backend: serviceName: coffee-svc servicePort: 80

- 

执行以下命令，配置coffee和tea服务对外暴露的域名和path路径。

kubectl apply -f cafe-ingress.yaml

预期输出：

ingress.networking.k8s.io/cafe-ingress created

- 

执行以下命令获取ALB实例地址。

kubectl get ing

预期输出：

NAME CLASS HOSTS ADDRESS PORTS AGE cafe-ingress alb demo.domain.ingress.top alb-m551oo2zn63yov****.cn-hangzhou.alb.aliyuncs.com 80 50s

## 步骤四：访问服务

- 

利用获取的ALB实例地址，通过命令行方式访问coffee服务。

curl -H Host:demo.domain.ingress.top http://alb-lhwdm5c9h8lrcm****.cn-hangzhou.alb.aliyuncs.com/coffee

- 

利用获取的ALB实例地址，通过命令行方式访问tea服务。

curl -H Host:demo.domain.ingress.top http://alb-lhwdm5c9h8lrcm****.cn-hangzhou.alb.aliyuncs.com/tea

## 相关文档

- 

如需了解ALB Ingress服务的高级用法，例如如何将来自不同域名或URL路径的请求转发给不同的后端服务器组、配置健康检查、将HTTP访问重定向至HTTPS、灰度发布、配置自定义监听端口等，请参见[ALB Ingress](products/ack/documents/serverless-kubernetes/user-guide/advanced-alb-ingress-settings.md)[服务高级用法](products/ack/documents/serverless-kubernetes/user-guide/advanced-alb-ingress-settings.md)。

- 

如需自定义ALB Ingress的转发规则，自行配置转发条件和动作，请参见[自定义](products/ack/documents/serverless-kubernetes/user-guide/customize-the-routing-rules-of-an-alb-ingress.md)[ALB Ingress](products/ack/documents/serverless-kubernetes/user-guide/customize-the-routing-rules-of-an-alb-ingress.md)[的转发规则](products/ack/documents/serverless-kubernetes/user-guide/customize-the-routing-rules-of-an-alb-ingress.md)。

- 

如需让HTTPS监听转发来自HTTPS协议的请求，请参见[使用](products/ack/documents/serverless-kubernetes/user-guide/use-an-alb-ingress-to-configure-certificates-for-an-https-listener-1.md)[ALB Ingress](products/ack/documents/serverless-kubernetes/user-guide/use-an-alb-ingress-to-configure-certificates-for-an-https-listener-1.md)[配置](products/ack/documents/serverless-kubernetes/user-guide/use-an-alb-ingress-to-configure-certificates-for-an-https-listener-1.md)[HTTPS](products/ack/documents/serverless-kubernetes/user-guide/use-an-alb-ingress-to-configure-certificates-for-an-https-listener-1.md)[监听证书](products/ack/documents/serverless-kubernetes/user-guide/use-an-alb-ingress-to-configure-certificates-for-an-https-listener-1.md)。

- 

如果您在使用ALB Ingress过程中遇到问题，可先参见[ALB Ingress](products/ack/documents/serverless-kubernetes/user-guide/troubleshooting-alb-ingress-exceptions.md)[异常问题排查](products/ack/documents/serverless-kubernetes/user-guide/troubleshooting-alb-ingress-exceptions.md)、[ALB Ingress FAQ](products/ack/documents/serverless-kubernetes/user-guide/alb-ingress-faq.md)自助排查问题。

[上一篇：管理ALB Ingress Controller组件](products/ack/documents/serverless-kubernetes/user-guide/manage-the-alb-ingress-controller.md)[下一篇：ALB配额计算方式](products/ack/documents/serverless-kubernetes/user-guide/alb-quota-calculation-method.md)

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
