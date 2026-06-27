- 如何创建MBR分区？
重要
MBR不支持超过2 TiB容量，若有2 TiB以上容量需求，请选择GPT分区。
登录ECS实例。
访问[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)。在页面左侧顶部，选择目标资源所在的资源组和地域。
进入目标实例详情页，单击远程连接，选择通过Workbench远程连接。根据页面提示登录，进入终端页面。
创建MBR分区。
进入fdisk工具界面。
<设备名称>调整为[步骤](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)[2.a](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)中获取到的设备名称。
sudo fdisk -u /dev/<设备名称>
输入n，开始新建分区。
以创建一个主分区为例。输入p，创建一个主分区。
p表示主分区。
e表示扩展分区。
输入分区编号，按Enter键。
Partition number表示主分区编号，可以选择1-4。
输入起始扇区编号，按Enter键。
First sector是分区的起始扇区号。系统会显示可选的扇区范围，可在此区间内自定义输入，或按 Enter 键使用默认值。
输入最后一个扇区编号，按Enter键。
Last sector是分区的截止扇区号，系统会显示可选的扇区范围，可在该范围内自定义输入，或按 Enter 键使用默认值。截止扇区号必须大于起始扇区号。
输入p，查看Device字段确定规划的新分区。
输入w，将分区结果写入分区表中。
若分区操作有误，请输入q退出 fdisk，此前分区结果不保留，可按步骤重新分区。
执行sudo lsblk查看新分区信息。若待初始化云盘存在正确分区信息，表明分区创建完成。示例中设备vdb，存在1个分区vdb1。接下来需要[创建文件系统](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)，才能使数据盘可用。
$ sudo lsblk NAME MAJ:MIN RM SIZE RO TYPE MOUNTPOINT vda 253:0 0 50G 0 disk ├─vda1 253:1 0 2M 0 part ├─vda2 253:2 0 200M 0 part /boot/efi └─vda3 253:3 0 49.8G 0 part / vdb 253:16 0
