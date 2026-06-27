## 三、创建账号
在[实例列表](https://rdsnext.console.aliyun.com/rdsList/basic)中单击实例ID，选择左侧导航栏账号管理，单击创建账号打开创建账号页签。
设置账号参数：本教程设置数据库账号为dbuser，账号类型选择高权限账号。
填写新密码与确认密码，单击确定按钮，完成账号创建。
说明
如您创建账号失败，请检查是否存在账号重名、创建过于频繁或实例中已有高权限账号等问题，解决后重新创建。
您可以刷新账号管理页面查看新建的高权限账号。
说明
RDS MySQL支持创建普通账号和高权限账号，两者区别如下：
高权限账号：云数据库RDS MySQL内最高权限账号（RDS MySQL不支持创建root账号），拥有实例下所有数据库的权限，可通过控制台或API创建，每个实例仅允许创建一个高权限账号。
普通账号：仅对被授权数据库有部分操作权限，可通过[控制台、API](create-an-account-on-an-apsaradb-rds-for-mysql-instance.md)[和](create-an-account-on-an-apsaradb-rds-for-mysql-instance.md)[SQL](create-an-account-on-an-apsaradb-rds-for-mysql-instance.md)[命令创建](create-an-account-on-an-apsaradb-rds-for-mysql-instance.md)。如您需要使用SQL命令创建普通账号（如CREATE USER），需要先创建高权限账号，再通过高权限账号登录数据库执行命令。
