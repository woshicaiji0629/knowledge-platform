## 常见问题
Q：我需要的插件在插件表中没有找到，怎么办？
A：可以采取如下措施：
本页面仅列举了常用插件，更多插件的支持情况，可在数据库内使用SELECT * FROM pg_available_extensions;命令查询。
到[阿里云聆听平台](https://connect.aliyun.com/)提交建议和需求。
Q：我需要的插件在其他大版本支持，但是我所使用的大版本不支持，怎么办？
A：可以采取如下措施：
耐心等待，各插件正逐步在各大版本中同步，可以关注[AliPG](release-notes-for-alipg.md)[内核小版本发布记录](release-notes-for-alipg.md)，可能在后续小版本更新中支持。
如果想要变更实例版本，尽快使用所需插件：
目标实例大版本高于当前实例大版本：在当前实例上执行大版本升级。具体操作，请参见[升级数据库大版本](upgrade-the-major-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md)。
目标实例大版本低于当前实例大版本：购买支持所需插件的大版本实例，然后通过[数据传输服务](https://help.aliyun.com/zh/dts/product-overview/what-is-dts)[DTS](https://help.aliyun.com/zh/dts/product-overview/what-is-dts)，将当前版本数据迁移至新实例中。
到[阿里云聆听平台](https://connect.aliyun.com/)提交建议和需求。
Q：插件表中显示支持的插件，但是在实际创建时报错提示不支持，怎么办？
A：请先[升级内核小版本](update-the-minor-engine-version-of-an-apsaradb-rds-for-postgresql-instance.md)至最新版后，再进行尝试。
Q：我创建的插件都是在public模式下，如何在其他Schema下创建插件并使用？
A：需要在创建插件时就指定Schema，例如：
CREATE EXTENSION <插件名> SCHEMA <Schema名>;
