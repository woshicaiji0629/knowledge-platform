## MySQL 5.7
innobackupex --backup --host=<自建库主机地址> --port=<自建库端口号> --user=<自建库root账号> --password=<自建库root密码> --stream=xbstream --compress <备份文件临时目录> > /<备份路径>/<备份文件名>_qp.xb
示例：
innobackupex --backup --host=127.0.0.1 --port=3306 --user=root --password=Aa123456@ --stream=xbstream --compress /root/mysql/data > /root/backup_qp.xb
