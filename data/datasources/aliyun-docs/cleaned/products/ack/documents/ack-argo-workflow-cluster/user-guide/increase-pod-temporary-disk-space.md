# 为ACSPod扩容临时存储空间EphemeralStorage-容器服务Kubernetes版ACK-阿里云

Source: https://help.aliyun.com/zh/ack/ack-argo-workflow-cluster/user-guide/increase-pod-temporary-disk-space

# 增加ACS Pod临时存储空间大小
ACS Pod默认提供30 GiB的免费的临时存储空间（EphemeralStorage），如果该存储空间大小无法满足需求，可以手动增加临时存储空间大小。
## 计费说明
临时存储空间（EphemeralStorage）如果超出了30 GiB，超出的部分按照云盘价格收取费用。
费用 = 云盘单价 * 增加的临时存储空间容量 * 使用时长。
云盘单价：按照ESSD PL1类型的云盘按量价格进行计费。不同地域下云盘单价不同，具体请参见[块存储价格页](https://www.aliyun.com/price/product#/disk/detail)。
增加的临时存储空间容量：自行声明增加的容量，即超出了30 GiB的容量大小。
使用时长：按秒计算。临时存储空间随ACS Pod一起创建和释放，使用时长与Pod运行时长一致。
## 配置示例
下方示例中为ACS Pod增加20 GiB临时存储空间，总临时存储空间 = 默认30 GiB + 新增20 GiB = 50 GiB。
### 添加Pod Annotation
apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: helloworld-- spec: entrypoint: helloworld templates: - name: helloworld metadata: annotations: alibabacloud.com/extra-ephemeral-storage: "20Gi" # 声明要增加的临时存储空间大小 container: image: mirrors-ssl.aliyuncs.com/busybox:latest command: - sh - -c args: - echo "Hello, world!"; sleep 60;
### 设置Pod resource
apiVersion: argoproj.io/v1alpha1 kind: Workflow metadata: generateName: helloworld-- spec: entrypoint: helloworld templates: - name: helloworld container: image: mirrors-ssl.aliyuncs.com/busybox:latest resources: requests: ephemeral-storage: 50Gi # 声明临时存储空间大小 command: - sh - -c args: - echo "Hello, world!"; sleep 60;
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
