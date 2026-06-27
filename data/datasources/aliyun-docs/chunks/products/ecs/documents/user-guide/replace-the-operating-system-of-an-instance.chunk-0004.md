## 后续任务
（条件必选）处理数据盘
同类型系统更换：如果更换前后的系统均为 Linux，且存在数据盘。更换后需登录实例，[挂载数据盘文件系统](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)。
跨类型系统更换：
Linux 更换为 Windows：Windows 默认无法识别 ext4、XFS 等文件系统格式。可使用Ext2Fsd等第三方工具读取数据盘，或在无重要数据的情况下[重新初始化数据盘](re-initialize-a-data-disk.md)。
Windows 更换为 Linux：Linux 默认无法识别 NTFS 文件系统格式。可[安装 ntfs-3g 工具挂载文件系统](how-do-i-move-an-ntfs-disk-between-a-linux-instance-and-a-windows-instance.md)，或在无重要数据的情况下[重新初始化数据盘](re-initialize-a-data-disk.md)。
（可选）恢复原系统盘数据如果需要恢复原系统盘的数据，可[通过原系统盘快照恢复系统盘中的数据](use-a-snapshot-of-the-original-system-disk-to-restore-data-after-the-operating-system-of-an-ecs-instance-is-replaced.md)，使用更换前创建的快照创建一个新的按量付费云盘，并将其挂载到实例上进行数据恢复。数据恢复完成后，请及时释放该云盘以避免产生不必要的费用。
（可选）扩容系统盘分区与文件系统
通过更换操作系统（系统盘）对系统盘进行扩容时，可能会因为超时导致分区扩容不生效。针对未扩容成功的系统，需参考[扩容分区与文件系统（Linux）](resize-linux-cloud-disks.md)手动扩展分区。该方式只是扩展系统盘分区，不会影响系统的版本。
重新部署业务环境在新的操作系统中重新安装业务所需的软件、配置环境变量并迁移业务代码。
