# MySQL 5.7、8.0自建数据库全量上云方案-云数据库 RDS(RDS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/rds/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance

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

# MySQL 5.7、8.0自建数据库全量上云

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/rds)

[我的收藏](https://help.aliyun.com/my_favorites.html)

RDS MySQL支持全量备份导入功能，可以将对象存储OSS中的自建MySQL全量备份数据导入至RDS控制台，并恢复至新RDS MySQL实例中。

## 前提条件

- 

自建MySQL数据库必须符合上云条件。具体详情，请参见[附录：使用限制](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)。

- 

已在目标地域创建了OSS Bucket。如未创建，请参见[控制台创建存储空间](products/oss/documents/getting-started/create-buckets-6.md)。

说明

该目标地域必须为您希望创建RDS实例的地域。

## 上云流程概览

本文包含如下步骤：

[步骤一：安装](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[Percona Xtrabackup](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)

[步骤二：安装](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[MySQL Backup Helper](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)

[步骤三：备份自建库并上云](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)

## 演示环境说明

本文演示所用的环境为阿里云ECS实例，镜像为CentOS Linux release 8.3.2011版本，其他版本请适配相关命令。如何创建ECS实例，请参见[创建](products/ecs/documents/user-guide/create-an-instance-by-using-the-wizard.md)[ECS](products/ecs/documents/user-guide/create-an-instance-by-using-the-wizard.md)[实例](products/ecs/documents/user-guide/create-an-instance-by-using-the-wizard.md)。

## 步骤一：安装Percona Xtrabackup

[Percona XtraBackup](https://docs.percona.com/percona-xtrabackup/)是Percona公司开发的用于MySQL数据库物理热备的备份工具，支持多种数据库引擎。如您使用的是Ubuntu系统，请参见[附录](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[1：Ubuntu](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[安装](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[Xtrabackup](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)。

请根据MySQL数据库的版本选择Xtrabackup的版本。

## MySQL 5.7

wget https://downloads.percona.com/downloads/Percona-XtraBackup-2.4/Percona-XtraBackup-2.4.29/binary/redhat/8/x86_64/percona-xtrabackup-24-2.4.29-1.el8.x86_64.rpm yum localinstall percona-xtrabackup-24-2.4.29-1.el8.x86_64.rpm

## MySQL 8.0

wget https://downloads.percona.com/downloads/Percona-XtraBackup-8.0/Percona-XtraBackup-8.0.35-31/binary/redhat/8/x86_64/percona-xtrabackup-80-8.0.35-31.1.el8.x86_64.rpm yum localinstall percona-xtrabackup-80-8.0.35-31.1.el8.x86_64.rpm

## 步骤二：安装MySQL Backup Helper

前提条件

- 

已安装Golang。如未安装，请在命令行中执行下列命令安装。

sudo yum install -y go

- 

已安装unzip。如未安装，请在命令行中执行下列命令安装。

sudo yum install -y unzip

说明

上述命令仅限CentOS系统使用，如您使用的是Ubuntu系统，请参见[附录](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[2：Ubuntu](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[安装](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[Golang](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[和](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[Unzip](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)。

操作步骤

- 

下载MySQL Backup Helper源码包。

wget https://github.com/aliyun/mysql-backup-helper/archive/refs/heads/master.zip

说明

您可访问[mysql-backup-helper](https://github.com/aliyun/mysql-backup-helper)获取最新版的源码包。

- 

解压MySQL Backup Helper源码包。

unzip master.zip

- 

进入mysql-backup-helper-master文件夹，对main.go文件进行编译，获得backup_helper可执行文件。

cd mysql-backup-helper-master go build -a -o backup_helper main.go

说明

如无法正常完成编译，请参见[附录](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[4：设置](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[Go](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[代理](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)。

- 

进入oss_stream文件夹，对oss_stream.go文件进行编译，获得oss_stream可执行文件。

cd oss_stream go build -a -o oss_stream oss_stream.go

说明

如无法正常完成编译，请参见[附录](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[4：设置](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[Go](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[代理](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)。

## 步骤三：备份自建库并上云

- 

通过MySQL Backup Helper验证当前自建MySQL数据库是否支持备份。

cd ~/mysql-backup-helper-master && ./backup_helper -host <自建库主机地址> -port <自建库端口号> -user <自建库root账号> --password <自建库root密码>

- 

验证通过后，全量备份自建库并将备份文件上传至阿里云对象存储OSS。如您未提前创建OSS Bucket，请参见本文前提条件。

请根据MySQL数据库的版本选择命令。

## MySQL 5.7

innobackupex --backup --host=<自建库主机地址> --port=<自建库端口号> --user=<自建库root账号> --password=<自建库root密码> --stream=xbstream --compress <备份文件临时目录> | ./mysql-backup-helper-master/oss_stream/oss_stream -accessKeyId <阿里云账号的AccessKey ID> -accessKeySecret <阿里云账号的AccessKey Secret> -bucketName <OSS Bucket名称> -endpoint <OSS Bucket的地域节点> -objectName <自定义备份文件名>

示例：

innobackupex --backup --host=127.0.0.1 --port=3306 --user=root --password=Aa123456@ --stream=xbstream --compress /root/mysql/data | ./mysql-backup-helper-master/oss_stream/oss_stream -accessKeyId LTAI**************** -accessKeySecret ****** -bucketName test -endpoint oss-********.aliyuncs.com -objectName backup_qp.xb

数据量越大，备份时间越长。如果数据量较大，为了避免意外登出导致备份中断，建议通过nohup命令在后台进行备份。命令示例如下：

nohup sh -c 'innobackupex --backup --host=127.0.0.1 --port=3306 --user=root --password=Aa123456@ --stream=xbstream --compress /root/mysql/data | ./mysql-backup-helper-master/oss_stream/oss_stream -accessKeyId LTAI**************** -accessKeySecret ****** -bucketName test -endpoint oss-ap-southeast-1.aliyuncs.com -objectName backup_qp.xb' &

## MySQL 8.0

xtrabackup --backup --host=<自建库主机地址> --port=<自建库端口号> --user=<自建库root账号> --password=<自建库root密码> --stream=xbstream --compress <备份文件临时目录> | ./mysql-backup-helper-master/oss_stream/oss_stream -accessKeyId <阿里云账号的AccessKey ID> -accessKeySecret <阿里云账号的AccessKey Secret> -bucketName <OSS Bucket名称> -endpoint <OSS Bucket的地域节点> -objectName <自定义备份文件名>

示例：

xtrabackup --backup --host=127.0.0.1 --port=3306 --user=root --password=Aa123456@ --stream=xbstream --compress /root/mysql/data | ./mysql-backup-helper-master/oss_stream/oss_stream -accessKeyId LTAI**************** -accessKeySecret ******** -bucketName test -endpoint oss-****.aliyuncs.com -objectName backup_qp.xb

数据量越大，备份时间越长。如果数据量较大，为了避免意外登出导致备份中断，建议通过nohup命令在后台进行备份。命令示例如下：

nohup sh -c 'xtrabackup --backup --host=127.0.0.1 --port=3306 --user=root --password=Aa123456@ --stream=xbstream /root/mysql/data | ./mysql-backup-helper-master/oss_stream/oss_stream -accessKeyId LTAI**************** -accessKeySecret ****** -bucketName test -endpoint oss-ap-southeast-1.aliyuncs.com -objectName backup_qp.xb' &

说明

- 

此过程的时长取决于实例在备份时的状态，例如备份期间原实例中有太多写入操作，导致实例大量生成redo日志、或实例中执行了大型的事务等情况下，备份时间会变长。当备份顺利完成后，屏幕上会打印出completed OK !。

- 

如您暂时无法使用阿里云OSS服务，可先将自建库备份至本地，等可以顺利访问OSS后再上传。更多信息，请参见[附录](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[3：分步骤执行全量备份和上传至](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[OSS](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)。

- 

完成此步骤后，可以登录[OSS](https://oss.console.aliyun.com/bucket)[控制台](https://oss.console.aliyun.com/bucket)确认备份文件是否上传成功。如未上传成功，请重复执行步骤2。

- 

登录[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在页面左上角选择地域，在左侧导航栏中单击备份管理。

- 

单击用户备份页签下的导入备份按钮。

- 

在弹出的导入备份对话框中，仔细阅读相关说明并单击下一步，直至切换到3. 数据导入页签。

说明

向导窗口引导您如何导入备份，详情如下。更多操作，请参见[分步骤执行全量备份并上传至](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[OSS](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)。

- 

1. 备份你的数据库：全量备份自建库中的数据。

- 

2. 上传备份文件到OSS：将自建库的全量备份数据上传到OSS。

- 

在3. 数据导入页签中，配置如下参数，并单击确定。

| 参数名 | 说明 |
| --- | --- |
| MySQL 版本 | 系统自动显示为 5.7/8.0 。 说明 仅支持导入备份自建数据库的版本为 MySQL 5.7 或 8.0。 |
| 地域 | [步骤](products/rds/documents/apsaradb-rds-for-mysql/restore-the-data-of-a-self-managed-mysql-instance-to-an-apsaradb-rds-for-mysql-instance.md) [1](products/rds/documents/apsaradb-rds-for-mysql/restore-the-data-of-a-self-managed-mysql-instance-to-an-apsaradb-rds-for-mysql-instance.md) 中选择的地域，该地域需要和备份文件所在的 OSS Bucket 的地域一致。 |
| OSS Bucket | 选择自建库备份文件所在的 OSS Bucket。关于 OSS Bucket 的更多信息，请参见 [上传文件](products/oss/documents/upload-download-and-manage-objects-upload-objects.md) 。 |
| OSS 文件名 | 选择 OSS Bucket 中的自建库备份文件。您可以在 OSS 文件名 右侧的文本框中输入备份文件的文件名快速查找。本功能支持模糊匹配和精确匹配。 说明 OSS 中的备份文件必须为 _QP.XB 格式，或者将 _QP.XB 格式的文件压缩为 TAR.GZ 格式进行存储。 更多限制，请参见 [附录：使用限制](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md) 。 |
| 备注 | 自定义备份文件的备注信息。 |
| 可用区 | 设置用户备份的可用区。选择可用区后，系统会在该可用区内创建一个秒级快照，大幅节省备份导入所需要的时间。 说明 用户备份导入完成，并通过其恢复到新实例时，该可用区即为新实例所在的可用区。 |


说明

- 

如您未授权RDS访问OSS，请先在3. 数据导入页面下方单击授权地址，在跳转到的页面左下角单击同意授权。

- 

更多导入备份时的注意事项请仔细阅读该页面下的说明。

- 

系统会在用户备份中生成备份文件校验任务，等待任务状态由校验中变更为完成即可。

重要

备份文件的校验时长取决于实例在备份时的状态。例如，备份期间原实例中若有太多写入操作，会导致实例大量生成redo日志、或实例中执行了大型的事务等情况下，备份文件校验时间会变长。

- 

单击目标备份ID/备注右侧操作列下的恢复。

- 

设置如下参数，单击下一步：实例配置。

- 

- 

| 类别 | 说明 |
| --- | --- |
| 主节点可用区 | 选择主实例所在可用区。 说明 本参数仅适用于导入时未选择可用区的用户备份。导入时已选择可用区的用户备份不显示本参数。 |
| 存储类型 | ESSD PL1 云盘 ：PL1 性能级别的增强型（Enhanced）SSD 云盘。 SSD 云盘 ：基于分布式存储架构的弹性块存储设备。选择 SSD 云盘，即实现了计算与存储分离。 说明 更多信息，请参见 [存储类型](products/rds/documents/product-overview/storage-types.md) 。 |
| 实例规格 | 通用规格（入门级） ：通用型的实例规格，独享被分配的内存和 I/O 资源，与同一服务器上的其他通用型实例共享 CPU 和存储资源。 说明 每种规格都有对应的 CPU 核数、内存、最大连接数和最大 IOPS。详情请参见 [主实例规格列表](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md) 。 |
| 存储空间 | 存储空间包括数据空间、系统文件空间、日志文件空间和事务文件空间。调整存储空间时最小单位为 5 GB。 |


- 

设置如下参数，单击下一步：确认订单。

| 类别 | 说明 |
| --- | --- |
| 网络类型 | 专有网络 ：也称为 VPC（Virtual Private Cloud）。VPC 是一种隔离的网络环境，安全性和性能均高于传统的经典网络。选择专有网络时您需要选择对应的 VPC 和 主节点交换机 。 说明 请确保选择的 VPC 与需要连接的 ECS 一致，否则它们无法通过内网互通。 |
| 参数模板 | 设置实例参数模板。方便您使用系统参数模板或已创建的自定义参数模板预设实例的参数，更多信息，请参见 [使用参数模板](products/rds/documents/apsaradb-rds-for-mysql/use-a-parameter-template-to-configure-the-parameters-of-apsaradb-rds-for-mysql-instances.md) 。 |
| 时区 | 设置实例时区。 |
| 表名大小写 | 设置实例表名是否区分大小写。当本地数据库区分大小写时，您可以选择 区分大小写 ，便于您迁移数据。 |


- 

确认参数配置，选择购买量，选中服务协议，单击去支付完成支付。

说明

实例的创建需要1~5分钟时间，请耐心等待。

## 相关操作

## 设置用户备份保留天数

备份导入完成后，该用户备份默认保留3天。您可以根据业务需求增加或减少备份保留天数。

说明

当您不再需要某个用户备份，您可以删除用户备份。

- 

登录[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在页面左上角选择地域，并在左侧导航栏中单击备份管理。

- 

单击目标备份ID/备注右侧过期时间列下的设置保留天数。

- 

在弹出的对话框中，您可以直接单击下拉框选择系统预设的保留天数，也可以勾选自定义天数左侧的选框，手动输入或单击数字右侧的上下箭头增减保留天数。

说明

保留到展示了备份的过期时间，若该时间超过2099年即显示为永久。

- 

单击确定完成更改。

## 为用户备份添加标签

为了方便管理，您可以为已经导入的备份添加标签。

- 

登录[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在页面左上角选择地域，并在左侧导航栏中单击备份管理。

- 

单击目标备份ID/备注右侧标签列下的+编辑标签。

- 

单击创建标签，输入标签的键和值，单击文本框右侧的确定完成创建，并单击对话框右下角的确定完成创建。

说明

如果您已经新建了标签，可以单击选择标签，为用户备份添加标签。

- 

添加完成后，如果您希望变更目标备份的标签，可以将鼠标移动到已添加的标签上，在弹出的气泡中单击编辑标签，重复步骤3重新创建或选择标签。

## 查看用户备份的日志信息

在[备份自建库](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)过程中，如果源库中存在数据修改的操作，则备份文件中会带有日志信息，方便您恢复这部分增量数据。

- 

登录[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在页面左上角选择地域，并在左侧导航栏中单击备份管理。

- 

单击目标备份ID右侧操作列下的详情。

- 

在弹出的窗口中即可查询到日志的具体信息。

说明

日志信息中包含如下内容：

- 

Master_Log_File：：日志的文件名，展示增量数据所在的起始日志文件。

- 

Master_Log_Position：：日志文件中的位置信息，展示日志文件中增量数据的起始位置。

## 删除用户备份

为了节省开支，您可以删除不再需要的用户备份。

- 

登录[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在页面左上角选择地域，并在左侧导航栏中单击备份管理。

- 

单击目标备份ID/备注右侧操作列下的删除。

- 

在弹出的窗口中单击确认。

## 其他操作

- 

自定义列表项：显示或隐藏备份列表下的列，默认为全部显示。

- 

登录[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在页面左上角选择地域，并在左侧导航栏中单击备份管理。

- 

单击页面右侧的图标，在弹出的窗口中，选定列表项，单击或图标，显示或隐藏列表项。

说明

左边框中的列表项为隐藏项，右边框中的列表项为显示项。

- 

单击确定。

- 

导出资源列表：将当前所有用户备份信息导出到CSV文件。

- 

登录[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在页面左上角选择地域，并在左侧导航栏中单击备份管理。

- 

单击页面右侧的图标即可导出资源列表。

- 

刷新：刷新用户备份列表。

- 

登录[RDS](https://rdsnext.console.aliyun.com/rdsList/basic)[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)，在页面左上角选择地域，并在左侧导航栏中单击备份管理。

- 

单击页面右侧的图标即可刷新用户备份列表。

## 附录1：Ubuntu安装Xtrabackup

请根据MySQL数据库的版本选择Xtrabackup的版本。

## MySQL 5.7

- 

安装Xtrabackup。

wget https://downloads.percona.com/downloads/Percona-XtraBackup-2.4/Percona-XtraBackup-2.4.29/binary/redhat/8/x86_64/percona-xtrabackup-24-2.4.29-1.el8.x86_64.rpm yum localinstall percona-xtrabackup-24-2.4.29-1.el8.x86_64.rpm

- 

安装qpress。

sudo apt-get install -y qpress

说明

qpress是Xtrabackup的解压缩工具，由于Ubuntu系统安装[XtraBackup](https://docs.percona.com/percona-xtrabackup/)不会集成qpress，因此需要此步骤单独进行安装。

说明

执行上述任意步骤时如出现类似于The following packages have unmet dependencies的提示，请按照提示执行apt-get -f install命令安装缺失的依赖包后重新执行。

## MySQL 8.0

- 

安装Xtrabackup。

wget https://downloads.percona.com/downloads/Percona-XtraBackup-8.0/Percona-XtraBackup-8.0.35-31/binary/redhat/8/x86_64/percona-xtrabackup-80-8.0.35-31.1.el8.x86_64.rpm yum localinstall percona-xtrabackup-80-8.0.35-31.1.el8.x86_64.rpm

- 

安装qpress。

sudo apt-get install -y qpress

说明

qpress是XtraBackup的解压缩工具，由于Ubuntu系统安装[XtraBackup](https://docs.percona.com/percona-xtrabackup/)不会集成qpress，因此需要此步骤单独进行安装。

说明

执行上述任意步骤时如出现类似于The following packages have unmet dependencies的提示，请按照提示执行apt-get -f install命令安装缺失的依赖包后重新执行。

## 附录2：Ubuntu安装Golang和Unzip

- 

安装Golang

sudo apt-get install -y software-properties-common sudo add-apt-repository ppa:longsleep/golang-backports sudo apt-get update sudo apt-get install -y golang-go

- 

安装Unzip

sudo apt-get -y install unzip

## 附录3：分步骤执行全量备份和上传至OSS

- 

全量备份自建数据库至本地。

请根据MySQL数据库的版本选择命令。

## MySQL 5.7

innobackupex --backup --host=<自建库主机地址> --port=<自建库端口号> --user=<自建库root账号> --password=<自建库root密码> --stream=xbstream --compress <备份文件临时目录> > /<备份路径>/<备份文件名>_qp.xb

示例：

innobackupex --backup --host=127.0.0.1 --port=3306 --user=root --password=Aa123456@ --stream=xbstream --compress /root/mysql/data > /root/backup_qp.xb

## MySQL 8.0

xtrabackup --backup --host=<自建库主机地址> --port=<自建库端口号> --user=<自建库root账号> --password=<自建库root密码> --stream=xbstream --compress <备份文件临时目录> > /<备份路径>/<备份文件名>_qp.xb

示例：

xtrabackup --backup --host=127.0.0.1 --port=3306 --user=root --password=Aa123456@ --stream=xbstream --compress /root/mysql/data > /root/backup_qp.xb

- 

通过OSS_Stream将备份文件上传至OSS。

cat /<备份路径>/<备份文件名>_qp.xb | ./mysql-backup-helper-master/oss_stream/oss_stream -accessKeyId LTAI**************** -accessKeySecret ****** -bucketName test -endpoint oss-********.aliyuncs.com -objectName backup_qp.xb

示例：

cat /root/backup_qp.xb | ./mysql-backup-helper-master/oss_stream/oss_stream -accessKeyId LTAI**************** -accessKeySecret ****** -bucketName test -endpoint oss-********.aliyuncs.com -objectName backup_qp.xb

## 附录4：设置Go代理

如果您使用的是中国地域的ECS，可能无法正常完成[步骤二](products/rds/documents/apsaradb-rds-for-mysql/migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)的编译流程，此时需要执行如下命令以便Go使用阿里云的代理，然后重新执行编译。

go env -w GO111MODULE=on go env -w GOPROXY=https://mirrors.aliyun.com/goproxy/,direct

说明

如果设置了上述代理后还是出现编译出错的情况，则可能是代理地址暂不可用造成的。此时可以在搜索引擎中搜索其他Go的代理地址来替换上述命令中的https://mirrors.aliyun.com/goproxy/,direct部分。推荐搜索关键词：Go代理。

## 附录5：使用限制

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 限制项 | 详情 |
| --- | --- |
| MySQL 版本限制 | 目前仅支持如下自建数据库上云。 MySQL 5.7（5.7.32 及以下小版本） MySQL 8.0（8.0.18 及以下小版本） 说明 自建库的版本必须和 RDS 实例版本对应。例如：MySQL 5.7 的备份数据只能恢复至 RDS MySQL 5.7 版本的实例。 如果版本不符合本文的要求，请参见 [从自建](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-self-managed-mysql-database-to-an-apsaradb-rds-for-mysql-instance.md) [MySQL](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-self-managed-mysql-database-to-an-apsaradb-rds-for-mysql-instance.md) [迁移至](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-self-managed-mysql-database-to-an-apsaradb-rds-for-mysql-instance.md) [RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-self-managed-mysql-database-to-an-apsaradb-rds-for-mysql-instance.md) [实例](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-self-managed-mysql-database-to-an-apsaradb-rds-for-mysql-instance.md) 进行迁移。 |
| 自建 MySQL 限制 | 自建库的数据必须存储在 MySQL 中配置的 datadir 数据目录下。您可在命令行执行 mysqladmin -u<自建库 root 账号> -p<自建库 root 密码> variables | grep datadir 命令，确认当前 MySQL 的 datadir 数据目录。 innodb_data_file_path 参数必须为默认的 ibdata1 。 |
| 备份限制 | 备份完成之后，自建库中产生的增量数据不会保留在备份文件中。 备份自建 MySQL 5.7 数据库必须使用 Percona XtraBackup 2.4 版本。 使用 Percona XtraBackup 备份自建库时不支持传入 --tables 、 --tables-exclude 、 --tables-file 、 --databases 或 --databases-file 选项。 无法读取 OSS Bucket 中的加密文件，因此创建 OSS Bucket 时 服务端加密方式 需要选 无 。 不支持差异备份文件或日志备份文件。 全量备份文件名不能包含特殊字符，否则会导致上云失败。 授予 RDS 服务账号访问 OSS 的权限以后，系统会在访问控制 RAM 的角色管理中创建名为 AliyunRDSImportRole 的角色。请勿修改或删除这个角色，否则会导致上云任务无法下载备份文件而失败。 在 OSS 备份数据恢复上云任务没有完成之前，请不要删除 OSS 上的备份文件，否则会导致上云任务失败。 OSS 中的备份文件必须为 _QP.XB 格式，或者将 _QP.XB 格式的文件压缩为 TAR.GZ 格式进行存储。 说明 对于不符合格式要求的备份文件，例如备份格式为 .xbstream ，建议您先将该格式文件恢复到本地数据库，转换为 _QP.XB 格式 后再进行上云操作；或者您也可以选择其他上云方案，请参见 [从自建](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-self-managed-mysql-database-to-an-apsaradb-rds-for-mysql-instance.md) [MySQL](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-self-managed-mysql-database-to-an-apsaradb-rds-for-mysql-instance.md) [迁移至](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-self-managed-mysql-database-to-an-apsaradb-rds-for-mysql-instance.md) [RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-self-managed-mysql-database-to-an-apsaradb-rds-for-mysql-instance.md) [实例](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-self-managed-mysql-database-to-an-apsaradb-rds-for-mysql-instance.md) 。 |
| OSS 限制 | 使用命令行分片上传，单个文件需限制在 16 TB 以内，详情请参见 [OSS](products/oss/documents/user-guide/limits.md) [使用限制](products/oss/documents/user-guide/limits.md) 。 存储备份文件的 OSS 区域必须与还原到的 RDS 实例区域一致。 |
| 恢复限制 | 为防止误操作覆盖实例数据，当前仅支持恢复数据至新实例。 无法恢复数据大小超过 RDS MySQL 所支持的最大存储空间的数据库，更多规格信息，请参见 [主实例规格列表](products/rds/documents/product-overview/primary-apsaradb-rds-instance-types.md) 。 导入备份时，系统会创建一个临时实例并将备份数据导入至该临时实例，恢复时从该临时实例中提取数据。默认情况下，该临时实例预配存储空间大小为备份数据大小的 5 倍，如导入备份出现存储空间不足，可自行调整该存储空间。 恢复操作不会导入自建库的用户账户，自定义函数和存储过程。请记录上述信息，在恢复完成后手动添加至 RDS 实例。 恢复操作不会导入时区信息。请记录自建库的时区信息，在恢复完成后手动进行设置。 目前仅支持将备份文件恢复至 RDS MySQL 5.7 或 8.0 基础系列（SSD 云盘）按量付费实例。 说明 您可以在迁移完成后进行如下操作： [升级数据库版本](products/rds/documents/apsaradb-rds-for-mysql/upgrade-the-major-engine-version-of-an-apsaradb-rds-for-mysql-instance.md) [基础系列升级为高可用系列](products/rds/documents/apsaradb-rds-for-mysql/upgrade-an-apsaradb-rds-for-mysql-instance-from-basic-edition-to-high-availability-edition.md) [变更配置](products/rds/documents/apsaradb-rds-for-mysql/change-the-specifications-of-an-apsaradb-rds-for-mysql-instance.md) [按量付费转包年包月](products/rds/documents/apsaradb-rds-for-mysql/change-the-billing-method-of-an-apsaradb-rds-for-mysql-instance-from-pay-as-you-go-to-subscription.md) |
| 复制限制 | 仅支持基于全局事务标识 GTID（Global Transaction Identifier）方式的复制。因此，自建库需要开启 GTID 复制，将 gtid_mode 和 enforce_gtid_consistency 均设置为 ON 。 备份校验记录默认保存 7 天，超过 7 天的备份记录以及生成的快照会自动删除，建立复制关系操作应在实例恢复完成后尽快实施，避免自建库的日志被清理，以及备份校验后生成的快照被删除。 |


[上一篇：从自建MySQL迁移至RDS MySQL实例](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-self-managed-mysql-database-to-an-apsaradb-rds-for-mysql-instance.md)[下一篇：从自建Oracle迁移至阿里云RDS MySQL](products/rds/documents/apsaradb-rds-for-mysql/migrate-data-from-a-user-created-oracle-instance-to-an-rds.md)

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
