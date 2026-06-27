# 通过自定义域名访问工作流控制台-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-argo-workflow-cluster/user-guide/access-the-workflow-console-via-a-custom-domain

# 通过自定义域名访问工作流控制台
容器Argo工作流集群默认使用IP地址提供对工作流控制台的公网访问。但因缺失SSL证书，使用IP将导致浏览器报警。通过将自定义域名指向工作流控制台IP并配置SSL证书，可以解决此问题。
## 适用范围
已[获取集群](obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)[KubeConfig](obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)[并通过](obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)[kubectl](obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)[工具连接集群](obtain-the-cluster-kubeconfig-and-connect-to-the-cluster-using-kubectl.md)。
已[开启](enable-argo-server-for-a-workflow-cluster.md)[Argo Server](enable-argo-server-for-a-workflow-cluster.md)[并访问工作流控制台](enable-argo-server-for-a-workflow-cluster.md)。
## 操作步骤
登录[容器](https://csnew.console.aliyun.com/#/next/argowf)[Argo](https://csnew.console.aliyun.com/#/next/argowf)[工作流集群控制台](https://csnew.console.aliyun.com/#/next/argowf)，单击目标集群名称。
在集群信息页面，单击工作流控制台（Argo）。然后，从浏览器中复制工作流控制台IP地址。
登录[云解析](https://dnsnext.console.aliyun.com/authoritative)[DNS-公网权威解析](https://dnsnext.console.aliyun.com/authoritative)控制台，为自定义域名添加一条A类型记录，将自定义域名指向工作流控制台IP地址。
准备SSL证书，记录证书文件cert.pem和key.pem的路径。
将SSL证书配置到集群。
将CLUSTER_ID替换为集群ID，填入证书文件路径，然后执行以下命令，在集群中创建名为argo-server-tls的Secret。
kubectl create -nCLUSTER_IDsecret tls argo-server-tls \ --cert=/path/to/cert.pem \ --key=/path/to/key.pem
将已创建的Secret配置到集群的argo-server中。
将CLUSTER_ID替换为集群ID，填入证书文件路径，然后执行以下命令，编辑argo-server文件。
kubectl -nCLUSTER_IDedit deploy argo-server
在spec.template.spec.containers.args部分添加TLS配置信息。
spec: containers: - args: - server - --auth-mode=sso - --auth-mode=client - --kube-api-qps=300 - --kube-api-burst=500 - --tls-certificate-secret-name=argo-server-tls image: ******.ack.aliyuncs.com/acs/argo:v3.5.13-a06e2ae imagePullPolicy: IfNotPresent
将自定义域名修改至RAM中OAuth应用的回调地址中。
使用RAM管理员登录[RAM](https://ram.console.aliyun.com/)[控制台](https://ram.console.aliyun.com/)。
在左侧导航栏，选择集成管理>OAuth应用（公测）。
在企业应用页签，单击目标应用ackone-argo-${cluster_id}@app.${uid}.onaliyun.com，其中，${cluster_id}为集群ID，${uid}为阿里云账号ID。
在基本信息区域，单击编辑基本信息，将回调地址修改为https://${domain}:2746/oauth2/callback，其中，${domain}为自定义的域名。
在浏览器中输入https://${domain}:2746，并使用云SSO账号登录，快速访问工作流集群控制台。
## 相关文档
如需要使用阿里云域名服务，请参见[域名注册](https://help.aliyun.com/zh/dws/user-guide/how-to-register-a-domain-name)。
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
