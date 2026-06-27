## MySQL 8.0
xtrabackup --backup --host=<自建库主机地址> --port=<自建库端口号> --user=<自建库root账号> --password=<自建库root密码> --stream=xbstream --compress <备份文件临时目录> | ./mysql-backup-helper-master/oss_stream/oss_stream -accessKeyId <阿里云账号的AccessKey ID> -accessKeySecret <阿里云账号的AccessKey Secret> -bucketName <OSS Bucket名称> -endpoint <OSS Bucket的地域节点> -objectName <自定义备份文件名>
示例：
xtrabackup --backup --host=127.0.0.1 --port=3306 --user=root --password=Aa123456@ --stream=xbstream --compress /root/mysql/data | ./mysql-backup-helper-master/oss_stream/oss_stream -accessKeyId LTAI**************** -accessKeySecret ******** -bucketName test -endpoint oss-****.aliyuncs.com -objectName backup_qp.xb
数据量越大，备份时间越长。如果数据量较大，为了避免意外登出导致备份中断，建议通过nohup命令在后台进行备份。命令示例如下：
nohup sh -c 'xtrabackup --backup --host=127.0.0.1 --port=3306 --user=root --password=Aa123456@ --stream=xbstream /root/mysql/data | ./mysql-backup-helper-master/oss_stream/oss_stream -accessKeyId LTAI**************** -accessKeySecret ****** -bucketName test -endpoint oss-ap-southeast-1.aliyuncs.com -objectName backup_qp.xb' &
说明
此过程的时长取决于实例在备份时的状态，例如备份期间原实例中有太多写入操作，导致实例大量生成redo日志、或实例中执行了大型的事务等情况下，备份时间会变长。当备份顺利完成后，屏幕上会打印出completed OK !。
如您暂时无法使用阿里云OSS服务，可先将自建库
