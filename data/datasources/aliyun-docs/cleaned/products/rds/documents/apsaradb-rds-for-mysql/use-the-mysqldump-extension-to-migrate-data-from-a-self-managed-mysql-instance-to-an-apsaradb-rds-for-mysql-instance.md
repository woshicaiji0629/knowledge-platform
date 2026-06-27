# 使用mysqldump迁移MySQL数据-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/use-the-mysqldump-extension-to-migrate-data-from-a-self-managed-mysql-instance-to-an-apsaradb-rds-for-mysql-instance

# 使用mysqldump迁移MySQL数据
当您需要将数据量较小或者允许较长停机时间的自建MySQL迁移至RDS MySQL时，可以使用mysqldump工具轻松实现数据迁移。该工具可以将自建数据库的结构和数据导出到一个包含创建和插入数据SQL语句的文本文件中，从而确保数据的完整性和一致性。
## 前提条件
RDS实例设置白名单、申请外网地址及创建数据库和账号的操作请参见[快速入门](../general-workflow-to-use-apsaradb-rds-for-mysql.md)。
## 背景信息
由于RDS提供的关系型数据库服务与原生的数据库服务完全兼容，所以对用户来说，将原有数据库迁移到RDS实例的过程与从一台MySQL服务器迁移到另一台MySQL服务器的过程基本类似。
说明
DTS工具更方便快捷且能实现平滑迁移，建议您使用[DTS](overview-of-data-migration-methods-2.md)[迁移数据](overview-of-data-migration-methods-2.md)。
mysqldump的更多参数请参见[MySQL](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html)[官方文档](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html)。
## 适用场景
自建MySQL数据库迁移至RDS MySQL或RDS MySQL Serverless实例内。
## 注意事项
默认情况下，自建库迁移到RDS以后表名统一变为小写。您可以通过如下两种方法让RDS MySQL或RDS MySQL Serverless实例区分表名大小写。
在[创建](create-an-apsaradb-rds-for-mysql-instance-1.md)[RDS MySQL](create-an-apsaradb-rds-for-mysql-instance-1.md)[实例](create-an-apsaradb-rds-for-mysql-instance-1.md)或[创建](rds-mysql-serverless.md)[RDS MySQL Serverless](rds-mysql-serverless.md)[实例](rds-mysql-serverless.md)时将表名大小写设置为区分大小写。
已经创建好的实例，可以[设置实例参数](modify-the-parameters-of-an-apsaradb-rds-for-mysql-instance.md)lower_case_table_names的参数值为0以区分表名大小写。
警告
lower_case_table_names参数设置为0后，务必不要再次设置为1，否则可能导致ERROR 1146 (42S02): Table doesn't exist错误，对业务造成严重影响。
RDS MySQL 8.0和8.4版本实例暂不支持修改该参数，请在创建实例时进行设置。
## 操作步骤
本文以Linux系统为例。在macOS的终端或者Windows的命令提示符下也可执行mysqldump命令。
使用mysqldump导出自建数据库的数据、存储过程、触发器和函数。
重要
导出期间请勿进行数据更新，耐心等待导出完成。
下文中的user用户需要具备本文介绍的操作的相关权限。权限设置的详细操作，请参见[权限设置](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html)。
在Linux命令行下导出自建数据库的数据，命令如下：
mysqldump -h 127.0.0.1 -u user -p --opt --default-character-set=utf8 --hex-blob <自建数据库名> --skip-triggers --skip-lock-tables > /tmp/<自建数据库名>.sql
说明
如果需要使用mysqldump导出RDS MySQL数据库的数据，请将命令中的连接地址、账号、密码及数据库名替换为RDS MySQL实例的信息。
示例
mysqldump -h 127.0.0.1 -u user -p --opt --default-character-set=utf8 --hex-blob testdb --skip-triggers --skip-lock-tables > /tmp/testdb.sql
在Linux命令行下导出存储过程、触发器和函数，命令如下：
mysqldump -h 127.0.0.1 -u user -p --opt --default-character-set=utf8 --hex-blob <自建数据库名> -R | sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' > /tmp/<自建数据库名>Trigger.sql
示例
mysqldump -h 127.0.0.1 -u user -p --opt --default-character-set=utf8 --hex-blob testdb -R | sed -e 's/DEFINER[ ]*=[ ]*[^*]*\*/\*/' > /tmp/testdbTrigger.sql
说明
若数据库中没有使用存储过程、触发器和函数，可跳过此步骤。
将导出的两个文件上传到ECS实例上，本例路径为/tmp。
说明
如果自建数据库原本就在ECS实例上，可跳过本步骤。
将导出的文件导入到目标RDS中，命令如下：
mysql -h <RDS实例连接地址> -P <RDS实例端口> -u <RDS实例账号> -p <RDS数据库名称> < /tmp/<自建数据库名>.sql mysql -h <RDS实例连接地址> -P <RDS实例端口> -u <RDS实例账号> -p <RDS数据库名称> < /tmp/<自建数据库名>Trigger.sql
说明
RDS数据库名称需要是RDS实例上已创建的数据库。创建数据库操作，请参见[管理数据库](create-a-database-for-an-apsaradb-rds-for-mysql-instance.md)。
RDS实例账号需要是高权限账号或具有读写权限的账号。
示例
mysql -h rm-bpxxxxx.mysql.rds.aliyuncs.com -P 3306 -u testuser -p testdb < /tmp/testdb.sql mysql -h rm-bpxxxxx.mysql.rds.aliyuncs.com -P 3306 -u testuser -p testdb < /tmp/testdbTrigger.sql
导入成功后[通过](use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[DMS](use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[登录](use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[RDS](use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[数据库](use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)查看数据是否正常。
## 常见问题
Q：OPERATION need to be executed set by ADMIN报错怎么解决？
A：可能是SQL脚本里面包括视图，触发器，存储过程等对象的definer问题，或者含有set global类SQL导致。详情请参见[RDS MySQL](../support/what-do-i-do-if-the-operation-need-to-be-executed-set-by-admin-error-message-is-displayed.md)[出现“OPERATION need to be executed set by ADMIN”报错](../support/what-do-i-do-if-the-operation-need-to-be-executed-set-by-admin-error-message-is-displayed.md)。
Q：Access denied; you need (at least one of) the SUPER privilege(s) for this operation报错怎么解决？
A：SQL脚本里面包括SUPER权限的语句，将相关语句删除再执行。
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
