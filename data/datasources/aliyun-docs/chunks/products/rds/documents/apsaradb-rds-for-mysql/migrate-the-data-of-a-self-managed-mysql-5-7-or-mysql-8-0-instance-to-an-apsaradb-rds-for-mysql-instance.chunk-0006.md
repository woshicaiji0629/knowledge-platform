## 步骤二：安装MySQL Backup Helper
前提条件
已安装Golang。如未安装，请在命令行中执行下列命令安装。
sudo yum install -y go
已安装unzip。如未安装，请在命令行中执行下列命令安装。
sudo yum install -y unzip
说明
上述命令仅限CentOS系统使用，如您使用的是Ubuntu系统，请参见[附录](migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[2：Ubuntu](migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[安装](migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[Golang](migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[和](migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)[Unzip](migrate-the-data-of-a-self-managed-mysql-5-7-or-mysql-8-0-instance-to-an-apsaradb-rds-for-mysql-instance.md)。
操作步骤
下载MySQL Backup Helper源码包。
wget https://github.com/aliyun/mysql-backup-helper/archive/refs/heads/master.zip
说明
您可访问[mysql-backup-helper](https://github.com/aliyun/mysql-backup-helper)获取最新版的源码包。
解压MySQL Backup Helper源码包。
unzip master.zip
进入mysql-backup-helper-master文件夹，对main.go文件进行编译，获得backup_helper可执行文件。
cd mysql-backup-
