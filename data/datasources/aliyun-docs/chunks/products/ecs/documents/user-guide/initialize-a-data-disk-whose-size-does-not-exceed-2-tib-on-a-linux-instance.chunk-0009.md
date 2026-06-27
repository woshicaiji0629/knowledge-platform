## 配置开机自动挂载分区
若未配置开机自动挂载，每次重启都需手动执行命令挂载文件系统，才能恢复对盘内文件的访问。
为防止误操作，建议备份/etc/fstab文件。
sudo cp /etc/fstab /etc/fstab.bak
配置挂载信息
获取目标数据盘信息。
运行命令sudo lsblk -f，记录待配置云盘的目标设备名称、挂载目录和文件系统类型，后续编辑挂载信息时需要使用。
sudo lsblk -fNAME FSTYPE LABEL UUID MOUNTPOINT vda └─vda1 ext4 root 33b46ac5-7482-4aa5-8de0-60ab4c3a4c78 / vdb ext4 3d7a3861-da22-484e-bbf4-b09375894b4f └─vdb1 ext4 f1645951-134f-4677-b5f4-c65c71f8f86d /mnt vdc xfs 3d7a3861-da22-484e-bbf4-b09375894b4f /test
如果设备存在分区，目标设备名称为分区名称。示例中数据盘vdb目标设备名称为vdb1，挂载目录为/mnt，文件系统类型为ext4。
如果设备不存在分区，目标设备名称与设备名称一致。示例中数据盘vdc目标设备名称为vdc，挂载目录为/test，文件系统类型为xfs。
将挂载信息写入/etc/fstab。
将命令中的变量<目标设备名称>、<挂载目录>和<文件系统类型>，替换为从[上一步](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)中获取到的信息后执行。
重要
当参数设置为defaults,nofail时，即使挂载配置错误，实例也可正常启动。但由于系统不会报错，需特别关注自动挂载是否配置成功，防止数据写入错误设备。
sudo sh -c "echo `sudo blkid /dev/<目标设备名称> | awk '{print \$2}' | sed 's/\"//g'` <挂载目录> <文件系统类型> defaults 0 0 >> /etc/fstab"以配置目标设备名称为vdb1，挂载目录为/mnt，文件系统类型为ext4为例：sudo sh -c "echo `sudo blkid /dev/vdb1 | awk '{print \$2}' | sed 's/\"//g'` /mnt ext4 defaults 0 0 >> /etc/fstab"
验证自动挂载功能是否生效。
卸载当前挂载点。
<目标设备名称>需替换为[步骤](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linu
