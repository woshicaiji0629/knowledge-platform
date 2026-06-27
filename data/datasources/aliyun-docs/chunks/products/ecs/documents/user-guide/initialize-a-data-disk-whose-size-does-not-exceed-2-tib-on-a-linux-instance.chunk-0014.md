J:MIN RM SIZE RO TYPE MOUNTPOINT vda 253:0 0 50G 0 disk ├─vda1 253:1 0 2M 0 part ├─vda2 253:2 0 200M 0 part /boot/efi └─vda3 253:3 0 49.8G 0 part / vdb 253:16 0 40G 0 disk └─vdb1 253:17 0 40G 0 part
- /etc/fstab 配置错误，重启后实例无法启动怎么办？
可依照[Linux](../support/the-etc-fstab-file-of-the-linux-instance-is-incorrectly-configured-causing.md)[实例的/etc/fstab](../support/the-etc-fstab-file-of-the-linux-instance-is-incorrectly-configured-causing.md)[文件配置错误导致系统启动异常问题处理](../support/the-etc-fstab-file-of-the-linux-instance-is-incorrectly-configured-causing.md)，使用VNC进行远程连接实例，在紧急模式下，手动修改错误的挂载信息。
- 创建GPT分区时，显示not aligned分区未对齐如何解决？
运行以下命令，重新开始分区。本操作以数据盘/dev/vdb为例。
sudo parted /dev/vdb
在parted工具分区界面，输入以下内容，删除错误分区。
<错误分区number号>可以通过print指令查看。
重要
请在删除分区前，确保分区内无数据或者数据已备份。
rm <错误分区number号>
运行以下命令，保证开始位置与结束位置的单位为MiB、GiB，重新划分分区。以MiB为例：
mkpart data <开始容量>MiB <结束容量>MiB
- 创建文件系统时提示“Size of device /dev/vdb too big to be expressed”。
原因：若数据盘容量为16 TiB，需使用1.42及以上版本的e2fsprogs工具创建ext4文件系统。否则将报错：
mkfs.ext4: Size of device /dev/vdb too big to be expressed in 32 bits using a blocksize of 4096.
解决方案：安装高版本的e2fsprogs，例如1.42.8。
检查e2fsprogs当前的版本。
sudo rpm -qa | grep e2fsprogs
下载1.42.8版本的e2fsprogs。
也可以在[e2fsprogs](https://www.kern
