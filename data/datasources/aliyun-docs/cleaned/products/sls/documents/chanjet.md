# 畅捷通基于日志服务构建智能运维平台替代自建ELK-日志服务-阿里云

Source: https://help.aliyun.com/zh/sls/chanjet

# 畅捷通
日志服务帮助畅捷通运维开发团队解决了误报频繁、 无法快速发现问题站点、无法快速定位异常的问题，实现了运维效率、运维成本、沟通成本等方面的改善。日志服务支撑了畅捷通所有云产品的健康稳定运行，在IT运维开发领域树立了一个标杆。
## 公司简介
畅捷通信息技术股份有限公司是用友旗下成员企业。畅捷通致力于为小微企业提供社交化、个性化、服务化、小量化的生意管理支持。畅捷通针对小微企业财务及管理转型问题，通过技术赋能，助力企业业务在线，改变传统的经营业态，实现利润持续增长。畅捷通充分利用SaaS业务与客户的高频互动的优势深挖客户的价值，从而多方面满足小微企业对云产品的需求。畅捷通未来业务将从SaaS市场拓展到企业业务运营服务的BaaS市场，并致力于成为中国较大的一站式小微企业服务平台。更多信息，请参见[畅捷通](https://www.chanjet.com/)。
## 业务场景
畅捷通IT运维开发部负责畅捷通所有云产品（包括好会计、好生意、易代账等）的生产及测试系统的运维、上线、发布等工作。该部门构建了一套MIDAS智能运维平台，提供了数据接入、数据处理、场景化分析等能力。
## 业务痛点
畅捷通在智能运维平台开发初期，底层使用了自建的ELK进行运维数据分析。随着畅捷通业务的增长接入的应用系统增多，畅捷通很快发现平台出现各种问题，各产品的稳定运行受到极大挑战。
并发量大
几万个点并发发送数据，每天产生的各种日志与消息达到TB级。自建的ELK系统性能较差，优化性能需要耗费大量开发资源。
类型杂
访问类、系统类、应用类、通知类、消息类等等，种类繁多、格式千奇百怪，为数据清洗增加了巨大的难度。
来源多
网络、服务器、移动App、Web、Docker等各种来源的日志，接口繁多，并且要求实时性高，无法集中统一管理。
应用深入
各产品部门对收集来的数据都有着自己个性化的需求，监控报警、问题诊断、分析挖掘、报表等，消费模式也多种多样。
## 解决方案
针对这些问题与调整，畅捷通选择日志服务作为基础来深度打造其智能运维平台。
高效消息采集和传输
畅捷通利用日志服务的强大数据接入能力，将其混合云架构中网络、服务器、移动端、容器的各类访问类、系统类、应用类、消息类等各类日志统一汇入日志服务，实现每天TB级数据的快速处理。
灵活的数据处理和存储
针对内部已经具备完善CMDB和关联规则的情况，畅捷通将原始日志进行语义切分和序列化后，对应到场景分析中。畅捷通在策略组中找到相应的执行策略，再发到外部服务中，用外部服务去调用Ansible或者消息转发等操作，实现数据投递的集中管理，为后续众多场景化分析提供支撑。
智能异常检测和定位
畅捷通通过日志服务的时序数据分析与函数计算能力构建了智能运维平台，通过直接使用同环比函数，可以快速的得出监控指标的当前值，并且具有实时性。有了同环比后，报警的发送会变得准确，与原来的阈值相比准确性大大提高。畅捷通通过日志服务的异常预测函数，从海量指标中快速定位异常，将有问题的地方显示出来，快速发现系统故障。畅捷通通过日志服务将各块汇集过来的数据进行标记后，与应用的配置信息进行关联和整合，通过时序发现故障的根因，从而可以实现故障预测。
畅捷通基于日志服务打造的智能运维平台的架构如下图所示。
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
