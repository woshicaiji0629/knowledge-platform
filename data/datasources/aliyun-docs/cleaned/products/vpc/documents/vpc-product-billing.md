# 产品计费-专有网络VPC(VPC)-阿里云帮助中心

Source: https://help.aliyun.com/zh/vpc/vpc-product-billing

# 产品计费
VPC本身是免费的，但VPC提供的对等连接、流量镜像、流日志功能，以及在VPC中创建其他产品资源，会收取费用。
## 计费概述
收费功能：VPC对等连接、流日志、流量镜像。
公测功能，当前公测期间免费使用：IP地址管理（IPAM）、高可用虚拟IP（HaVip）。
免费功能：
VPC与交换机、附加网段、预留网段
DNS主机名、DHCP选项集
路由表、前缀列表
共享VPC
ClassicLink、网关终端节点
IPv4网关、网络ACL
如果您在VPC中创建了云产品资源，或使用过程中产生存储、传输流量，您需要为其付费。详情可参考对应资源的计费文档。
## VPC对等连接计费说明
同地域VPC对等连接：两端VPC属于同账号或跨账号，均不收取任何费用。
跨地域VPC对等连接：统一由[云数据传输](https://help.aliyun.com/zh/cdt/product-overview/what-is-cdt)[CDT](https://help.aliyun.com/zh/cdt/product-overview/what-is-cdt)按出向流量收取[流量传输费](https://help.aliyun.com/zh/cdt/inter-region-data-transfers)。
计费单价根据地域到地域粒度、链路类型来确定。支持铂金、金两种链路类型，提供不同质量的流量传输服务。
铂金（服务可用性承诺：99.995%）：适用于对链路抖动、链路时延非常敏感，对链路质量要求较高的业务。例如证券交易、在线语音、视频会议、实时游戏等。
金（服务可用性承诺：99.95%）：适用于对链路质量不敏感的业务。例如数据同步、文件传输等。
计费周期为每小时。如果在计费周期内切换链路类型，将按照较高服务等级的单价进行计费。
### 流量计费价格表
地域A到地域B的价格与地域B到地域A的价格相同。
服务等级：金
|  | 流入地域 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 流出地域 | 中国内地 | 亚太 | 欧洲 | 北美 | 南美 | 中东 |
| 中国内地 | 0.48 元/GB | 5.6 元/GB | 5.6 元/GB | 5.6 元/GB | 5.6 元/GB | 5.6 元/GB |
| 亚太 | 5.6 元/GB | 0.525 元/GB | 0.525 元/GB | 0.525 元/GB | 2.5 元/GB | 2.5 元/GB |
| 欧洲 | 5.6 元/GB | 0.525 元/GB | 0.131 元/GB | 0.35 元/GB | 2.5 元/GB | 2.5 元/GB |
| 北美 | 5.6 元/GB | 0.525 元/GB | 0.35 元/GB | 0.131 元/GB | 2.5 元/GB | 2.5 元/GB |
| 南美 | 5.6 元/GB | 2.5 元/GB | 2.5 元/GB | 2.5 元/GB | 2.5 元/GB | 2.5 元/GB |
| 中东 | 5.6 元/GB | 2.5 元/GB | 2.5 元/GB | 2.5 元/GB | 2.5 元/GB | 2.5 元/GB |
服务等级：铂金
|  | 流入地域 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 流出地域 | 中国内地 | 亚太 | 欧洲 | 北美 | 南美 | 中东 |
| 中国内地 | 0.72 元/GB | 8.4 元/GB | 8.4 元/GB | 8.4 元/GB | 8.4 元/GB | 8.4 元/GB |
| 亚太 | 8.4 元/GB | 0.788 元/GB | 0.788 元/GB | 0.788 元/GB | 3.75 元/GB | 3.75 元/GB |
| 欧洲 | 8.4 元/GB | 0.788 元/GB | 0.197 元/GB | 0.525 元/GB | 3.75 元/GB | 3.75 元/GB |
| 北美 | 8.4 元/GB | 0.788 元/GB | 0.525 元/GB | 0.197 元/GB | 3.75 元/GB | 3.75 元/GB |
| 南美 | 8.4 元/GB | 3.75 元/GB | 3.75 元/GB | 3.75 元/GB | 3.75 元/GB | 3.75 元/GB |
| 中东 | 8.4 元/GB | 3.75 元/GB | 3.75 元/GB | 3.75 元/GB | 3.75 元/GB | 3.75 元/GB |
## 流日志计费说明
### 计费项
流日志的计费项由流日志生成费、日志服务的服务费、流量分析器的流量处理费和流量分析存储费组成。
流日志生成费：
计费周期与出账周期均为1小时。账单出账时间通常在当前计费周期结束后3~4小时左右，具体以系统实际出账时间为准。
流日志生成费按照每月每地域生成的日志量实行阶梯累积计费。每个阿里云账号（主账号）在每个地域每月拥有5 GB免费额度。
| 流日志生成量阶梯（每月） | 定价（ 元/GB ） |
| --- | --- |
| 0 TB~10 TB（含） | 2.5 |
| 10 TB~30 TB（含） | 1.25 |
| 30 TB~50 TB（含） | 0.5 |
| 大于 50 TB | 0.25 |
日志服务的服务费：流日志投递到SLS之后产生，由SLS产品计费。收取[写入和存储等费用](../../sls/documents/billing-overview.md)。
SLS提供2种计费模式：“按写入数据量计费”和“按使用功能计费”。在VPC控制台创建流日志并选择新建Logstore时，默认使用“按使用功能计费”模式。
流量分析器计费：流日志投递到流量分析器之后产生，由NIS产品计费。收取[流量分析处理费和流量分析存储费](https://help.aliyun.com/zh/nis/product-overview/billing-method-new-version)。
### 计费示例
示例1
假设您于2022年09月01日00:00:00在某地域启用流日志功能，至2022年10月01日00:00:00期间，共向日志服务投递3 GB日志。
由于每个阿里云账号（主账号）每月有5 GB流日志生成费的免费额度，当月流日志的总费用=日志服务的服务费。
示例2
假设您于2022年09月01日00:00:00在华东2（上海）启用流日志功能，至2022年10月01日00:00:00期间，共向日志服务投递100 GB日志。
当月流日志的生成费=(100－5)×2.5=237.5元，总费用=237.5元＋日志服务的服务费
示例3
假设您于2022年09月01日00:00:00在华北2（北京）启用流日志功能，至2022年10月01日00:00:00期间，共向日志服务投递60 TB日志。
流日志的生成费按照阶梯定价计费：
0至10 TB（含）：(10×1024－5)×2.5=25587.5元
10 TB至30 TB（含）：20×1024×1.25=25600元
30 TB至50 TB（含）：20×1024×0.5=10240元
大于50 TB：10×1024×0.25=2560元
当月流日志生成费合计：25587.5+25600+10240+2560=63987.5元，总费用=63987.5元＋日志服务的服务费
### 欠费与充值
如果您开启了余额预警，当账号余额小于设定的预警值时将给予短信或邮件提醒。
欠费后如果在延停权益额度内，您的服务将不会受到停止影响，实例会继续运行。
阿里云提供[延期免停权益](https://help.aliyun.com/zh/user-center/exemption-of-suspension-after-delinquency)，即当按量付费的资源发生欠费后，提供一定额度或时长继续使用云服务的权益，延停期间正常计费。
欠费后如果超出了延停权益额度，服务将自动停止。实例停止后，不能对VPC流日志实例进行任何操作，计费也将停止。
在实例停止后7天内[充值](https://help.aliyun.com/zh/document_detail/37107.html)补足欠费后，服务会自动开启，可以继续使用。
如果实例停止7天仍未补足欠款，VPC流日志实例会被自动释放。实例被释放后相关配置和数据将被删除，不可恢复。
## 流量镜像计费说明
### 计费项
流量镜像费用 = 实例费 + 流量处理费
实例费 = 启动镜像会话的镜像源个数（个） × 镜像会话活跃时长（小时） × 实例费单价（元/个/小时）
流量处理费 = 镜像流量总量（GB） × 流量处理费单价（元/GB）
| 计费项 | 单价 |
| --- | --- |
| 实例费 | 0.1（元/个/小时） |
| 流量处理费 | 0.05（元/GB） |
### 计费规则
2027年03月31日前，免收流量处理费。
镜像源启动镜像会话后，每个启用了镜像会话的镜像源按小时付费，不足1小时按1小时计费。
单个镜像源创建了多个镜像会话，实例费仅收取一次。镜像会话活跃时长按照镜像源在每个镜像会话中累计的活跃时长计算。例如，镜像源在镜像会话1中活跃时长为5小时，在镜像会话2中活跃时长为4小时，计费时镜像会话活跃时长为9小时。
### 计费示例
例如，一个VPC中有5个弹性网卡实例启用了镜像会话，镜像会话的活跃时间为30天，每天24小时，镜像流量总量为20 GB。详细费用计算如下：
实例费 =5 × 30 × 24 × 0.1 = 360 元
流量处理费 =20 × 0.05 = 1 元
流量镜像总费用 =360 + 1 = 361 元
### 欠费与充值
欠费后如果在延停权益额度内，流量镜像功能不会受到停服影响。
阿里云提供[延期免停权益](https://help.aliyun.com/zh/user-center/exemption-of-suspension-after-delinquency)，即当按量付费的资源发生欠费后，提供一定额度或时长继续使用云服务的权益，延停期间正常计费。
欠费后如果超出了延停权益额度，流量镜像功能停止工作，已开启的镜像会话自动关闭。
如果在流量镜像功能停止15天内[充值](https://help.aliyun.com/zh/document_detail/37107.html)并补足欠费后，服务会自动开启，您可以继续使用流量镜像服务，被停止的镜像会话会自动恢复。
如果流量镜像功能停止15天仍未及时充值，镜像会话实例会被删除。实例被删除后相关配置和数据将被删除，不可恢复。
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
