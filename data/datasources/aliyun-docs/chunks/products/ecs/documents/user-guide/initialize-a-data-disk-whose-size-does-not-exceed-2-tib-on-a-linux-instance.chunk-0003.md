### 方法二：通过命令行初始化
步骤一：创建分区
登录ECS实例。
访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。在页面左侧顶部，选择目标资源所在的资源组和地域。
进入目标实例详情页，单击远程连接，选择通过Workbench远程连接。根据页面提示登录，进入终端页面。
创建分区。
创建分区有助于逻辑隔离，可将不同用途的数据分隔存放，防止相互干扰或影响。如果无需创建分区可直接[创建文件系统](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)。
确定待初始化云盘设备名称。FSTYPE表示文件系统类型。如果为空，表示没有文件系统。
sudo lsblk -fNAME FSTYPE LABEL UUID MOUNTPOINT vda └─vda1 ext4 root 33b46ac5-7482-4aa5-8de0-60ab4c3a4c78 / vdb └─vdb1 ext4 f1645951-134f-4677-b5f4-c65c71f8f86d vdc
如果目标云盘存在文件系统，表示已经初始化，仅需[挂载文件系统](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)。示例中数据盘vdb的分区vdb1，存在ext4文件系统，无需创建分区及文件系统。
如果目标云盘不存在分区和文件系统，表示未初始化。示例中数据盘vdc无分区和文件系统，需要创建才可使用。
创建分区。
以创建GPT分区为例，MBR分区请参看[如何创建](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)[MBR](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)[分区](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)。
请参阅[如何选择分区类型和文件系统类型](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)，了解不同分区的区别。
重要
创建分区将清除数据盘中所有数据，请确保云盘为空或已创建快
