## 挂载访问
创建挂载目录。
您可按需自由设定挂载目录的文件名与路径。例如，创建/tmp/ossfs2-bucket目录作为挂载目录。
sudo mkdir /tmp/ossfs2-bucket
执行命令挂载。
执行命令将ossfs 2.0配置文件ossfs2.conf中所配置的Bucket只读挂载至本地/tmp/ossfs2-bucket/目录下。如果您需要采用读写挂载，请删除ossfs2.conf配置文件中的--ro=true选项。
sudo ossfs2 mount /tmp/ossfs2-bucket/ -c /etc/ossfs2.conf
操作已挂载的Bucket。
挂载完成后您就可以像访问本地文件系统一样操作Bucket中的对象。例如执行sudo ls -lh /tmp/ossfs2-bucket/命令，查看已挂载Bucket的文件列表。
[root@iZbp1hxeiqyf3kjqoxgrgqZ ossfs2-bucket]# sudo ls -lh /tmp/ossfs2-bucket/ total 36G drwxrwxrwx 1 root root 0 Mar 20 13:27 100G drwxrwxrwx 1 root root 0 Mar 20 13:27 100G -rwxrwxrwx 1 root root 36G Feb 21 10:48 xxx.bin drwxrwxrwx 1 root root 0 Mar 20 10:48 checkpoints -rwxrwxrwx 1 root root 0 Feb 10 18:25 filename.txt -rwxrwxrwx 1 root root 23K Mar 7 13:26 xxx.txt -rwxrwxrwx 1 root root 191 Feb 25 15:10 xxx.txt drwxrwxrwx 1 root root 0 Mar 20 10:48 img -rwxrwxrwx 1 root root 575 Mar 6 16:52 xxx.txt -rwxrwxrwx 1 root root 269 Jan 23 14:48 xxx.txt -rwxrwxrwx 1 root root 2.2M Feb 10 13:20 xxx.txt -rwxrwxrwx 1 root root 11 Jan 23 14:08 xxxon.txt -rwxrwxrwx 1 root root 2.1K Jan 24 14:16 xxx.txt -rwxrwxrwx 1 root root 2.1K Jan 24 14:17 xxx.txt -rwxrwxrwx 1 root root 4.8K Feb 10 13:36 xxx.txt -rwxrwxrwx 1 root
