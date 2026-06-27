# 欠费预警停服影响与恢复服务-CDN-阿里云

Source: https://help.aliyun.com/zh/cdn/product-overview/overdue-payments

# 欠费说明
通过本文您可以详细了解CDN停服原因和收到费用预警提示的原因。
## 欠费停服说明
当您账号的可用额度（含阿里云账户余额、代金券、优惠券等）无法结清待结算的账单时，您的账号会立即进入欠费状态。
欠费通知
您的账号进入欠费状态后，系统会立即以站内信、短信及邮件的方式提醒您尽快支付账单。
停止服务
账号欠费后，没有启用延停权益或超过延停权益额度的用户，CDN会立即停止加速服务。
说明
阿里云提供延期免停权益，如果您开启了该服务，当您的账户欠费后，阿里云会根据您的客户等级或历史消费等因素，提供一定额度或时长继续使用云服务的权益，每个月自动计算并更新。更多信息，请参见[延期免停权益](https://help.aliyun.com/zh/user-center/exemption-of-suspension-after-delinquency)。
账号欠费停服后，CDN会立即停止加速服务，加速域名将会被执行下线（Offline）操作，并且加速域名对应的CNAME域名将被解析到无效地址offline.***.com，加速域名将无法被访问。
说明
域名下线详情请参见[关于域名下线（Offline）规则调整的公告](rules-for-disabling-accelerated-domain-names.md)。
账号欠费并且触发CDN停服后，您账号下的CDN域名在节点上所占用的缓存资源将被释放，CDN域名的配置信息将会保留不超过30天。
结清欠款，恢复服务
您可以在[费用中心](https://usercenter2.aliyun.com/home)查看账户的欠费信息，并通过充值来核销欠款。账号结清欠款后，CDN产品将会恢复服务。之前因为账户欠费而被下线，处于Offline状态的域名会自动上线并恢复加速服务。
需要注意，如果您账号下的CDN域名配置已经被系统删除，当您结清欠款之后，需要重新添加您需要的域名配置信息，并且CDN节点也需要重新下载和缓存源站的资源。
## 费用预警提示
如果您的CDN服务处于以下几种情况，您会收到预警提示信息。
按流量计费：系统根据CDN服务最近7小时的账单应付金额的平均值来判断您的账户余额是否足以支付CDN服务下三个账期的费用。如果不足以支付，系统将以站内信、短信及邮件的方式提醒您。
按峰值带宽计费：系统根据CDN服务最近一个计费周期（天）的账单应付金额值来判断您的账户余额是否足以支付CDN服务下一个计费周期（天）的费用。如果不足以支付，系统将以站内信、短信及邮件的方式提醒您。
可用额度预警：如果您开启了[可用额度预警](https://usercenter2.aliyun.com/home)，当账户余额小于您设定的预警值时，系统将给您发送站内信、短信及邮件提醒。
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
