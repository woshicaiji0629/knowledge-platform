## MySQL 8.0
xtrabackup --backup --host=<自建库主机地址> --port=<自建库端口号> --user=<自建库root账号> --password=<自建库root密码> --stream=xbstream --compress <备份文件临时目录> > /<备份路径>/<备份文件名>_qp.xb
示例：
xtrabackup --backup --host=127.0.0.1 --port=3306 --user=root --password=Aa123456@ --stream=xbstream --compress /root/mysql/data > /root/backup_qp.xb
通过OSS_Stream将备份文件上传至OSS。
cat /<备份路径>/<备份文件名>_qp.xb | ./mysql-backup-helper-master/oss_stream/oss_stream -accessKeyId LTAI**************** -accessKeySecret ****** -bucketName test -endpoint oss-********.aliyuncs.com -objectName backup_qp.xb
示例：
cat /root/backup_qp.xb | ./mysql-backup-helper-master/oss_stream/oss_stream -accessKeyId LTAI**************** -accessKeySecret ****** -bucketName test -endpoint oss-********.aliyuncs.com -objectName backup_qp.xb
