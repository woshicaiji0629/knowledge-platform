# 使用镜像缓存加速ACS Pod启动-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-argo-workflow-cluster/user-guide/use-imagecache-to-accelerate-acs-pod-startup

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-argo-workflow-cluster/product-overview.md)

- [服务支持](products/ack/documents/ack-argo-workflow-cluster/support.md)

- [实践教程](products/ack/documents/ack-argo-workflow-cluster/use-cases.md)

- [操作指南](products/ack/documents/ack-argo-workflow-cluster/user-guide.md)

[首页](https://help.aliyun.com/zh)

# 使用镜像缓存加速ACS Pod启动

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

使用镜像缓存（ImageCache）创建ACS Pod可以加速拉取镜像，减少ACS Pod的启动耗时。本文介绍镜像缓存的基本功能、创建和使用方式、计费说明等。

## 功能介绍

在运行容器前，ACS Pod需要先拉取指定的容器镜像，但因网络和容器镜像大小等因素，镜像拉取耗时往往成了ACS Pod启动的主要耗时。为加速实例的启动速度，ACS提供镜像缓存功能。通过预先将需要使用的镜像制作成镜像缓存，然后基于该镜像缓存来创建ACS Pod，避免或者减少镜像层的下载，从而提升实例的启动速度。

具体提升速度由 ACS Pod 中使用的容器镜像大小和镜像仓库网络因素等决定。

每个镜像缓存中可以包含一个镜像。镜像缓存状态制作中表示正处于制作镜像缓存阶段。稍等一段时间，当状态变成制作完成后即可支持使用镜像缓存。

具体镜像缓存制作时间与容器镜像大小与配置的网络带宽相关。如果由于网络不通、认证失败、仓库/Tag 不存在等原因，可能会导致超时制作失败。

## 计费说明

### 制作镜像缓存阶段

无镜像缓存制作中转资源费用，地域级别容器镜像缓存 20 个免费。当某个地域超过 20 个免费额度后，收费如下：

容器镜像缓存存储费用= 单价 * 容器镜像缓存大小 * 容器镜像缓存存活时长

- 

单价：0.18 元/GiB/月。

- 

容器镜像缓存大小：对应容器镜像拉取解压后的大小，单位为 GiB。

- 

容器镜像缓存存活时长：容器镜像缓存创建完成后开始计费，直至删除容器镜像缓存后停止计费。

### 使用镜像缓存阶段

此阶段的费用包含使用了镜像缓存的Pod全生命周期加速费用，计费时长与当前 Pod 的运行时长一致。

容器镜像缓存加速费用= 单价 * 容器镜像缓存大小 *n=1∑Pod总数​Podn​运行时长

- 

单价：0.00231 元/GiB/小时

- 

容器镜像缓存大小：对应容器镜像拉取解压后的大小，单位为 GiB。

- 

所有Pod的运行时长总和：当基于容器镜像缓存启动 Pod，则累计 Pod 拉取镜像、启动、运行的全生命周期时长（容器镜像缓存的付费时长与 Pod 自身的计费时长保持一致）。在 T0 小时，如果有 3 个 Pod 基于容器镜像缓存快速拉起，Pod 1 本身计费时长 3600 秒，Pod 2 本身计费时长 3000 秒，Pod 3 本身计费时长 600 秒。则一共加速时长为 3600 + 3000 + 600 = 7200 秒。

## 注意事项

- 

目前 ACS 镜像缓存功能在白名单邀测阶段，可[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请开通。

- 

创建镜像缓存会为用户创建Service Linked Role，因此需要确保调用创建的子账号具有ram:CreateServiceLinkedRole权限。

- 

制作完成后会显示镜像缓存大小，该数值为容器镜像解压缩后完整文件和容器镜像缓存额外索引文件的总大小。镜像缓存目前支持解压前不超过500GiB的镜像制作。

- 

镜像缓存单地域默认配额为200，可[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请提升。

- 

镜像缓存单地域支持最多50个镜像缓存同时进行创建，已创建完成的镜像缓存不计入其中。

- 

目前镜像缓存支持的地域：华北2（北京）、华东2（上海）、华东1（杭州）、华北6（乌兰察布）、华南1（深圳）、中国香港、新加坡。

- 

目前镜像缓存支持的镜像类型：linux/amd64。

- 

目前 GPU 场景镜像缓存支持的卡型：G59、G49E、L20（GN8IS）。

- 

在使用已创建的镜像缓存时，请确保 Pod 和镜像仓库之间的网络连通性。

## 创建镜像缓存

## 控制台

- 

登录[容器计算服务控制台](https://acs.console.aliyun.com)，在左侧导航栏选择镜像缓存。

- 

在镜像缓存页面，单击页面左上角的创建镜像缓存。

- 

参考页面提示完成地域、镜像缓存与访问凭证、网络连通性配置，并确认创建。

创建镜像缓存后，可以通过其制作事件了解镜像缓存的制作过程。

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 配置项 | 说明 | 示例值 |
| --- | --- | --- |
| 地域 | 目前镜像缓存支持的地域。 | 华北 2（北京） |
| 镜像缓存与访问凭证 | 镜像缓存名 ：长度为[2, 128]个英文小写字母、数字或者连字符（-），不能以连字符开始或结尾。 镜像 ：支持从容器镜像服务企业版、容器镜像服务个人版、制品中心选择目标镜像和版本。 访问凭证 ：同账号 ACR 仓库支持自动免密，无需填写访问凭证。若使用非阿里云容器镜像服务 ACR 托管的镜像，需指定 Server 为镜像仓库域名地址，并配置对应的镜像仓库用户名和镜像仓库密码。 | 镜像缓存名： image-cache-***** 镜像： egs-registry.cn-hangzhou.cr.aliyuncs.com/egs/vllm:0.9.0.1-pytorch2.7-cu128-20250612 |
| 网络连通性配置 | 选择以下方式拉取需要被缓存的容器镜像。 公网方式： 为 专有网络 绑定 [公网 NAT 网关](https://vpcnext.console.aliyun.com/nat/cn-hangzhou/nats) ，并为所选 交换机 配置 SNAT 规则。 自动创建或者使用已有的 弹性公网 IP 。 自动创建的弹性公网 IP 将按照实际产生的流量收费，并在镜像缓存创建完成后自动释放，具体收费细则请参见 [计费概述](products/eip/documents/billing-overview.md) 。 VPC 内网方式：推荐将容器镜像上传到相应地域的 [容器镜像服务](https://cr.console.aliyun.com/cn-hangzhou/repositories) [ACR](https://cr.console.aliyun.com/cn-hangzhou/repositories) 企业版实例，通过内网 VPC 地址拉取镜像。 | 请按实际网络信息配置。 |


## OpenAPI

- 

[创建镜像缓存](https://api.aliyun.com/api/acc/2024-04-02/CreateImageCache?params={%22RegionId%22:%22cn-beijing%22})

- 

[删除镜像缓存](https://api.aliyun.com/api/acc/2024-04-02/DeleteImageCache?params={%22RegionId%22:%22cn-beijing%22})

- 

[查询镜像缓存](https://api.aliyun.com/api/acc/2024-04-02/ListImageCaches?params={%22RegionId%22:%22cn-beijing%22})

- 

[查询镜像缓存详细信息](https://api.aliyun.com/api/acc/2024-04-02/GetImageCache?params={%22RegionId%22:%22cn-beijing%22})

## 使用镜像缓存

| Pod 注解 | 说明 |
| --- | --- |
| image.alibabacloud.com/enable-image-cache: "true" | 为 Pod 开启镜像缓存匹配能力。 |


功能开启后，Pod将自动匹配使用最优的镜像缓存：

- 

镜像匹配度：选择镜像名完全匹配的镜像缓存。

- 

创建时间：优先选择创建时间最近且可用的镜像缓存。

- 

在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择工作负载>容器组，然后单击使用YAML创建资源。

- 

使用以下YAML创建Pod并添加注解开启镜像缓存匹配能力。

请确保网络配置和密钥信息能够访问到所配置的镜像仓库，目前支持的imagePullPolicy为Always。apiVersion: v1 kind: Pod metadata: labels: name: hello-pod name: hello-pod annotations: image.alibabacloud.com/enable-image-cache: "true" spec: containers: - image: egs-registry.cn-hangzhou.cr.aliyuncs.com/egs/vllm:0.9.0.1-pytorch2.7-cu128-20250612 # 请替换为实际镜像地址 command: ["/bin/sleep", "infinity"] imagePullPolicy: Always name: hello-pod ports: - containerPort: 8080 protocol: TCP resources: {} securityContext: capabilities: {} privileged: false terminationMessagePath: /dev/termination-log dnsPolicy: ClusterFirst restartPolicy: Always

- 

创建成功后，单击Pod名称进入基本信息页面。开启镜像缓存匹配能力之后，创建的Pod会根据镜像名称尝试匹配镜像缓存，匹配成功的Pod会自动追加当前匹配的镜像缓存的注解。

| 功能 | 参数 | 示例值 | 说明 |
| --- | --- | --- | --- |
| 镜像缓存命中信息 | image.alibabacloud.com/matched-image-caches | [{"imageCacheId":"imc-*****t15xuii6tz*****","size":30}] | 命中的镜像缓存 ID 及大小（GiB）。 |


[上一篇：配置Artifacts](products/ack/documents/ack-argo-workflow-cluster/user-guide/configure-artifacts.md)[下一篇：使用钉钉机器人发送事件通知](products/ack/documents/ack-argo-workflow-cluster/user-guide/send-event-notifications-via-dingtalk-bot.md)

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
