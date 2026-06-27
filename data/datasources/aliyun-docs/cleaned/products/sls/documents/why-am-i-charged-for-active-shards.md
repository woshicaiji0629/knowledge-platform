# 为什么会产生活跃Shard租用费用-日志服务(SLS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/sls/why-am-i-charged-for-active-shards

# 为什么会产生活跃Shard租用费用？
当您的活跃Shard租用量超过免费额度时，就会产生活跃Shard租用费用。
## 租用费用
日志服务使用活跃Shard，即读写状态的Shard，来控制读写能力。日志服务根据您的活跃Shard租用量收取费用。活跃Shard租用量取决于您租用的活跃Shard数量及其租用时间。
## 计费示例
重要
活跃Shard租用价格，请参见[产品定价](https://www.aliyun.com/price/product?spm=a2c4g.11186623.2.11.66cd2aab6wAn6p#/sls/detail)。
您在创建LogStore时，日志服务默认预留两个Shard。更多信息，请参见[管理](manage-a-logstore.md)[LogStore](manage-a-logstore.md)。
## 按量计费
按量计费模式下，每月活跃Shard租用免费额度31（个*天）。
如果每天活跃Shard数量为1，则可以用31天。
如果每天活跃Shard数量为2，2个*15天=30（个*天）<31（个*天），当月前15天为免费使用，第16天开始产生活跃Shard租用费用。
如果每天活跃Shard数量为4，4个*7天=28（个*天）<31（个*天），当月前7天为免费使用，第8天开始产生活跃Shard租用费用。
## 包年包月
包年包月模式下，日志服务不提供活跃Shard租用免费额度，因此每天都会产生活跃Shard租用费用。
## 成本节约
每个Shard支持5 MB/s的数据写入和10 MB/s的数据读取。当数据流量未达到Shard的最大读写能力时，建议您合并Shard从而节约成本。合并后的Shard为非活跃状态，不收取活跃Shard租用费用。如何合并Shard，请参见[合并](manage-shards.md)[Shard](manage-shards.md)。
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
