# RDS MariaDB实例间的数据迁移-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mariadb/migrate-data-between-apsaradb-rds-for-mariadb-instances

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

# RDS MariaDB实例间的数据迁移

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

RDS MariaDB支持通过DTS或mysqldump工具实现实例间的数据迁移。

## 方法一：使用DTS

[RDS MariaDB](https://help.aliyun.com/zh/dts/user-guide/migrate-data-between-rds-mariadb-instances)[实例间的迁移](https://help.aliyun.com/zh/dts/user-guide/migrate-data-between-rds-mariadb-instances)

## 方法二：使用mysqldump

下文以MariaDB 10.3版本为例，演示RDS MariaDB实例间的数据迁移。

### 前提条件

- 

本地主机或阿里云ECS实例安装CentOS 7系统并安装MySQL 5.7。

- 

两个RDS MariaDB实例都已[设置白名单](products/rds/documents/apsaradb-rds-for-mariadb/configure-an-ip-address-whitelist-for-an-apsaradb-rds-for-mariadb-instance.md)，放通CentOS 7所在主机或实例的外网IP地址。

- 

两个RDS MariaDB实例都已[申请外网地址](products/rds/documents/apsaradb-rds-for-mariadb/apply-for-or-release-a-public-endpoint-for-an-apsaradb-rds-for-mariadb-instance.md)。

### 操作步骤

- 

使用客户端工具[登录目标](products/rds/documents/apsaradb-rds-for-mariadb/connect-to-an-apsaradb-rds-for-mariadb-instance.md)[MariaDB](products/rds/documents/apsaradb-rds-for-mariadb/connect-to-an-apsaradb-rds-for-mariadb-instance.md)[实例](products/rds/documents/apsaradb-rds-for-mariadb/connect-to-an-apsaradb-rds-for-mariadb-instance.md)，创建空数据库。在目标 RDS MariaDB 实例的数据库管理工具（如 MySQL-Front）中，执行 SQL 语句create database test001;创建目标数据库test001。创建成功后，可在左侧数据库对象树中看到test001节点。

- 

在CentOS 7使用自带的mysqldump工具将源MariaDB实例的数据库导出为数据文件。

mysqldump -h <源实例外网地址> -P <源实例端口> -u <源实例高权限账号> -p<源实例高权限账号密码> --opt --default-character-set=utf8 --hex-blob <要迁移的数据库名称> --skip-triggers > /tmp/<要迁移的数据库名称>.sql

示例

mysqldump -h rm-xxx.mariadb.rds.aliyuncs.com -P 3306 -u test -pTestxxx --opt --default-character-set=utf8 --hex-blob testdb --skip-triggers > /tmp/testdb.sql

重要

导出期间请勿进行数据更新。本步骤仅导出数据，不包括存储过程、触发器及函数。

- 

使用mysqldump导出存储过程、触发器和函数。

mysqldump -h <源实例外网地址> -P <源实例端口> -u <源实例高权限账号> -p<源实例高权限账号密码> --opt --default-character-set=utf8 --hex-blob <要迁移的数据库名称> -R > /tmp/<要迁移的数据库名称>trigger.sql

示例如下：

mysqldump -h rm-xxx.mariadb.rds.aliyuncs.com -P 3306 -u test -pTestxxx --opt --default-character-set=utf8 --hex-blob testdb -R > /tmp/testdbtrigger.sql

说明

若数据库中没有使用存储过程、触发器和函数，可跳过此步骤。

- 

通过如下命令将数据文件、存储过程、触发器和函数导入目标RDS MariaDB实例中。

mysql -h <目的实例外网地址> -P <目的实例端口> -u <目的实例高权限账号> -p<目的实例高权限账号密码> <目的实例数据库名称> < /tmp/<要迁移的数据库名称>.sql mysql -h <目的实例外网地址> -P <目的实例端口> -u <目的实例高权限账号> -p<目的实例高权限账号密码> <目的实例数据库名称> < /tmp/<要迁移的数据库名称>trigger.sql

示例如下：

mysql -h rm-xxx.mariadb.rds.aliyuncs.com -P 3306 -u test2 -pTest2xxx test001 < /tmp/testdb.sql mysql -h rm-xxx.mariadb.rds.aliyuncs.com -P 3306 -u test2 -pTest2xxx test001 < /tmp/testdbtrigger.sql

[上一篇：从RDS MariaDB迁移至RDS MySQL](products/rds/documents/apsaradb-rds-for-mariadb/migrate-data-from-an-apsaradb-rds-for-mariadb-instance-to-an-apsaradb-rds-for-mysql-instance.md)[下一篇：使用mysqldump将自建MariaDB数据库迁移上云](products/rds/documents/apsaradb-rds-for-mariadb/use-mysqldump-to-migrate-data-from-a-self-managed-mariadb-database-to-an-apsaradb-rds-for-mariadb-instance.md)

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
