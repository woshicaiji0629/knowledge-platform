## 步骤三：备份自建库并上云
通过MySQL Backup Helper验证当前自建MySQL数据库是否支持备份。
cd ~/mysql-backup-helper-master && ./backup_helper -host <自建库主机地址> -port <自建库端口号> -user <自建库root账号> --password <自建库root密码>
验证通过后，全量备份自建库并将备份文件上传至阿里云对象存储OSS。如您未提前创建OSS Bucket，请参见本文前提条件。
请根据MySQL数据库的版本选择命令。
