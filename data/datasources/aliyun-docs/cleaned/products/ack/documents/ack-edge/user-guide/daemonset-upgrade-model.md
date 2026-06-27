# 配置DaemonSet扩展升级模型解决升级阻塞和OTA升级-容器服务Kubernetes版ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/daemonset-upgrade-model

# 配置DaemonSet升级模型以解决升级阻塞以及OTA升级问题
在边缘计算场景中，原生的DaemonSet升级模型无法满足某些特定的需求，例如，由于云边网络中断，节点NotReady而导致的DaemonSet滚动升级被阻塞，或者需要根据实际边缘环境的状态在边缘节点上直接触发应用的升级，而不由云端驱动（例如新能源汽车的OTA升级）。此时，可以通过配置扩展的DaemonSet升级模型AdvancedRollingUpdate和OTA以解决云边网络中断导致的升级阻塞以及OTA升级问题。
## 前提条件
适用于v1.26.3-aliyun.1及以上版本的ACK Edge集群。
## 升级模型说明
AdvancedRollingUpdate升级模型
该升级模型解决云边网络断链时，由于节点状态NotReady而导致的DaemonSet升级阻塞问题。在升级过程中，它会忽略NotReady状态的节点，优先完成状态为Ready的节点上的Pod升级。同时，当节点状态从NotReady转变为Ready时，它会自动完成该节点上DaemonSet Pod的升级。
OTA升级模型
该升级模型允许直接在边缘节点上通过调用REST API来检查Pod是否可以更新，以及触发Pod的升级操作。
## 配置说明
apiVersion: apps/v1 kind: DaemonSet metadata: annotations: apps.openyurt.io/update-strategy: AdvancedRollingUpdate apps.openyurt.io/max-unavailable: 30% spec: updateStrategy: type: OnDelete
| 参数 | 说明 |
| --- | --- |
| apps.openyurt.io/update-strategy | 启用扩展升级模型，支持 AdvancedRollingUpdate 或 OTA。 |
| apps.openyurt.io/max-unavailable | 此配置仅在 AdvancedRollingUpdate 模式下生效。定义高级滚动升级过程中最大不可用 Pod 的数量，此注解的值与原生 DaemonSet 的 maxUnavailable 配置相同。如果未指定，则默认值为 10% 。 |
| spec.updateStrategy.type | 必须设置为 OnDelete ，即需要手动删除旧的 Pod 以触发新版本的 Pod 的创建。 |
## 使用方式
### AdvancedRollingUpdate升级模型
以下示例代码为AdvancedRollingUpdate升级示例，在示例中创建了一个名为nginx-daemonset的DaemonSet，使用AdvancedRollingUpdate升级模型，并且在滚动升级过程中最多允许30%的Pod不可用。
cat <<EOF | kubectl apply -f - apiVersion: apps/v1 kind: DaemonSet metadata: name: nginx-daemonset annotations: apps.openyurt.io/update-strategy: AdvancedRollingUpdate apps.openyurt.io/max-unavailable: 30% spec: selector: matchLabels: app: nginx updateStrategy: type: OnDelete template: metadata: labels: app: nginx spec: containers: - name: nginx image: nginx:1.19.4 EOF
### OTA升级模型
OTA升级接口
边缘节点上的edge-hub组件提供了与OTA升级相关的REST APIs。
GET /pods
通过此接口可以获取节点上的Pod信息。可以通过Pod.status.conditions中的PodNeedUpgrade来检查Pod是否可以更新。
POST /openyurt.io/v1/namespaces/{ns}/pods/{podname}/imagepull
此接口允许用户触发特定的DaemonSet Pod的镜像拉取。路径参数{ns}和{podname}分别代表 Pod 的命名空间和名称。一些Pod镜像体积较大、启动时间长，可通过这个API进行预拉取，加速启动时间。
镜像拉取的接口仅支持集群为1.32-aliyun.1及以上的版本。
POST /openyurt.io/v1/namespaces/{ns}/pods/{podname}/upgrade
通过此接口允许触发特定的DaemonSet Pod的更新。路径参数{ns}和{podname}分别代表Pod的命名空间和名称。请根据实际需求对指定的Pod执行升级操作。
OTA升级使用示例
创建一个名为nginx-daemonset的DaemonSet，使用OTA升级模型，当DaemonSet的镜像更新后，节点上的Pod并不会自动更新，请在边缘节点上通过REST API来检查和触发Pod的升级。
cat <<EOF | kubectl apply -f - apiVersion: apps/v1 kind: DaemonSet metadata: name: nginx-daemonset annotations: apps.openyurt.io/update-strategy: OTA spec: selector: matchLabels: app: nginx updateStrategy: type: OnDelete template: metadata: labels: app: nginx spec: containers: - name: nginx image: nginx:1.19.4 EOF
OTA升级用例
登录边缘节点，查看节点上的所有Pod是否有升级需求。
curl http://127.0.0.1:10267/pods
若输出结果中default/nginx-daemonset-bwzss pod.Status.Conditions的PodNeedUpgrade=true，表明对应的Pod需要升级。
（可选）预拉取镜像。
curl -X POST http://127.0.0.1:10267/openyurt.io/v1/namespaces/default/pods/nginx-daemonset-bwzss/imagepull
预期输出：
Image pre-pull requested for pod default/nginx-daemonset-bwzss
对该Pod进行升级并更新DaemonSet配置。
curl -X POST http://127.0.0.1:10267/openyurt.io/v1/namespaces/default/pods/nginx-daemonset-bwzss/upgrade
预期输出：
Start updating pod default/nginx-daemonset-bwzss
## 相关文档
如需确认Pod运行状态，请参见[管理容器组（Pod）](../../ack-managed-and-ack-dedicated/user-guide/manage-pods.md)。
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
