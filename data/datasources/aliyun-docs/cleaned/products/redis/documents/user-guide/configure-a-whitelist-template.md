# 使用IP白名单模板统一管理多实例访问-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/user-guide/configure-a-whitelist-template

# 设置IP白名单模板
当您有多个需要设置相同IP白名单的实例时，您可以创建一个IP白名单模板，并将该模板与多个云数据库 Tair（兼容 Redis）实例进行关联，当您需要调整IP白名单时，您仅需要维护一套IP白名单模板，即可对该模板关联的全部实例动态生效，从而简化设置白名单的操作。
## 注意事项
实例仅能关联相同地域下的IP白名单模板，且单个实例可关联多个IP白名单模板。
## 创建与修改IP白名单模板
登录[管理控制台](https://kvstore.console.aliyun.com/)。
在页面左上角，选择目标地域。
在左侧导航栏，单击IP白名单模板。
在页面左上角，单击创建IP白名单模板。
若已创建IP白名单模板，您可以找到目标IP白名单模板，单击操作列的修改。
在右侧弹出的面板中，配置如下参数。
| 配置项 | 说明 |
| --- | --- |
| IP 白名单模板名称 | 根据业务名称、类型等信息，设置 IP 白名单模板的名称，便于后续业务识别。 |
| 白名单内 IP 地址 | 向该 IP 白名单模板中添加 IP 地址或 IP 地址段，以英文逗号（,）分隔，不可重复，上限为 1000 个。 |
| 关联实例 | 在左侧 可选择实例 列表，单击需要关联该 IP 白名单模板的实例。 说明 关联后， 云数据库 Tair（兼容 Redis） 会在目标实例中增加该白名单分组，不会影响实例的原白名单设置。 在右侧 已选择实例 列表，单击目标实例可取消关联。您也可以在实例的白名单设置中，取消关联 IP 白名单模板。 重要 取消关联后， 云数据库 Tair（兼容 Redis） 会在目标实例中移除该白名单分组，该操作会导致对应 IP 地址无法连接该实例，请谨慎操作。 |
单击确定。
在弹出的对话框中，单击确定。
## 删除IP白名单模板
若业务调整，您也可以删除IP白名单模板，但在删除前，您需要先解绑（取消关联）已关联该模板的实例。
登录[管理控制台](https://kvstore.console.aliyun.com/)。
在左侧导航栏，单击IP白名单模板。
在IP白名单模板页面，找到目标IP白名单模板，单击操作列的删除。
在弹出的对话框中，单击删除。
## 相关文档
[设置](configure-whitelists.md)[IP](configure-whitelists.md)[白名单](configure-whitelists.md)
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
