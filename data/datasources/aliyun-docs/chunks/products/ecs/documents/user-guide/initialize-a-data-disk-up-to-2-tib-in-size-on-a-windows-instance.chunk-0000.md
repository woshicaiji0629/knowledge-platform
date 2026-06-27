## 操作步骤
登录ECS实例。
访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。在页面左侧顶部，选择目标资源所在的资源组和地域。
进入目标实例详情页，单击远程连接，选择通过Workbench远程连接。选择连接方式为终端连接，输入账号和密码，登录图形化终端页面
联机。
在Windows Server桌面，右键单击图标，选择磁盘管理。
在磁盘管理页面中，找到脱机状态的目标数据盘。
若弹出初始化磁盘对话框，表示云盘已联机。可直接[初始化云盘](initialize-a-data-disk-up-to-2-tib-in-size-on-a-windows-instance.md)。若数据盘已联机且分区状态良好，无需其余操作，可直接使用。
右键单击目标磁盘，选择联机。
若磁盘显示联机，目标分区显示状态良好，表示系统可正常使用该云盘。
若磁盘显示没有初始化，目标分区显示未分配，需要[初始化](initialize-a-data-disk-up-to-2-tib-in-size-on-a-windows-instance.md)后才可存储数据。
初始化云盘。
初始化云盘会删除数据盘中数据，请确保云盘为空。
右键单击目标磁盘，选择初始化磁盘。
在初始化磁盘对话框，选择磁盘分区形式后，单击确定。
重要
MBR 分区最大支持 2 TiB 容量。如果云盘容量大于 2 TiB 或后续有扩容至 2 TiB 以上需求，分区时请采用 GPT 分区格式。
右键单击目标磁盘的未分配区域，选择新建简单卷。
在新建简单卷向导对话框中，单击下一步，根据向导完成初始化操作。
在指定卷大小对话框中，设置简单卷大小后，单击下一步。
如果只需要创建一个主区，保持默认即可。也可以根据需要设置简单卷大小，将目标磁盘分成多个分区来使用。
在分配驱动器号和路径对话框中，按需选择分配以下驱动器号，然后单击下一步。
在格式化分区对话框中，选择按下列设置格式化这个卷，设置格式化信息后，单击下一步。
重要
请谨慎选择分配单元大小，此设置一旦确定将无法修改。具体云盘容量限制，请参看[NTFS](https://learn.microsoft.com/en-us/windows-server/storage/file-server/ntfs-overview)[概述](https://learn.microsoft.com/en-us/windows-server/storage/file-server/ntfs-overview)。
后续有扩容至16TiB～32TiB（包括）需求，选8192。
后续有扩容至32TiB～64TiB（包括）需求，选16K。
其
