| sed 's/\"//g'` /mnt ext4 defaults 0 0 >> /etc/fstab"
验证自动挂载功能是否生效。
卸载当前挂载点。
<目标设备名称>需替换为[步骤](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)[3.a](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)中获取的目标设备名称。
sudo umount /dev/<目标设备名称>
重新加载/etc/fstab文件。
运行以下指令，系统将根据/etc/fstab配置文件，挂载尚未被挂载的文件系统。
sudo mount -a
如果产生报错，可通过sudo mv /etc/fstab.bak /etc/fstab指令，快速还原/etc/fstab文件。
查看挂载是否可以生效。
运行sudo lsblk命令，若回执中目标设备存在挂载目录（MOUNTPOINT）信息，表示配置成功。
