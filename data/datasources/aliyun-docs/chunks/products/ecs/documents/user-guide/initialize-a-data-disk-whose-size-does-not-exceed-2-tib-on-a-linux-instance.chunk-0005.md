tance.md)[2.a](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)中获取到的设备名称。
sudo parted /dev/<设备名称> print
检查是否对齐。
<设备名称>调整为[步骤](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)[2.a](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)中获取到的设备名称，<分区编号>为上一步获取的分区Number。
sudo parted /dev/<设备名称> align-check optimal <分区编号>
返回aligned表示对齐。[创建](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)[GPT](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)[分区时，显示](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)[not aligned](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)[分区未对齐如何解决？](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)
刷新磁盘分区表。
执行sudo partprobe，通知操作系统重新读取磁盘上的分区信息，以便能够识别新建的分区信息。
查看分区创建是否成功。
执行sudo lsblk查看新分区信息。若待初始化云盘存在正确分区信息，表明分区创建完成。接下来需要[创建文件系统](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)，才能使数据盘可用。
sudo lsblkNAME MAJ:MIN RM SIZE RO TYPE MOUNTPOINT vda 253:0 0 50G 0 disk └─vda1 253:3 0 49.8G 0 part / vdb 253:16 0 4
