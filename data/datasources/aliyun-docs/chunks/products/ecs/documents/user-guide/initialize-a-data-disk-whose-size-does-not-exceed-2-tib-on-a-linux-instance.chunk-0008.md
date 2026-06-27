| 参数 | 说明 |
| --- | --- |
| <目标设备名称> | 替换为创建文件系统时获取的 [目标设备名称](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md) 。 |
| <挂载目录> | 自定义 <挂载目录> ，应为以 / 开头的空路径，可自定义但不可重复。 重要 若目录非空，原有内容将被隐藏，会影响业务，请谨慎评估。 |

以将目标设备vdc1挂载至新创建的/data为例，需执行sudo mkdir /data && sudo mount /dev/vdc1 /data。
检查文件系统是否挂载成功。
运行sudo lsblk命令，若目标设备存在挂载目录（MOUNTPOINT）信息，表示文件系统挂载成功。
重要
当前为临时挂载，重启后失效。为使重启后数据仍可访问，建议[配置开机自动挂载分区](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)。
