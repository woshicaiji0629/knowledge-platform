ux-instance.md)。
请参阅[如何选择分区类型和文件系统类型](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)，了解不同分区的区别。
重要
创建分区将清除数据盘中所有数据，请确保云盘为空或已创建快照备份数据。
安装Parted工具。
Alibaba Cloud Linux、CentOS类型。
sudo yum install -y parted
Debian、Ubuntu类型。
sudo apt-get install -y parted
创建分区。
重要
请使用 MiB、GiB 等二进制单位设置分区起止位置（创建后会自动 4KiB 对齐），否则可能导致分区不对齐，影响云盘性能。
<设备名称>调整为[步骤](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)[2.a](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)中获取到的设备名称。
sudo parted /dev/<设备名称> --script mklabel gpt mkpart <自定义分区名称> <分区起始容量> <分区终止容量>单分区示例：将设备名称为vdc的云盘容量全部划分给单个分区，执行sudo parted /dev/vdc --script mklabel gpt mkpart primary 1MiB 100%。多分区示例：将设备名称为vdc的云盘容量划分给两个分区，第一个名为primary分区20G，剩余容量全都划分给第二个名为secondary的分区，执行sudo parted /dev/vdc --script mklabel gpt mkpart primary 1MiB 20GiB mkpart secondary 20GiB 100%。
检查分区是否对齐。
若分区未对齐，会影响云盘性能。
查看分区编号。记录回执中的Number，后续检查是否对齐时需要使用。
<设备名称>调整为[步骤](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)[2.a](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)中获取到的设备名称。
sudo parted /dev/<设备名称> print
检查是否对齐。
<设备名称>调整为[步骤](ini
