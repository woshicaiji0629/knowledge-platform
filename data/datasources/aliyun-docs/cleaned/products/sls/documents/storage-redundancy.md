# 存储冗余类型对比与选择-日志服务-阿里云-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/storage-redundancy

# 存储冗余
日志服务提供本地冗余存储和同城冗余存储两种类型，覆盖单可用区到多可用区的数据冗余机制，确保数据持久性和可用性。
## 地域说明
同城冗余存储（ZRS）在具备多个可用区（2 AZ，3 AZ）的地域中支持。单 AZ 地域仅支持本地冗余存储（LRS）。详见下表：
| 地域 | 地域编号 | 可用区数量 |
| --- | --- | --- |
| 日本（东京） | ap-northeast-1 | 3az |
| 韩国（首尔） | ap-northeast-2 | 2az |
| 新加坡 | ap-southeast-1 | 3az |
| 马来西亚（吉隆坡） | ap-southeast-3 | 3az |
| 印度尼西亚（雅加达） | ap-southeast-5 | 2az |
| 菲律宾（马尼拉） | ap-southeast-6 | 2az |
| 泰国（曼谷） | ap-southeast-7 | 2az |
| 华北 2（北京） | cn-beijing | 3az |
| 华北 2 金融云 | cn-beijing-finance-1 | 3az |
| 西南 1（成都） | cn-chengdu | 2az |
| 华东 6（福州） | cn-fuzhou | 单 az |
| 华南 3（广州） | cn-guangzhou | 2az |
| 华东 1（杭州） | cn-hangzhou | 3az |
| 华东 1 金融云 | cn-hangzhou-finance | 3az |
| 华南 2（河源） | cn-heyuan | 2az |
| cn-heyuan-acdr-1 | cn-heyuan-acdr-1 | 单 az |
| 中国香港 | cn-hongkong | 3az |
| 华北 5（呼和浩特） | cn-huhehaote | 单 az |
| 华东 5（南京） | cn-nanjing | 单 az |
| 华北 1（青岛） | cn-qingdao | 2az |
| 华东 2（上海） | cn-shanghai | 3az |
| 华东 2 金融云 | cn-shanghai-finance-1 | 3az |
| 华南 1（深圳） | cn-shenzhen | 3az |
| 华南 1 金融云 | cn-shenzhen-finance | 3az |
| 华北 6（乌兰察布） | cn-wulanchabu | 3az |
| 华北 3（张家口） | cn-zhangjiakou | 3az |
| 德国（法兰克福） | eu-central-1 | 2az |
| 英国（伦敦） | eu-west-1 | 2az |
| 沙特（利雅得） | me-central-1 | 单 az |
| 阿联酋（迪拜） | me-east-1 | 2az |
| 美国（弗吉尼亚） | us-east-1 | 2az |
| 美国（亚特兰大） | us-southeast-1 | 2az |
| 美国（硅谷） | us-west-1 | 2az |
## 本地冗余存储（LRS）
采用单可用区（AZ）内的数据冗余存储机制，将用户的数据冗余存储在同一个可用区内多个设施的多个设备上。本地冗余存储能确保硬件失效时的数据持久性和可用性。
重要
本地冗余存储类型的数据冗余在某个特定的地域内。当该地域不可用时，会导致相关数据不可访问。
## 同城冗余存储（ZRS）
采用多可用区（AZ）内的数据冗余存储机制，将用户的数据冗余存储在同一地域（Region）的多个可用区。当某个可用区不可用时，同城冗余存储仍然能够保障数据的正常访问。
当发生断网、断电或者灾难事件导致某个机房不可用时，日志服务仍能继续提供强一致性的服务。整个故障切换过程用户无感知、数据不丢失，满足关键业务系统对于访问快速恢复（分钟级）以及恢复点目标（RPO）等于 0 的需求。
## 存储冗余类型对比
本地冗余存储和同城冗余存储的服务可用性和价格对比如下。
| 存储冗余类型 | 服务可用性 | 价格 |
| --- | --- | --- |
| 本地冗余存储 | 99.9% | 存储空间-日志存储 0.0115 元/GB/天 存储空间-日志低频存储 0.005 元/GB/天 存储空间-日志归档存储 0.0017 元/GB/天 |
| 同城冗余存储 | 99.95% | 存储空间-日志存储 0.0115 元/GB/天 存储空间-日志低频存储 0.005 元/GB/天 存储空间-日志归档存储 0.0017 元/GB/天 |
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
