# 通知发送时段机制及示例-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/periods-for-sending-alert-notifications

# 通知发送时段机制
告警通知的发送时间由行动组中的发送时段决定。您可以通过配置发送时段，自定义告警通知时间。
## 发送时段
满足发送时段的通知被发送，否则取消。详细说明如下：
说明
发送时段基于全局默认日历判断工作日、非工作日、工作时间和非工作时间。更多信息，请参见[修改全局默认日历](modify-the-global-default-calendar.md)。
任意：任何时候都可以通过该渠道发送通知。
工作日：只有在工作日才可以通过该渠道发送通知。
非工作日：只有在非工作日才可以通过该渠道发送通知。
工作时间：只有在工作日的工作时间才可以通过该渠道发送通知。
非工作时间：只有在非工作日或者工作日的非工作时间才可以通过该渠道发送通知。
## 示例1
例如您希望工作时间通过钉钉接收告警通知，非工作时间通过短信接收告警通知。您可以参考如下配置，在行动组中添加两个通知渠道。具体操作，请参见[行动策略](create-an-action-policy.md)。
钉钉渠道：配置发送时段为工作时间。
短信渠道：配置发送时段为非工作时间。
其中钉钉渠道的提醒方式选择所有人，内容模板选择SLS内置内容模板；短信渠道的接收人类型选择静态接收人，内容模板选择SLS内置内容模板。
## 示例2
例如您希望发生严重告警时，工作时间内通过钉钉和邮件接收告警通知，而在非工作时间内除钉钉和邮件渠道外，还通过语音接收告警通知。您可以参考以下配置，添加两个行动组。具体操作，请参见[行动策略](create-an-action-policy.md)。
语音渠道：配置发送时段为非工作时间。
邮件、钉钉渠道：配置发送时段为工作时间。
配置条件节点为告警严重度数值等于严重。语音渠道的接收人类型选择静态接收人，内容模板选择SLS内置内容模板。钉钉渠道的提醒方式选择所有人，内容模板选择SLS内置内容模板。
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
