## MySQL 5.7
安装Xtrabackup。
wget https://downloads.percona.com/downloads/Percona-XtraBackup-2.4/Percona-XtraBackup-2.4.29/binary/redhat/8/x86_64/percona-xtrabackup-24-2.4.29-1.el8.x86_64.rpm yum localinstall percona-xtrabackup-24-2.4.29-1.el8.x86_64.rpm
安装qpress。
sudo apt-get install -y qpress
说明
qpress是Xtrabackup的解压缩工具，由于Ubuntu系统安装[XtraBackup](https://docs.percona.com/percona-xtrabackup/)不会集成qpress，因此需要此步骤单独进行安装。
说明
执行上述任意步骤时如出现类似于The following packages have unmet dependencies的提示，请按照提示执行apt-get -f install命令安装缺失的依赖包后重新执行。
