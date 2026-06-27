# 加速容器运行启动-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/load-resources-of-a-container-image-on-demand

# 按需加载容器镜像
传统容器运行需要将全量镜像数据下载后再解包，然而容器启动可能仅使用其中部分的内容，导致容器启动耗时长。通过容器镜像服务企业版的按需加载功能，允许仅下载和解压容器启动所必需的部分，而不是整个镜像，从而大幅提高应用部署速度和提升弹性体验。
## 前提条件
支持ACK集群版本及类型。
说明
支持在版本≥1.16.9的托管版、专有版，≥1.26.3的ACK Edge集群和ACK Serverless集群、ACK灵骏集群和容器计算服务ACS上使用加速镜像。且创建集群时操作系统为Alibaba Cloud Linux 2.1903、Alibaba Cloud Linux 3.2104、Alibaba Cloud Linux 3.2104 LTS 64 bit ARM edition、Alibaba Cloud Linux UEFI 2.1903、CentOS 7.9。
已创建企业版实例，更多信息，请参见[创建企业版实例](https://help.aliyun.com/zh/acr/user-guide/create-a-container-registry-enterprise-edition-instance#task488)。
重要
在镜像加速中，两种模式支持的企业版实例规格有所不同：
完整模式：支持的企业版实例为标准版或高级版。
仅索引模式：支持的企业版实例为基础版、标准版或高级版。
已在企业版实例中配置ACK或ACK Serverless集群对应的专有网络。加速镜像需要在专有网络中使用，更多信息，请参见[配置专有网络的访问控制](https://help.aliyun.com/zh/acr/user-guide/configure-access-over-vpcs#task1305)。
## 背景信息
通过容器镜像服务企业版的按需加载功能，您可以在业务部署中使用加速镜像版本，实现镜像数据免全量下载和在线解压，大幅提升应用分发效率和弹性体验。镜像的加速效果与镜像大小、镜像仓库网络等因素有关。经实测，基于Docker Hub的[NodeBB](https://github.com/NodeBB/NodeBB)镜像（1.34 GB）启动应用在镜像拉取阶段需耗费36s，整体应用启动时间38s。基于加速镜像启动应用在镜像拉取阶段仅需4s，整体应用启动时间仅需9s。
## 使用限制
如果您的容器运行时为Containerd，则支持加速镜像仓库使用自定义域名，而Docker由于自身限制暂不支持加速镜像仓库自定义域名的使用。更多信息，请参见[通过自定义域名访问容器镜像服务企业版实例](https://help.aliyun.com/zh/acr/user-guide/use-a-custom-domain-name-to-access-a-container-registry-enterprise-edition-instance#task-1955575)。
仅索引模式不支持在FC和SAE的场景下使用。
存量镜像需要手动触发加速镜像转换。
## 地域限制
金融云与政务云地域不支持按需加载功能。
## 转换加速镜像
目前支持仓库级别配置，自动将推送的原始镜像转换为加速镜像。镜像转换时间取决于您的镜像大小，原始镜像不受任何影响。
说明
加速镜像的命名空间和仓库名称与原始镜像保持一致，Tag格式为：
仅索引模式：原始镜像tag+_accelerated后缀的加速镜像仅支持Containerd运行时，且使用时原始镜像tag不可删除。
完整模式：
原始镜像tag+_accelerated后缀的加速镜像。支持Docker和Containerd运行时
原始镜像tag+_containerd_accelerated后缀的加速镜像仅适用于Containerd运行时。
注意使用时_containerd_accelerated后缀的镜像和其原始镜像均不可删除。
登录[容器镜像服务控制台](https://cr.console.aliyun.com)。
在顶部菜单栏，选择所需地域。
在左侧导航栏，选择实例列表。
在实例列表页面单击目标企业版实例。
在企业版实例管理页左侧导航栏中选择仓库管理>镜像仓库。
在镜像仓库页面单击目标镜像仓库名称或目标镜像仓库右侧操作列下的管理。然后在基本信息页面左上角单击编辑。
在修改基本信息对话框中，开启镜像加速，并选择所需模式后，单击确定。
完整模式：容器启动的加速效果较为显著，转换生成的加速镜像体积约为原镜像体积的130%，1GB原始镜像生成加速镜像的时间约为25秒，已生成的镜像层不会重复生成。
仅索引模式：容器启动的加速效果约为70%完整模式加速效果，加速镜像体积约为3%原镜像体积，1GB原始镜像生成加速镜像时间约为3秒，已生成索引的镜像层不会重复生成。
重要
仅索引模式正在公测中，建议您使用前先在测试环境进行验证，验证适用您的业务场景后再应用到生产环境中。
说明
仅索引模式目前仅适用于tar和tgz压缩的镜像，不适用于其他压缩方式（如zstd压缩）的镜像。
仅索引模式需要绑定原始镜像使用，使用时原始镜像不可删除，完整模式可以独立使用加速镜像。
仅索引模式不支持Docker运行时使用。
在完成镜像加速转换设置后，您后续推送的镜像将自动触发镜像转换任务。若您希望接收镜像转换完成的通知，可以配置事件通知。例如将表达式设置为_accelerated$，更多信息，请参见[事件通知](https://help.aliyun.com/zh/acr/user-guide/event-notification/)。
（可选）指定预取文件列表。该列表中出现的文件项将在加速镜像启动的时候被优先预取，推荐在容器启动需要读取大文件时使用该功能。
说明
格式为每行一个文件绝对路径，如果为目录则需要以/结尾。
## 安装镜像加速组件
为了启动加速容器，需要在Worker节点安装按需加载相关的镜像存储插件。
为了支持DADI加速镜像，可以在ACK控制台中，通过节点池的容器镜像加速开关，为新建节点池或存量节点池启用节点的镜像加速功能。
## ACK托管版与专有集群
### 为新建节点池时开启
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择节点管理>节点池。
在节点池页面，参见[创建和管理节点池](../../ack-managed-and-ack-dedicated/user-guide/create-a-node-pool.md)完成配置并勾选高级选项中容器镜像加速。
### 为已有节点池开启
开启或关闭节点池容器镜像加速开关后，仅对新增节点生效。如需针对存量节点生效，需要将节点移除出节点池后，重新添加回节点池，相关操作，请参见[移除节点](../../ack-managed-and-ack-dedicated/user-guide/remove-a-node-11.md)并[添加已有节点](../../ack-managed-and-ack-dedicated/user-guide/add-existing-ecs-instances-to-an-ack-cluster.md)。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择节点管理>节点池。
在节点池列表页面，单击目标节点池所在行操作列的编辑，在高级选项中，勾选容器镜像加速，按照页面提示更新节点池的配置项。
在节点池列表，如果节点池状态显示更新中，表明节点池正在变更中。显示已激活，表明变更已完成。
## 其它类型集群
您需要为节点添加镜像加速标签alibabacloud.com/image-accelerate-enabled: true，以在节点初始化时自动开启镜像加速功能并安装镜像存储插件。
不同类型集群的标签设置方式如下：
| 集群类型 | 配置方式及文档链接 |
| --- | --- |
| ACK Serverless 集群 | [创建节点池](../../serverless-kubernetes/developer-reference/api-cs-2015-12-15-createclusternodepool-serverless.md) [修改节点池配置](../../serverless-kubernetes/developer-reference/api-cs-2015-12-15-modifyclusternodepool-serverless.md) |
| ACK Edge 集群 | 云端节点池请参见 [创建和管理节点池](create-a-node-pool.md) 边缘节点池请参见 [创建边缘节点池](edge-node-pool-management.md) |
| ACK 灵骏集群 | [灵骏节点池](../../ack-lingjun-managed-clusters/user-guide/overview-of-lingjun-node-pools.md) |
| 容器计算服务 ACS | [节点标签和污点管理](https://help.aliyun.com/zh/cs/user-guide/node-label-and-taint-management) |
安装镜像加速组件。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，单击组件管理。
在组件管理页面的其他区域找到aliyun-acr-acceleration-suite，单击右侧的安装。
在提示对话框中单击确认。
在左侧导航栏，选择工作负载>守护进程集，在守护进程集页面，查看组件守护进程安装详情。
在左侧导航栏，选择工作负载>无状态，在无状态页面查看组件无状态应用安装详情。
当目标组件的容器组数量显示全部启动完成，表示组件安装成功。
## 启用加速镜像
设置镜像仓库访问凭证。
警告
请确保您的镜像拉取密钥权限按最小权限原则配置，仅包含拉取本集群所需业务镜像的权限。更多详情，请参见[授予](https://help.aliyun.com/zh/acr/user-guide/attach-a-custom-policy-to-a-ram-user)[RAM](https://help.aliyun.com/zh/acr/user-guide/attach-a-custom-policy-to-a-ram-user)[用户自定义策略](https://help.aliyun.com/zh/acr/user-guide/attach-a-custom-policy-to-a-ram-user)。
镜像免密插件方式。
若已使用免密插件，且企业版实例的免密配置正确，无需其他操作。
若未使用免密插件，您可使用免密插件，更多信息，请参见[使用免密组件拉取容器镜像](https://help.aliyun.com/zh/acr/use-the-aliyun-acr-credential-helper-component-to-pull-images-without-using-secrets#task-2456294)。
指定镜像拉取凭证Secret的标签方式。
说明
仅镜像加速组件的版本不小于0.2.6支持该方式。
创建kubernetes.io/dockerconfigjson的Secret，并为其打上images.alibabacloud.com/accelerated: true的标签。
kubectl create secret docker-registry <SecretName> --docker-server=<RegistryVpcDomain> --docker-username=<UserName> --docker-password=<Password>kubectl label secrets <SecretName> images.alibabacloud.com/accelerated="true"
添加镜像加速标签。
您可以为应用负载添加镜像加速标签，例如Pod、Deployment等。也可以为ACK或ACK Serverless集群的命名空间设置标签，该命名空间内的所有符合加速条件的应用负载会启用按需加载容器镜像，无需再修改所有符合加速条件的应用负载的YAML文件。根据实际情况选择任一方式添加镜像加速标签。
说明
标签的名称为k8s.aliyun.com/image-accelerate-mode，值为on-demand。
为应用负载添加镜像加速标签。
以下以Pod为例设置标签。执行以下命令，为Deployment管理的Pod设置标签。
kubectl edit deployment <Deployment名称> -n <Deployment命名空间>
在Deployment的YAML描述文件中添加标签k8s.aliyun.com/image-accelerate-mode: on-demand。
apiVersion: apps/v1 kind: Deployment metadata: name: nginx-deployment labels: app: nginx spec: replicas: 1 selector: matchLabels: app: nginx template: metadata: labels: app: nginx # enable on-demand mode k8s.aliyun.com/image-accelerate-mode: on-demand spec: containers: # your ACR instacne image - image: test-registry-vpc.cn-hangzhou.cr.aliyuncs.com/test/nginx:latest name: test command: ["sleep", "3600"]
为命名空间添加镜像加速标签
通过控制台添加镜像加速标签。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择命名空间与配额。
在命名空间页面单击目标命名空间操作列的编辑。
在编辑命名空间对话框中设置标签的变量名称为k8s.aliyun.com/image-accelerate-mode，标签的变量值为on-demand，然后单击确定。
通过命令行添加镜像加速标签。
kubectl label namespaces <YOUR-NAMESPACE> k8s.aliyun.com/image-accelerate-mode=on-demand
设置加速标签后，如果您已完成普通镜像到加速镜像的转换，在相应命名空间内创建和更新Pod时，加速组件会自动将Pod的原始镜像地址替换为加速镜像地址，并添加nodeSelector，将Pod调度到加速节点。
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
