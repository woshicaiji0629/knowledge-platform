# ACK Edge集群支持通过公网或专线接入，需配置访问域名、路由网段及端口策略以确保边缘节点与云端服务的通信。-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/network-configuration-for-public-network-access

# 公网环境下节点以及网络设备配置
本文适用于ACK Edge集群的边缘节点（云下节点）以公网方式接入阿里云容器服务平台的场景，并列出了需要放通的域名地址及端口。
## 边缘节点需要暴露的端口（入方向）
在ACK Edge集群中，控制面和监控组件需要从云端或其它节点访问边缘节点，您需要在边缘节点的主机网段放通下列端口。
| 协议 | 端口 | 源地址或源地址网段 | 注释 |
| --- | --- | --- | --- |
| TCP | 10250、10255 | 边缘节点的主机网段。 | APIServer 和 MetricsServer 主动访问 Kubelet 端口，由于通过 Raven 组件代理到边缘节点，因此需要放开边缘节点的主机网段。 |
| 9100、9445 | 边缘节点的主机网段。 | Prometheus 主动访问 Node-Exporter 端口，由于通过 Raven 组件代理，因此需要放开边缘节点的主机网段。 |  |
| UDP | 8472 | 边缘节点的主机网段。 | Flannel VXLAN 会采用节点 UDP 8472 端口构建 VXLAN 隧道，因此需要放开边缘节点的主机网段。 |
## 边缘节点需要访问的域名（出方向）
为了确保IDC设备或边缘设备能顺利接入ACK Edge集群，您需要放通下表域名。其中{region}为集群所在地域的Region ID，例如杭州地域为cn-hangzhou。具体各地域所对应的Region ID，请参见[开服地域](../../product-overview/supported-regions.md)。
| 访问对象 | 公网访问域名 | 端口 | 说明 |
| --- | --- | --- | --- |
| 容器服务控制面 | cs-anony.aliyuncs.com cs-anony.{region}.aliyuncs.com | TCP 443（集群版本 ≥ 1.26） TCP 80（集群版本＜1.26） | 容器服务管控地址。 |
| 组件安装包 | aliacs-k8s-{region}.oss-{region}.aliyuncs.com | TCP 443（集群版本 ≥ 1.26） TCP 80 和 443（集群版本＜1.26） | OSS 下载地址。可通过 OSS 下载 edgeadm 、kubelet、CNI、runtime、edgehub 等安装包。 |
| API Server 公网端点 | 通过集群 基本信息 页签查看。 | TCP 6443 | 与 kube-apiserver 交互。 |
| Tunnel-server 公网 SLB（集群版本＜1.26） | 通过集群 Service（服务）资源查看： kube-system/x-tunnel-server-svc | TCP 10262、10263 | 边缘隧道。 |
| Raven 云端网关 SLB | 通过集群 Service（服务）资源查看： kube-system/x-raven-proxy-svc-gw-cloud-xxx kube-system/x-raven-tunnel-svc-gw-cloud-xxx | TCP [10280,10284] UDP 4500 | Raven 隧道。 |
| NTP | ntp1.aliyun.com cn.ntp.org.cn | 与 NTP 协议有关，一般是 UDP 123 端口。 | 时钟同步服务器地址。 接入时若选择配置 selfHostNtpServer 参数为 true ，即已手动完成时间同步，则不需要使用该地址。 |
| 系统组件镜像地址 | dockerauth.{region}.aliyuncs.com 重要 如果地域为 cn-zhangjiakou，此处对应的 Docker 公网访问域名需修改为 dockerauth-{region}.aliyuncs.com。 dockerauth-ee.{region}.aliyuncs.com registry-{region}.ack.aliyuncs.com | TCP 443 | 系统组件镜像需要使用的地址。 |
| 系统工具 | 系统工具在线安装（无需额外域名） net-tools、iproute、chrony（或者 ntpdate）、crontabs、pciutils、socat、ebtables、iptables、conntrack-tools | 不涉及 | 检测待添加节点是否已安装系统工具，如果没有，则会在线安装，具体的访问地址由节点 yum/apt 源配置决定。 如果是 Ubuntu 系统，则采用 apt-get 安装。 如果是 CentOS 系统，则采用 yum 安装。 |
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
