## 配置目标库参数
本教程中的目标库指云数据库RDS MySQL实例，您需要将源库迁移至该数据库。
数据库类型：选择MySQL。
接入方式：选择云实例。
实例地区：选择RDS实例所在地域，本教程以华东1 （杭州）为例。
RDS实例ID：在下拉列表中选择[准备工作](step-3-migrate-a-user-created-database-to-an-rds-mysql-instance.md)中创建的RDS MySQL实例ID。
数据库账号和数据库密码：填写RDS MySQL实例中高权限账号和密码，本教程以dbuser和用户自定义密码为例。
连接方式：本教程以非加密连接为例。如果选择SSL安全连接，您需要提前开启RDS MySQL实例的SSL加密功能，详情请参见[使用云端证书快速开启](configure-a-cloud-certificate-to-enable-ssl-encryption.md)[SSL](configure-a-cloud-certificate-to-enable-ssl-encryption.md)[链路加密](configure-a-cloud-certificate-to-enable-ssl-encryption.md)。
单击测试连接以进行下一步。DTS会自动为ECS实例添加DTS安全组，并将DTS服务器IP添加至RDS实例白名单中，以允许DTS访问ECS实例和RDS实例。
配置任务对象。
选择迁移类型。为了实现数据库平滑迁移，您需要勾选库表结构迁移、全量迁移和增量迁移。三种迁移方式的区别请参见[迁移类型说明](https://help.aliyun.com/zh/dts/user-guide/overview-of-data-migration-scenarios#section-wda-pa7-g81)。
在源库对象中选择待迁移的数据库（本教程以wordpressdb为例），单击将其移动至已选择对象，然后单击下一步高级配置。
高级配置页面中您无需进行参数选择，您可以直接使用默认的参数配置并单击下一步数据校验。
在数据校验页面中勾选全量校验、增量校验和结构校验，然后单击下一步保存任务并预检查。三种数据校验方式详情请参见[什么是数据校验](https://help.aliyun.com/zh/dts/user-guide/what-is-data-verification)。
预检查通过率达到100%后，单击下一步购买。
选择数据迁移实例的链路规格，本教程以small规格为例。阅读并选中《数据传输（按量付费）服务条款》，单击购买并启动。
迁移任务正式开始，您可以单击迁移任务ID查看具体进度。当您看到如下界面，表示存量数据已迁移完成，增量数据会实时同步。任务启动后，在迁移任务详情页的实例进展区域可查看各阶段运行状态（增
