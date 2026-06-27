# 修改或重置实例账号密码-云数据库 Tair（兼容 Redis®）-阿里云

Source: https://help.aliyun.com/zh/redis/user-guide/change-or-reset-the-password

# 修改或重置密码
如果忘记云数据库 Tair（兼容 Redis）实例的密码，或者需要定期更新密码以提高数据安全性，或者创建实例时没有设置密码，您可以通过控制台或API修改实例密码。本文介绍修改实例密码的注意事项、操作步骤、相关API等。
## 注意事项
如果实例的大版本为兼容Redis 4.0或以上版本，但是没有账号管理功能，请[升级小版本](update-the-minor-version.md)后重试。
## 操作步骤
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏，单击账号管理。
单击页面右上角的修改密码。
说明
如果忘记旧密码，您也可以找到目标账号，单击其操作列的重置密码，根据提示重置密码（无需输入旧密码）。
在弹出的对话框中，选择目标账号，填写旧密码和新密码。
密码长度为8~32位。
密码需包含大写字母、小写字母、数字和特殊字符中的至少三种，支持的特殊字符为!@#$%^&*()_+-=。
单击确定。
修改后，密码会立即生效（无需重启实例），不会影响已通过认证的连接，但新连接需使用新密码。
## 相关API
| API 接口 | 说明 |
| --- | --- |
| [ResetAccountPassword](../developer-reference/api-r-kvstore-2015-01-01-resetaccountpassword-redis.md) | 重置实例账号的密码。 |
## 常见问题
Q：云数据库 Tair（兼容 Redis）实例的密码可以为空吗？
A：当实例开启[专有网络免密访问](enable-password-free-access.md)时，在同一专有网络下无需密码即可连接Tair实例。除此之外，连接实例均需要使用账号密码进行鉴权验证，您需要为实例配置账号、密码。
Q：修改密码后，为什么在DMS中报错“WRONGPASS invalid username-password pair”？
A：修改密码后，您需要在DMS的数据库列表中，右键单击目标实例，选择编辑实例，重新填写账号密码。
## 后续步骤
完成重置密码的操作后，您需要将客户端程序中的密码更新为新密码。
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
