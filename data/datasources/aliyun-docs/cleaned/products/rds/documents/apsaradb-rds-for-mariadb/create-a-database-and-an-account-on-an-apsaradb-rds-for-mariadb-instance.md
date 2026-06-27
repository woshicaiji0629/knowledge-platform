# 创建RDS MariaDB数据库并管理用户账号-云数据库 RDS-阿里云

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mariadb/create-a-database-and-an-account-on-an-apsaradb-rds-for-mariadb-instance

# 创建数据库和账号
本文介绍如何为RDS MariaDB实例创建数据库和账号。
## 账号类型
RDS MariaDB实例支持两种数据库账号：高权限账号和普通账号。您可以在控制台管理所有账号和数据库。
| 账号类型 | 说明 |
| --- | --- |
| 高权限账号 | 只能通过控制台或 API 创建和管理。 一个实例中只能创建一个高权限账号，可以管理所有普通账号和数据库。 开放了更多权限，可满足个性化和精细化的权限管理需求，例如可按用户分配不同表的查询权限。 拥有实例下所有数据库的所有权限。 可以断开任意账号的连接。 |
| 普通账号 | 可以通过控制台、API 或者 SQL 语句创建和管理。 一个实例可以创建多个普通账号，具体的数量与实例内核有关 。 需要手动给普通账号授予特定数据库的权限。 普通账号不能创建和管理其他账号，也不能断开其他账号的连接。 |
## 创建高权限账号
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏中选择账号管理。
单击创建账号。
设置以下参数：
| 参数 | 说明 |
| --- | --- |
| 数据库账号 | 填写账号名称。要求如下： 以字母开头，以字母或数字结尾； 由小写字母、数字或下划线组成； 长度为 2~16 个字符。 说明 如果创建的高权限账号的账号名与已有的普通账号的账号名相同，则原来的普通账号会被替换为该高权限账号。 |
| 账号类型 | 此处选择 高权限账号 。 |
| 新密码 | 设置账号密码。要求如下： 长度为 8~32 个字符。 由大写字母、小写字母、数字、特殊字符中的至少任意三种组成。 特殊字符为!@#$%^&*()_+-= |
| 确认密码 | 再次输入密码。 |
| 备注 | 备注该账号的相关信息，便于后续账号管理。最多支持 256 个字符。 |
单击确定。
## 重置高权限账号
如果高权限账号自身出现问题，比如权限被意外回收（REVOKE ），您可以通过重置账号权限的方法恢复。
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏中，选择账号管理。
单击高权限账号右侧的重置账号权限。
输入高权限账号密码，重置账号权限。
## 创建普通账号
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏中选择账号管理。
单击创建账号。
设置以下参数：
| 参数 | 说明 |
| --- | --- |
| 数据库账号 | 填写账号名称。要求如下： 以字母开头，以字母或数字结尾； 由小写字母、数字或下划线组成； 长度为 2~16 个字符。 |
| 账号类型 | 此处选择 普通账号 。 |
| 授权数据库： | 为该账号授予一个或多个数据库的权限。本参数可以留空，在创建数据库时再给账号 [授权](create-a-database-on-an-apsaradb-rds-for-mariadb-instance.md) 。 从左侧选中一个或多个数据库，单击 添加到右侧。 在右侧框中，为某个数据库选择 读写（DDL+DML） 、 只读 、 仅 DDL 或 仅 DML 。 如果要为多个数据库批量设置相同的权限，则单击右侧框里右上角的按钮，例如 全部设读写（DDL+DML） 。 说明 右上角的按钮会随着点击而变化。例如，单击 全部设读写（DDL+DML） 后，该按钮会变成 全部设只读 。 |
| 新密码 | 设置账号密码。要求如下： 长度为 8~32 个字符。 由大写字母、小写字母、数字、特殊字符中的至少任意三种组成。 特殊字符为!@#$%^&*()_+-= |
| 确认密码 | 再次输入密码。 |
| 备注 | 非必填。备注该账号的相关信息，便于后续账号管理。最多支持 256 个字符。 |
单击确定。
## 创建数据库
访问[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏中，选择数据库管理。
单击创建数据库。
设置以下参数。
| 参数 | 说明 |
| --- | --- |
| 数据库（DB）名称 | 以字母开头，以字母或数字结尾； 由小写字母、数字、下划线或中划线组成； 长度为 2~64 个字符。 |
| 支持字符集 | 数据库的字符集。 |
| 授权账号 | 选中需要访问本数据库的账号。本参数可以留空，在创建数据库后再 [修改或重置账号权限](modify-the-permissions-of-a-standard-account-on-an-apsaradb-rds-for-mariadb-instance.md) 。 说明 此处只会显示 普通账号 ，因为高权限账号拥有所有数据库的所有权限，不需要授权。 |
| 备注说明 | 非必填。用于备注该数据库的相关信息，便于后续数据库管理，最多支持 256 个字符。 |
单击创建。
## 相关API
| API | 描述 |
| --- | --- |
| [CreateAccount](../api-create-an-account.md) | 创建账号 |
| [CreateDatabase](../api-create-database.md) | 创建数据库 |
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
