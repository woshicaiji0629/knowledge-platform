## 后续操作
若创建实例时增加了数据盘的大小，实例创建成功后，必须登录ECS实例扩容分区和文件系统才能使新增的容量生效。[Linux](resize-linux-cloud-disks.md)[实例指引](resize-linux-cloud-disks.md)、[Windows](resize-windows-cloud-disks.md)[实例指引](resize-windows-cloud-disks.md)。
增加了系统盘大小，系统盘会自动扩容，若自动扩容失败，需手动扩容分区和文件系统使新增的容量生效。[Linux](resize-linux-cloud-disks.md)[实例指引](resize-linux-cloud-disks.md)、[Windows](resize-windows-cloud-disks.md)[实例指引](resize-windows-cloud-disks.md)。
若创建实例时，手动添加了新数据盘，实例创建成功后，必须先[初始化](initialize-a-data-disk.md)该新数据盘才能正常使用。
