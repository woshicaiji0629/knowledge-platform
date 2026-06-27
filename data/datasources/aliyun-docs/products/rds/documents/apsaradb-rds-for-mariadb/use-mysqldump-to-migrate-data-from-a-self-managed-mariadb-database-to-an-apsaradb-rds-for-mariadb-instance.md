# 如何将自建MariaDB数据库迁移上云-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mariadb/use-mysqldump-to-migrate-data-from-a-self-managed-mariadb-database-to-an-apsaradb-rds-for-mariadb-instance

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/rds/documents/apsaradb-rds-for-mariadb/product-overview.md)

- [快速入门](products/rds/documents/apsaradb-rds-for-mariadb/getting-started.md)

- [操作指南](products/rds/documents/apsaradb-rds-for-mariadb/user-guide.md)

- [实践教程](products/rds/documents/apsaradb-rds-for-mariadb/use-cases.md)

- [安全合规](products/rds/documents/apsaradb-rds-for-mariadb/security-and-compliance.md)

- [开发参考](products/rds/documents/apsaradb-rds-for-mariadb/developer-reference.md)

- [服务支持](products/rds/documents/apsaradb-rds-for-mariadb/support.md)

[首页](https://help.aliyun.com/zh)

# 使用mysqldump将自建MariaDB数据库迁移上云

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

您可以通过mysqldump工具将自建MariaDB数据库迁移到RDS MariaDB，本文将介绍详细的操作步骤。

## 背景信息

由于RDS提供的关系型数据库服务与原生的数据库服务完全兼容，因此对用户来说，将原有数据库迁移到RDS实例的过程，与从一个MariaDB服务器迁移到另外一台MariaDB服务器的过程基本类似。

本文以本地Linux7和MariaDB 10.2.4版本为例，演示如何从本地迁移到RDS MariaDB。

## 注意事项

迁移后的表不区分大小写，统一变为小写。

## 前提条件

已对RDS MariaDB实例[设置白名单](products/rds/documents/apsaradb-rds-for-mariadb/configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mariadb-instance.md)和[申请外网地址](products/rds/documents/apsaradb-rds-for-mariadb/apply-for-or-release-a-public-endpoint-for-an-apsaradb-rds-for-mariadb-instance.md)。

## 操作步骤

- 

使用远程工具[登录](products/rds/documents/apsaradb-rds-for-mariadb/connect-to-an-apsaradb-rds-for-mariadb-instance.md)[RDS MariaDB](products/rds/documents/apsaradb-rds-for-mariadb/connect-to-an-apsaradb-rds-for-mariadb-instance.md)[实例](products/rds/documents/apsaradb-rds-for-mariadb/connect-to-an-apsaradb-rds-for-mariadb-instance.md)，创建空数据库（例如test001）。在 MySQL-Front 工具中连接 MariaDB 实例，在SQL编辑器中执行create database test001;创建目标数据库，执行成功后左侧数据库列表中出现test001数据库。

- 

登录本地Linux服务器，使用自带的mysqldump工具将本地数据库数据导出为数据文件。

mysqldump -h localhost -u <本地数据库用户名> -p --opt --default-character-set=utf8 --hex-blob <想要迁移的数据库名> --skip-triggers > /tmp/<想要迁移的数据库名>.sql

示例

说明

下文中的user用户需要具备相关权限，权限设置的详细操作，请参见[权限设置](https://dev.mysql.com/doc/refman/5.7/en/mysqldump.html)。

mysqldump -h localhost -u user -p --opt --default-character-set=utf8 --hex-blob testdb --skip-triggers > /tmp/testdb.sql

重要

导出期间请勿进行数据更新。本步骤仅仅导出数据，不包括存储过程、触发器及函数。

- 

使用mysqldump导出存储过程、触发器和函数。

mysqldump -h localhost -u <本地数据库用户名> -p --opt --default-character-set=utf8 --hex-blob <想要迁移的数据库名> -R | sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' > /tmp/<想要迁移的数据库名>_trigger.sql

示例

mysqldump -h localhost -u user -p --opt --default-character-set=utf8 --hex-blob testdb -R | sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' > /tmp/testdb_trigger.sql

说明

若数据库中没有使用存储过程、触发器和函数，可跳过此步骤。在导出存储过程、触发器和函数时，需要将definer去掉，以兼容RDS。

- 

通过如下命令将数据文件和存储过程文件导入到目标RDS MariaDB实例中。

mysql -h <RDS实例外网地址> -P <RDS实例外网端口> -u <RDS实例高权限账号> -p <RDS上数据库名> < /tmp/<想要迁移的数据库名>.sql mysql -h <RDS实例外网地址> -P <RDS实例外网端口> -u <RDS实例高权限账号> -p <RDS上数据库名> < /tmp/<想要迁移的数据库名>trigger.sql

示例

mysql -h rm-bpxxxxx.mariadb.rds.aliyuncs.com -P 3306 -u testuser -p test001 < /tmp/testdb.sql mysql -h rm-bpxxxxx.mariadb.rds.aliyuncs.com -P 3306 -u testuser -p test001 < /tmp/testdb_trigger.sql

- 

刷新远程工具后查看表，已经有了数据，说明已经迁移成功。

[上一篇：RDS MariaDB实例间的数据迁移](products/rds/documents/apsaradb-rds-for-mariadb/migrate-data-between-apsaradb-rds-for-mariadb-instances.md)[下一篇：使用DTS将自建MariaDB数据库迁移上云](products/rds/documents/apsaradb-rds-for-mariadb/use-dts-to-migrate-the-data-of-a-self-managed-mariadb-database-to-the-cloud.md)

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
