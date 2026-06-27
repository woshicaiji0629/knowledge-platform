ed-2-tib-on-a-linux-instance.md)，才能使数据盘可用。
sudo lsblkNAME MAJ:MIN RM SIZE RO TYPE MOUNTPOINT vda 253:0 0 50G 0 disk └─vda1 253:3 0 49.8G 0 part / vdb 253:16 0 40G 0 disk └─vdb1 253:17 0 40G 0 part vdc 253:23 0 40G 0 disk └─vdc1 253:24 0 40G 0 part
示例中目标设备vdc的云盘容量，全部划至vdc1分区。
步骤二：创建文件系统
重要
创建文件系统会删除数据盘中数据，请确保云盘为空或已[手动创建单个快照](create-a-snapshot.md)备份数据。
记录待初始化云盘的目标设备名称，后续创建文件系统时需要使用。
sudo lsblk -fNAME FSTYPE LABEL UUID MOUNTPOINT vda └─vda1 ext4 root 33b46ac5-7482-4aa5-8de0-60ab4c3a4c78 / vdb └─vdb1 ext4 f1645951-134f-4677-b5f4-c65c71f8f86d vdc └─vdc1 vdd
如果设备存在分区，目标设备名称为分区名称。示例中数据盘vdc目标设备名称为vdc1。
如果设备不存在分区，目标设备名称与设备名称一致。示例中数据盘vdd目标设备名称为vdd。
创建文件系统。
ext4
将命令中的变量<目标设备名称>替换为[上一步](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)获取的目标设备名称后执行。
若有扩容至64 TiB需求时，请在命令中添加-i 65536，指定bytes-per-inode为65536。sudo mkfs -t ext4 /dev/<目标设备名称>
xfs
安装xfsprogs工具。
Debian或Ubuntu等类型，请使用sudo apt-get install -y <软件包名称>。sudo yum install -y xfsprogs
创建xfs文件系统。
将命令中的变量<目标设备名称>替换为[上一步](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)获取的目标设备名称后执行。
sudo mkfs -t xfs /dev/<目标设备名称>
检查文件系统是否创建成功。
运行sudo lsblk -f，若回执中目标设备的FSTYPE为所创建的目标文件系统类型，表示配置成功。接下来需要[挂载文件系统
