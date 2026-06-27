ement-service/user-guide/integrate-apsaradb-rds-secrets-into-dms.md)。
填写数据库账号与数据库密码，本教程以高权限账号dbuser和用户自定义密码为例。
选择管控模式。本教程以自由操作 永久免费为例。
说明
稳定变更与安全协同[收费](https://help.aliyun.com/zh/dms/product-overview/pricing)。
相比于自由操作 永久免费的[管控模式](https://help.aliyun.com/zh/dms/product-overview/control-modes)，稳定变更与安全协同提供更多的功能支持和更强的数据库管控能力，如果您是试用或体验RDS MySQL产品，建议您选择自由操作模式。
查看数据库。登录成功后您可以在DMS页面左侧的已登录实例中查看新创建的数据库，本教程以db_test1数据库为例，您也可以双击其它数据库进行切换。
说明
information_schema、MySQL、performance_schema、sys、回收站均为系统库。
如果实例存在，但实例展开后未找到目标数据库，可能是：
登录账号无目标数据库的访问权限：您可前往RDS实例详情页的账号管理页面手动[调整账号权限](modify-the-permissions-of-a-standard-account-on-an-apsaradb-rds-for-mysql-instance.md)。
元数据未同步导致目录无法显示：请将鼠标悬浮在目标数据库所属实例上，单击实例名右侧的按钮，即可刷新数据库列表，显示目标数据库。
如需快速同步数据库的库表结构，可以通过DMS[空库初始化](https://help.aliyun.com/zh/dms/initialize-empty-databases)功能实现。
