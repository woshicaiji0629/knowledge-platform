# 如何将TokuDB引擎转换为InnoDB引擎-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/the-storage-engine-was-switched-from-tokudb-to-innodb

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/rds/documents/apsaradb-rds-for-mysql/product-overview.md)

- [快速入门](products/rds/documents/apsaradb-rds-for-mysql/getting-started.md)

- [AI能力中心](products/rds/documents/apsaradb-rds-for-mysql/ai-capability-center.md)

- [自研内核AliSQL](products/rds/documents/apsaradb-rds-for-mysql/proprietary-alisql.md)

- [操作指南](products/rds/documents/apsaradb-rds-for-mysql/user-guide.md)

- [实践教程](products/rds/documents/apsaradb-rds-for-mysql/use-cases.md)

- [安全合规](products/rds/documents/apsaradb-rds-for-mysql/security-and-compliance.md)

- [开发参考](products/rds/documents/apsaradb-rds-for-mysql/developer-reference.md)

- [服务支持](products/rds/documents/apsaradb-rds-for-mysql/support.md)

[首页](https://help.aliyun.com/zh)

# 【停售/下线】TokuDB引擎转换为InnoDB引擎

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

RDS MySQL在2019年08月01日后将不再支持TokuDB引擎，本文介绍如何将TokuDB引擎转换为InnoDB引擎。

## 背景信息

由于Percona已经不再对TokuDB提供支持，很多已知BUG无法修正，极端情况下会导致业务受损，因此RDS MySQL在2019年08月01日后将不再支持TokuDB引擎。由于直接进行引擎转换会阻塞DML操作，影响并发，建议您尽快对业务评估后选择以下其中一种方案对引擎进行转换。

## TokuDB引擎下线时间

2019年08月01日

## 适用范围

存储引擎为TokuDB的实例。

说明

您可以使用show engines;命令查看实例当前默认引擎，或者使用show create table <表名>;命令查看表的存储引擎。

## 注意事项

- 

转换存储引擎后空间占用会增大，在操作期间需要预留出的空间大约应为并行操作的TokuDB表容量的2倍。操作期间请随时关注空间使用情况。

- 

转换引擎后，CPU使用率会下降，但IOPS会上升。这是由于数据页没有压缩，所以读取相同的数据量，IOPS会有所上升。

- 

全库迁移时，由于需要切换连接地址，请在业务低峰期进行操作。

- 

全库迁移时，如果变更了数据库版本，建议提前进行兼容性测试。

## 方案建议

- 

实例中的表较小（100M以下），且业务可接受短时阻塞时，可以使用方案一，锁表时间短，而且免去各种工具配置流程。

- 

实例中的表较大（大于5G）时，建议使用方案二或方案三。

- 

实例中的所有表都需要转换时，建议使用方案三或方案四。

- 

切换引擎后请修改实例参数default_storage_engine为InnoDB。

## 方案一

此方案为直接转换引擎，最简单直接，但过程中会全程阻塞DML操作且大表转换时间比较久。

- 

[通过](products/rds/documents/apsaradb-rds-for-mysql/use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[DMS](products/rds/documents/apsaradb-rds-for-mysql/use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[登录](products/rds/documents/apsaradb-rds-for-mysql/use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[RDS](products/rds/documents/apsaradb-rds-for-mysql/use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[数据库](products/rds/documents/apsaradb-rds-for-mysql/use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)。

- 

在上方选择SQL操作>SQL窗口。

- 

执行如下命令：

Alter table test.testfs engine innodb

## 方案二

此方案为使用第三方工具进行转换。支持Online DDL的第三方工具很多，例如Percona开发的[pt-osc](https://www.percona.com/doc/percona-toolkit/LATEST/pt-online-schema-change.html)、Git-hub开发的[gh-ost](https://github.com/github/gh-ost)等，这里以gh-ost为例进行转换说明，详细说明请参见[gh-ost](https://github.com/github/gh-ost/blob/master/README.md)。

原理说明

gh-ost进行转换的基本原理是新建一个与原表结构相同的临时表，然后同步原表数据，全量完成后通过模拟Slave进程读取Binlog，实时同步数据到临时表。最后在业务低峰时间段重命名表进行切换。此方案主要压力来自全量数据初始化时的IO，但是可以通过修改参数限制IO。

- 

优点：机动性强，可以自定义时间，同步过程可控。

- 

缺点：每一个表都要用命令同步一次，如果表很多的话操作比较繁琐。

参数说明

| 参数 | 说明 |
| --- | --- |
| --initially-drop-old-table | 检查并删除已经存在的旧表。 |
| --initially-drop-ghost-table | 检查并删除已经存在的 ghost 中间表。 |
| --aliyun-rds | 在阿里云 RDS 上执行。 |
| --assume-rbr | 设置 gh-ost 为 rbr binlog 模式。 |
| --allow-on-master | 在主库上执行 gh-ost。 |
| --assume-master-host | 主库的地址。 |
| --user | 数据库账号名称。 |
| --password | 数据库密码。 |
| --host | 连接地址，与主库地址相同即可。 |
| --database | 数据库名称。 |
| --table | 表名。 |
| --alter | 操作语句。 |
| --chunk-size | 行拷贝的 batch 大小。 |
| --postpone-cut-over-flag-file | 切换文件。指定时间删除此文件立刻进行表切换。 |
| --panic-flag-file | 生成此文件，ghost 进程立刻停止。 |
| --serve-socket-file | 用于接收交互命令。 |
| --execute | 直接执行。 |


前提条件

- 

已在本地主机或ECS安装gh-ost。

- 

已在RDS实例的IP白名单中添加本地主机或ECS的IP。

操作步骤

- 

在本地主机或ECS上执行如下命令进行转换，等待转换完成。

gh-ost --user="test01" --password="Test123456" --host="rm-bpxxxxx.mysql.rds.aliyuncs.com" --database="test" --table="testfs" --alter="engine=innodb" --initially-drop-old-table --initially-drop-ghost-table --aliyun-rds --assume-rbr --allow-on-master --assume-master-host="rm-bpxxxxx.mysql.rds.aliyuncs.com" --chunk-size=500 --postpone-cut-over-flag-file="/tmp/ghostpost.postpone" --panic-flag-file="/tmp/stop.flag" --serve-socket-file="/tmp/ghost.sock" --execute

- 

[通过](products/rds/documents/apsaradb-rds-for-mysql/use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[DMS](products/rds/documents/apsaradb-rds-for-mysql/use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[登录](products/rds/documents/apsaradb-rds-for-mysql/use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[RDS](products/rds/documents/apsaradb-rds-for-mysql/use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[数据库](products/rds/documents/apsaradb-rds-for-mysql/use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)。

- 

在左侧查看表，会发现存在以_gho、_ghc结尾的临时表。

- 

执行rm /tmp/ghostpost.postpone命令开始切换表。结果如下。

说明

请忽略显示的error（错误），实际已经切换完成。

- 

检查表并验证数据。

说明

验证数据没有问题后删除_del表即可。

## 方案三

此方案使用阿里云的数据传输服务DTS（Data Transmission Service）实时同步原表数据到临时表，在业务低峰期锁原表并交换表名。该方案可以大量的表同时操作。

- 

[通过](products/rds/documents/apsaradb-rds-for-mysql/use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[DMS](products/rds/documents/apsaradb-rds-for-mysql/use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[登录](products/rds/documents/apsaradb-rds-for-mysql/use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[RDS](products/rds/documents/apsaradb-rds-for-mysql/use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)[数据库](products/rds/documents/apsaradb-rds-for-mysql/use-dms-to-log-on-to-an-apsaradb-rds-for-mysql-instance-1.md)。

- 

在上方选择SQL操作>SQL窗口。

- 

使用如下命令创建临时表。

CREATE TABLE `testfs_tmp` ( `id` int(11) NOT NULL AUTO_INCREMENT, `vc` varchar(8000) DEFAULT NULL, PRIMARY KEY (`id`) ) ENGINE=innodb DEFAULT CHARSET=utf8

- 

[购买数据同步作业](https://help.aliyun.com/zh/dts/getting-started/purchase-a-dts-instance)。

说明

数据同步作业为计费项，详细价格请参见[数据传输](https://cn.aliyun.com/price/product#/dts/detail)。

- 

在数据传输控制台左侧单击数据同步。

- 

找到已购买的数据同步实例，在右侧单击配置同步链路。

- 

配置如下参数。

| 类别 | 参数 | 说明 |
| --- | --- | --- |
| 源实例信息 | 实例类型 | 选择 RDS 实例 。 |
| 实例 ID | 选择需要切换引擎的 RDS 实例。 |  |
| 连接方式 | 有 非加密传输 和 SSL 安全连接 两种连接方式。选择 SSL 安全连接 ，需要提前开启 [SSL](products/rds/documents/apsaradb-rds-for-mysql/configure-a-cloud-certificate-to-enable-ssl-encryption.md) [加密](products/rds/documents/apsaradb-rds-for-mysql/configure-a-cloud-certificate-to-enable-ssl-encryption.md) ，会显著增加 CPU 消耗。 |  |
| 目标实例信息 | 实例类型 | 选择 RDS 实例 。 |
| 实例 ID | 选择需要切换引擎的 RDS 实例。 |  |
| 连接方式 | 有 非加密传输 和 SSL 安全连接 两种连接方式。选择 SSL 安全连接 ，需要提前开启 [SSL](products/rds/documents/apsaradb-rds-for-mysql/configure-a-cloud-certificate-to-enable-ssl-encryption.md) [加密](products/rds/documents/apsaradb-rds-for-mysql/configure-a-cloud-certificate-to-enable-ssl-encryption.md) ，会显著增加 CPU 消耗。 |  |


- 

单击授权白名单并进入下一步。

- 

等待创建同步账号，然后单击下一步。

- 

将左侧的表testfs移动到右侧，并单击编辑。

- 

修改数据库名为之前创建的testfs_tmp，并单击确定。

- 

单击下一步。

- 

仅勾选全量数据初始化，并单击预检查并启动。

- 

等待预检查完成，单击关闭。

- 

等待数据同步延迟为0ms。

- 

在DMS的SQL窗口执行切换表名命令：

rename table `testfs` to `testfs_del`,`testfs_tmp` to `testfs`;

说明

- 

切换后DTS同步会报错，属于正常现象。

- 

验证数据后请尽快释放同步作业，避免继续产生计费。

## 方案四

此方案使用DTS同步整个数据库至新实例，适用于有实例升级需求，或者可以接受业务停机时间相对长一些的实例。

- 

源实例导出所有结构脚本，将脚本中关于引擎部分删除或修改。

说明

例如将create table t1(id int,name varchar(10)) engine=tokudb;修改为create table t1(id int,name varchar(10)) engine=innodb;。

- 

[新建](products/rds/documents/create-an-apsaradb-rds-for-mysql-instance.md)[RDS](products/rds/documents/create-an-apsaradb-rds-for-mysql-instance.md)[实例](products/rds/documents/create-an-apsaradb-rds-for-mysql-instance.md)，使用修改过的脚本创建库、表。

- 

将源实例数据库使用DTS[同步至新实例](https://help.aliyun.com/zh/dts/user-guide/configure-one-way-data-synchronization-between-apsaradb-rds-for-mysql-instances)上。

说明

在同步初始化时，仅勾选全量数据初始化。

- 

确认同步无延迟后，切换应用连接地址到新实例即可。

[上一篇：【产品/功能变更】RDS网络链路升级说明](products/rds/documents/apsaradb-rds-for-mysql/rds-network-link-upgrade.md)[下一篇：快速入门](products/rds/documents/apsaradb-rds-for-mysql/getting-started.md)

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
