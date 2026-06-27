-exceed-2-tib-on-a-linux-instance.md)获取的目标设备名称后执行。
sudo mkfs -t xfs /dev/<目标设备名称>
检查文件系统是否创建成功。
运行sudo lsblk -f，若回执中目标设备的FSTYPE为所创建的目标文件系统类型，表示配置成功。接下来需要[挂载文件系统](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)，才能正常存储数据。
步骤三：挂载文件系统
创建并挂载目录。
sudo mkdir <挂载目录> && sudo mount /dev/<目标设备名称> <挂载目录>
