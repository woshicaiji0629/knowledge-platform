# P2P加速拉取镜像-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-edge/user-guide/use-p2p-acceleration-feature

# 使用P2P加速
P2P加速功能可以提升镜像拉取速度，减少应用部署时间。当大规模容器集群批量下载镜像时，您可以使用P2P加速功能提升镜像拉取速度。本文介绍如何使用P2P加速功能提升镜像拉取速度。
## 背景信息
当大规模容器集群批量下载镜像时，容器镜像存储的网络带宽会成为性能瓶颈，导致镜像拉取缓慢。P2P加速功能可以利用您计算节点的带宽资源，进行节点之间的镜像分发，以减少对容器镜像存储的压力，可以大幅提升镜像拉取速度，减少应用部署时间。经过测试，1000节点规模下拉取1 GB大小的镜像，相比普通镜像拉取方式（以带宽为10 Gbps为例），P2P加速方式可以减少95%以上的镜像拉取时间。此外，新版的P2P加速方案相较于旧版的P2P有30%~50%的性能提升，且新版的P2P方案默认支持按需加载容器镜像使用P2P加速，具体操作，请参见[按需加载容器镜像](https://help.aliyun.com/zh/acr/user-guide/load-resources-of-a-container-image-on-demand)。
您可以在以下场景使用P2P加速功能。
ACK集群
IDC或其他云厂商集群
## 前提条件
安装P2P加速套件。
若您需要在ACK集群中使用P2P加速功能。关于如何安装P2P加速套件的具体操作，请参见[在](https://help.aliyun.com/zh/acr/user-guide/use-p2p-acceleration-in-an-ack-cluster)[ACK](https://help.aliyun.com/zh/acr/user-guide/use-p2p-acceleration-in-an-ack-cluster)[集群中安装](https://help.aliyun.com/zh/acr/user-guide/use-p2p-acceleration-in-an-ack-cluster)[P2P](https://help.aliyun.com/zh/acr/user-guide/use-p2p-acceleration-in-an-ack-cluster)[加速套件](https://help.aliyun.com/zh/acr/user-guide/use-p2p-acceleration-in-an-ack-cluster)。
若您需要在IDC或其他云厂商集群中使用P2P加速功能。关于如何安装P2P加速套件的具体操作，请参见[在](https://help.aliyun.com/zh/acr/user-guide/install-p2p-acceleration-suite-in-idc-or-other-cloud-vendor-clusters)[IDC](https://help.aliyun.com/zh/acr/user-guide/install-p2p-acceleration-suite-in-idc-or-other-cloud-vendor-clusters)[或其他云厂商集群中安装](https://help.aliyun.com/zh/acr/user-guide/install-p2p-acceleration-suite-in-idc-or-other-cloud-vendor-clusters)[P2P](https://help.aliyun.com/zh/acr/user-guide/install-p2p-acceleration-suite-in-idc-or-other-cloud-vendor-clusters)[加速套件](https://help.aliyun.com/zh/acr/user-guide/install-p2p-acceleration-suite-in-idc-or-other-cloud-vendor-clusters)。
## 使用限制
开启P2P加速后，P2P加速套件会将您的容器镜像地址通过Webhook替换为P2P的镜像地址，例如，您的原始镜像地址为test****vpc.cn-hangzhou.cr.aliyuncs.com/docker-builder/nginx:latest，替换后的P2P加速镜像地址为test****vpc.distributed.cn-hangzhou.cr.aliyuncs.com:65001/docker-builder/nginx:latest。
同时，Webhook会帮您自动生成一个用于加速镜像地址的镜像拉取密钥（基于原始镜像的镜像拉取密钥复制生成），由于该P2P镜像拉取密钥的创建和P2P镜像地址的替换是异步逻辑，因此建议您在下发工作负载前优先下发容器镜像拉取需要的镜像拉取密钥，或手动创建一个用于P2P镜像拉取（domain为test-registry-vpc.distributed.cn-hangzhou.cr.aliyuncs.com:65001）的镜像拉取密钥，然后再下发工作负载，避免由于镜像地址的替换而导致镜像拉取失败。
## 启用P2P加速
您可以通过添加标签的方式启用P2P加速，可以为应用负载添加P2P加速标签，例如Pod、Deployment等。也可以为ACK集群的命名空间设置P2P加速标签。为命名空间设置P2P加速标签后，该命名空间内的所有符合加速条件的应用负载都会启用P2P加速，无需再修改应用负载的YAML文件。根据实际情况选择任一方式添加P2P加速标签。
说明
标签的名称为k8s.aliyun.com/image-accelerate-mode，值为p2p。
为应用负载添加P2P加速标签。
以下以Deployment为例设置标签。执行以下命令，为Deployment设置标签。
kubectl edit deploy <Deployment名称>
在Deployment文件中添加标签k8s.aliyun.com/image-accelerate-mode: p2p。
apiVersion: apps/v1 kind: Deployment metadata: name: test labels: app: nginx spec: replicas: 1 selector: matchLabels: app: nginx template: metadata: labels: # enable P2P k8s.aliyun.com/image-accelerate-mode: p2p app: nginx spec: # your ACR instacne image pull secret imagePullSecrets: - name: test-registry containers: # your ACR instacne image - image: test-registry-vpc.cn-hangzhou.cr.aliyuncs.com/docker-builder/nginx:latest name: test command: ["sleep", "3600"]
为命名空间添加P2P加速标签
通过控制台添加P2P加速标签。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择命名空间与配额。
在命名空间页面单击目标命名空间操作列的编辑。
在编辑命名空间对话框中，单击+命名空间标签，配置变量名称为k8s.aliyun.com/image-accelerate-mode，变量值为p2p，然后单击确定。
通过命令行添加P2P加速标签。
kubectl label namespaces <YOUR-NAMESPACE> k8s.aliyun.com/image-accelerate-mode=p2p
## 验证P2P加速
启用P2P加速后，P2P组件会自动为Pod注入P2P相关annotation、P2P加速镜像地址以及对应的镜像拉取凭证。
重要
P2P镜像拉取凭证与您原先配置的非P2P镜像地址拉取凭证仅镜像仓库域名不一样，其他凭证信息一致。因此，若您原先镜像拉取凭证用户信息配置错误，也会导致P2P镜像拉取失败。
执行以下命令，查看Pod。
kubectl get po <Pod的名称> -oyaml
预期输出：
apiVersion: v1 kind: Pod metadata: annotations: # inject p2p-annotations automatically k8s.aliyun.com/image-accelerate-mode: p2p k8s.aliyun.com/p2p-config: '...' spec: containers: # inject image to p2p endpoint - image: test-registry-vpc.distributed.cn-hangzhou.cr.aliyuncs.com:65001/docker-builder/nginx:latest imagePullSecrets: - name: test-registry # inject image pull secret for p2p endpoint - name: acr-credential-test-registry-p2p
可以看到，Pod已注入P2P相关annotation、P2P加速镜像地址以及对应的镜像拉取凭证，说明启用P2P加速成功。
## （可选）启用客户端指标采集
### P2P Metrics说明
### 打开Metrics
安装P2P时，打开Metrics配置。
p2p: v2: # Component for P2P v2 image: registry-vpc.__ACK_REGION_ID__.aliyuncs.com/acs/dadi-agent imageTag: v0.1.2-72276d4-aliyun # Concurrency limit number of layers downloading by each node proxy proxyConcurrencyLimit: 128 # The server port to communicate with P2P nodes p2pPort: 65002 cache: # Disk cache capacity in bytes, default 4GB capacity: 4294967296 # Set to 1 if you are using high-performance disks on your ECS, e.g. ESSD PL2/PL3 aioEnable: 0 exporter: # Set to true if you want to collect component metrics enable: false port: 65003 # limit for downstream throughput throttleLimitMB: 512
### 访问方式
P2P YAML中关于exporter字段定义了Metrics的端口。
ExporterConfig: enable: true # 是否开启 port: 65006 # 监听端口 standaloneExporterPort: true # 是否采用独立端口暴露，如果为false，则通过http服务端口吐出
curl 127.0.0.1:$port/metrics可以得到Metrics结果如下。
# HELP DADIP2P_Alive # TYPE DADIP2P_Alive gauge DADIP2P_Alive{node="192.168.69.172:65005",mode="agent"} 1.000000 1692156721833 # HELP DADIP2P_Read_Throughtput Bytes / sec # TYPE DADIP2P_Read_Throughtput gauge DADIP2P_Read_Throughtput{node="192.168.69.172:65005",type="pread",mode="agent"} 0.000000 1692156721833 DADIP2P_Read_Throughtput{node="192.168.69.172:65005",type="download",mode="agent"} 0.000000 1692156721833 DADIP2P_Read_Throughtput{node="192.168.69.172:65005",type="peer",mode="agent"} 0.000000 1692156721833 DADIP2P_Read_Throughtput{node="192.168.69.172:65005",type="disk",mode="agent"} 0.000000 1692156721833 DADIP2P_Read_Throughtput{node="192.168.69.172:65005",type="http",mode="agent"} 0.000000 1692156721833 # HELP DADIP2P_QPS # TYPE DADIP2P_QPS gauge DADIP2P_QPS{node="192.168.69.172:65005",type="pread",mode="agent"} 0.000000 1692156721833 DADIP2P_QPS{node="192.168.69.172:65005",type="download",mode="agent"} 0.000000 1692156721833 DADIP2P_QPS{node="192.168.69.172:65005",type="peer",mode="agent"} 0.000000 1692156721833 DADIP2P_QPS{node="192.168.69.172:65005",type="disk",mode="agent"} 0.000000 1692156721833 DADIP2P_QPS{node="192.168.69.172:65005",type="http",mode="agent"} 0.000000 1692156721833 # HELP DADIP2P_MaxLatency us # TYPE DADIP2P_MaxLatency gauge DADIP2P_MaxLatency{node="192.168.69.172:65005",type="pread",mode="agent"} 0.000000 1692156721833 DADIP2P_MaxLatency{node="192.168.69.172:65005",type="download",mode="agent"} 0.000000 1692156721833 DADIP2P_MaxLatency{node="192.168.69.172:65005",type="peer",mode="agent"} 0.000000 1692156721833 DADIP2P_MaxLatency{node="192.168.69.172:65005",type="disk",mode="agent"} 0.000000 1692156721833 DADIP2P_MaxLatency{node="192.168.69.172:65005",type="http",mode="agent"} 0.000000 1692156721833 # HELP DADIP2P_Count Bytes # TYPE DADIP2P_Count gauge DADIP2P_Count{node="192.168.69.172:65005",type="pread",mode="agent"} 0.000000 1692156721833 DADIP2P_Count{node="192.168.69.172:65005",type="download",mode="agent"} 0.000000 1692156721833 DADIP2P_Count{node="192.168.69.172:65005",type="peer",mode="agent"} 0.000000 1692156721833 DADIP2P_Count{node="192.168.69.172:65005",type="disk",mode="agent"} 0.000000 1692156721833 DADIP2P_Count{node="192.168.69.172:65005",type="http",mode="agent"} 0.000000 1692156721833 # HELP DADIP2P_Cache # TYPE DADIP2P_Cache gauge DADIP2P_Cache{node="192.168.69.172:65005",type="allocated",mode="agent"} 4294967296.000000 1692156721833 DADIP2P_Cache{node="192.168.69.172:65005",type="used",mode="agent"} 4294971392.000000 1692156721833 # HELP DADIP2P_Label # TYPE DADIP2P_Label gauge
### 指标说明
指标名
DADIP2P_Alive：服务是否存活。
DADIP2P_Read_Throughtput：P2P服务吞吐，单位：byte/s。
DADIP2P_QPS：QPS。
DADIP2P_MaxLatency：延迟统计，单位：us。
DADIP2P_Count：流量统计，单位：bytes。
DADIP2P_Cache：单机Cache用量，单位：bytes。
Tag
node：P2P Agent/Root的服务IP和端口。
type：指标类型。
pread：处理下游请求。
download：回源。
peer：P2P网络分发。
disk：处理磁盘。
http：处理HTTP请求。
allocated：缓存分配空间。
used：缓存使用空间。
指标示例
DADIP2P_Count{node="11.238.108.XXX:9877",type="http",mode="agent"} 4248808352.000000 1692157615810 Agent服务累计处理HTTP请求流量：4248808352字节。 DADIP2P_Cache{node="11.238.108.XXX:9877",type="used",mode="agent"} 2147487744.000000 1692157615810 当前Agent缓存用量：2147487744字节。
### 审计日志
开启审计日志
修改p2p configmap里audit字段为true。
DeployConfig: mode: agent logDir: /dadi-p2p/log logAudit: true logAuditMode: stdout # 输出到控制台, file为输出到日志目录/dadi-p2p/log/audit.log
审计日志格式
格式如下，其含义为：从接收到请求至结果返回的处理耗时，单位：us。
2022/08/30 15:44:52|AUDIT|th=00007FBA247C5280|download[pathname=/https://cri-pi840la*****-registry.oss-cn-hangzhou.aliyuncs.com/docker/registry/v2/blobs/sha256/dd/dd65726c224b09836aeb6ecebd6baf58c96be727ba86da14e62835569896008a/data][offset=125829120][size=2097152][latency=267172] .... 2022/08/30 15:44:55|AUDIT|th=00007FBA2EFEAEC0|http:pread[pathname=/https://cri-pi840lacia*****-registry.oss-cn-hangzhou.aliyuncs.com/docker/registry/v2/blobs/sha256/dd/dd65726c224b09836aeb6ecebd6baf58c96be727ba86da14e62835569896008a/data][offset=127467520][size=65536][latency=21]
主要字段为：时间、 AUDIT、线程指针、操作码[pathname=][size=][latency=]。
其中AUDIT和线程指针一般不用关心，size为单次请求大小，若为负数则表示异常；latency为单次请求延迟，单位：us。
常见操作码如下：
http:pread：表示HTTP Proxy处理下游数据请求。
rpc:stat：表示P2P Agent获取文件长度。
rpc:pread：表示P2P Agent处理下游数据请求。
download：表示P2P Agent从上游下载数据。
filewrite：表示P2P Agent写入当前数据分片到缓存。
fileread：表示P2P Agent从缓存读取数据分片。
日志示例
download[pathname=mytest][offset=0][size=65536][latency=26461] ## P2P Agent从上游下载mytest文件[0,65536)这段数据的延迟为26461us rpc:pread[pathname=mytest][offset=0][size=65536][latency=2] ## P2P Agent向下游返回mytest文件[0,65536)这段数据的延迟为2us http:pread[pathname=mytest][offset=0][size=65536][latency=26461] ## 代理向从上游下载mytest文件[0,65536)这段数据的延迟为26461us
## （可选）关闭按需加载镜像使用P2P加速
说明
以下是集群内修改单节点配置的参考步骤。您需关注节点的后续运维操作，是否会覆盖此配置。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择节点管理>节点。
在节点页面，单击目标节点IP地址下的实例ID。
在实例详情页面，使用远程连接，登录节点。
使用vi命令编辑/etc/overlaybd/overlaybd.json文件中的p2pConfig，将enable改为false。
{ "p2pConfig": { "enable": false, "address": "https://localhost:6****/accelerator" }, ... ... }
执行如下命令，重新按需加载的组件。
service overlaybd-tcmu restart
## 附录
### P2P 加速效果参考
不同规格镜像拉取
测试镜像规格如下
4 GB（512 MB * 8层）
10 GB（10 GB * 1层）
20 GB（4 GB * 5层，10 GB * 2层，512 MB * 40层， 20 GB * 1层，2 GB * 10层）
测试环境如下
ACK集群：1000节点
ECS规格：4核8 GB内存
云盘规格：200 GB ESSD PL1
P2P Agent规格：1核1 GB内存，缓存4 GB
测试场景
1000 节点拉取相同镜像（含镜像下载后解压完成）
测试结果（P95耗时）
| 镜像规格 | 耗时 | 回源（Bucket）峰值吞吐（Gbps） |
| --- | --- | --- |
| 512 MB * 8 层 | 116 秒 | 2 |
| 10 GB * 1 层 | 6 分 20 秒 | 1.2 |
| 4 GB * 5 层 | 9 分 15 秒 | 5.1 |
| 10 GB * 2 层 | 9 分 50 秒 | 6.7 |
| 512 MB * 40 层 | 7 分 55 秒 | 3.8 |
| 20 GB * 1 层 | 11 分 | 2.5 |
| 2 GB * 10 层 | 8 分 13 秒 | 3.2 |
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
