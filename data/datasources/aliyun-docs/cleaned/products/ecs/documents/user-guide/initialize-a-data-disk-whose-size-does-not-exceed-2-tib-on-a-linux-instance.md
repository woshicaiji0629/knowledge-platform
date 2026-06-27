# 初始化数据盘（Linux）-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance

# 初始化数据盘（Linux）
云盘创建并挂载至实例后，需初始化并挂载文件系统才可使用。
## 操作步骤
阿里云提供了两种方式：
通过控制台初始化（邀测）：在控制台利用云助手初始化并挂载文件系统，无需手动输入命令，操作便捷。
通过命令行初始化：登录实例手动输入命令初始化并挂载文件系统。该方式操作性强，适用范围广。
### 方法一：通过控制台初始化（邀测）
该功能处于邀测阶段，仅部分客户及场景支持开启检测功能，再次进入初始化界面。
在实例详情页的块存储页面中，开启云助手检测功能。
若无云助手检测功能，请[通过命令行初始化](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)云盘。
再次进入云助手初始化界面。
若云盘未初始化：单击目标云盘的系统内状态检测下的0/3检测已通过处，单击去初始化重新进入。
若云盘已初始化但未挂载文件系统：单击目标云盘的系统内状态检测下的1/3检测已通过处，单击去挂载文件系统重新进入。
未初始化当有扩容至64 TiB需求或页面提示云助手查询或执行失败、未安装云助手，请[通过命令行初始化](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)云盘。
云助手仅支持创建GPT分区、ext4文件系统。
重要
创建分区和文件系统将清除数据盘中所有数据，请确保云盘为空。
在云盘状态检测界面，配置参数并勾选风险提示后，单击开始执行。
| 参数 | 说明 |
| --- | --- |
| 大小 | 总分区大小不得超过云盘容量。 |
| 挂载点 | 应为以 / 开头的空路径，可自定义但不可重复。若目录非空，原有内容将被隐藏，可能影响业务。 |
| 添加分区 | 可根据需要单击 添加分区 ，创建多个分区，每块云盘最多支持添加 5 个分区。 |
当界面显示云盘检测完成，可以正常使用时，表示初始化并挂载文件系统已完成。
重要
当前为临时挂载，重启后失效。为使重启后数据仍可访问，建议登录实例[配置开机自动挂载分区](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)。
已初始化当页面提示云助手查询或执行失败、未安装云助手，请[通过命令行初始化](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)云盘。
在云盘状态检测界面，配置挂载点后，单击手动挂载。
| 参数 | 说明 |
| --- | --- |
| 挂载点 | 应为以 / 开头的空路径，可自定义但不可重复。若目录非空，会覆盖其下内容，导致原文件无法访问，可能影响业务。 |
当界面显示云盘检测完成，可以正常使用时，表示挂载文件系统已完成。
重要
当前为临时挂载，重启后失效。为使重启后数据仍可访问，建议登录实例[配置开机自动挂载分区](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)。
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
<设备名称>调整为[步骤](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)[2.a](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)中获取到的设备名称，<分区编号>为上一步获取的分区Number。
sudo parted /dev/<设备名称> align-check optimal <分区编号>
返回aligned表示对齐。[创建](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)[GPT](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)[分区时，显示](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)[not aligned](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)[分区未对齐如何解决？](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)
刷新磁盘分区表。
执行sudo partprobe，通知操作系统重新读取磁盘上的分区信息，以便能够识别新建的分区信息。
查看分区创建是否成功。
执行sudo lsblk查看新分区信息。若待初始化云盘存在正确分区信息，表明分区创建完成。接下来需要[创建文件系统](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)，才能使数据盘可用。
sudo lsblkNAME MAJ:MIN RM SIZE RO TYPE MOUNTPOINT vda 253:0 0 50G 0 disk └─vda1 253:3 0 49.8G 0 part / vdb 253:16 0 40G 0 disk └─vdb1 253:17 0 40G 0 part vdc 253:23 0 40G 0 disk └─vdc1 253:24 0 40G 0 part
示例中目标设备vdc的云盘容量，全部划至vdc1分区。
步骤二：创建文件系统
重要
创建文件系统会删除数据盘中数据，请确保云盘为空或已[手动创建单个快照](create-a-snapshot.md)备份数据。
记录待初始化云盘的目标设备名称，后续创建文件系统时需要使用。
sudo lsblk -fNAME FSTYPE LABEL UUID MOUNTPOINT vda └─vda1 ext4 root 33b46ac5-7482-4aa5-8de0-60ab4c3a4c78 / vdb └─vdb1 ext4 f1645951-134f-4677-b5f4-c65c71f8f86d vdc └─vdc1 vdd
如果设备存在分区，目标设备名称为分区名称。示例中数据盘vdc目标设备名称为vdc1。
如果设备不存在分区，目标设备名称与设备名称一致。示例中数据盘vdd目标设备名称为vdd。
创建文件系统。
ext4
将命令中的变量<目标设备名称>替换为[上一步](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)获取的目标设备名称后执行。
若有扩容至64 TiB需求时，请在命令中添加-i 65536，指定bytes-per-inode为65536。sudo mkfs -t ext4 /dev/<目标设备名称>
xfs
安装xfsprogs工具。
Debian或Ubuntu等类型，请使用sudo apt-get install -y <软件包名称>。sudo yum install -y xfsprogs
创建xfs文件系统。
将命令中的变量<目标设备名称>替换为[上一步](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)获取的目标设备名称后执行。
sudo mkfs -t xfs /dev/<目标设备名称>
检查文件系统是否创建成功。
运行sudo lsblk -f，若回执中目标设备的FSTYPE为所创建的目标文件系统类型，表示配置成功。接下来需要[挂载文件系统](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)，才能正常存储数据。
步骤三：挂载文件系统
创建并挂载目录。
sudo mkdir <挂载目录> && sudo mount /dev/<目标设备名称> <挂载目录>
| 参数 | 说明 |
| --- | --- |
| <目标设备名称> | 替换为创建文件系统时获取的 [目标设备名称](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md) 。 |
| <挂载目录> | 自定义 <挂载目录> ，应为以 / 开头的空路径，可自定义但不可重复。 重要 若目录非空，原有内容将被隐藏，会影响业务，请谨慎评估。 |
以将目标设备vdc1挂载至新创建的/data为例，需执行sudo mkdir /data && sudo mount /dev/vdc1 /data。
检查文件系统是否挂载成功。
运行sudo lsblk命令，若目标设备存在挂载目录（MOUNTPOINT）信息，表示文件系统挂载成功。
重要
当前为临时挂载，重启后失效。为使重启后数据仍可访问，建议[配置开机自动挂载分区](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)。
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
<目标设备名称>需替换为[步骤](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)[3.a](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)中获取的目标设备名称。
sudo umount /dev/<目标设备名称>
重新加载/etc/fstab文件。
运行以下指令，系统将根据/etc/fstab配置文件，挂载尚未被挂载的文件系统。
sudo mount -a
如果产生报错，可通过sudo mv /etc/fstab.bak /etc/fstab指令，快速还原/etc/fstab文件。
查看挂载是否可以生效。
运行sudo lsblk命令，若回执中目标设备存在挂载目录（MOUNTPOINT）信息，表示配置成功。
## 相关文档
若需扩容已有云盘，请参考[扩容云盘（Linux）](resize-linux-cloud-disks.md)。
若想为Windows实例初始化数据盘，请参考[初始化数据盘（Windows）](initialize-a-data-disk-up-to-2-tib-in-size-on-a-windows-instance.md)。
## 常见问题
- 如何选择分区类型和文件系统类型？
选择需要创建的分区格式：MBR分区不支持超过2 TiB的容量，如果云盘容量有2 TiB以上需求，请选择GPT分区。
创建分区有助于数据管理和逻辑隔离，如果无需创建分区可直接[选择需要创建的文件系统类型](initialize-a-data-disk-whose-size-does-not-exceed-2-tib-on-a-linux-instance.md)。
| 分区格式 | 最大分区容量 | 分区数量 | 分区说明 |
| --- | --- | --- | --- |
| GPT（推荐） | 18 EiB（1 EiB=1,048,576 TiB） 阿里云云盘支持的最大容量为 64 TiB。 | 128 | 所有分区均为主分区，不区分扩展分区与逻辑分区。 |
| MBR | 2 TiB | MBR 有以下分区形式： 4 个主分区 3 个主分区和 1 个扩展分区 | 分为主分区、扩展分区和逻辑分区三种类型。 扩展分区不可直接使用，需划分为若干个逻辑分区才能使用，逻辑分区数量无上限。 |
选择需要创建的文件系统类型。与xfs相比，ext4更适合处理小文件。
| 文件系统类型 | 最大文件大小 | 使用场景 |
| --- | --- | --- |
| ext4 | 16 TiB | 对小文件处理较好，适合大量小文件场景。如通用服务器与桌面系统、开发测试环境、小型日志服务器、内部管理系统，小型数据库服务器等场景。 |
| xfs | 8 EiB 阿里云云盘支持的最大容量为 64 TiB。 | 大规模目录和大文件性能更优。如大型数据库服务器（MySQL/PostgreSQL）、高性能计算（HPC）、存储密集型应用（如视频、图像存储）、高并发写入、大数据分析平台等场景。 |
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
$ sudo lsblk NAME MAJ:MIN RM SIZE RO TYPE MOUNTPOINT vda 253:0 0 50G 0 disk ├─vda1 253:1 0 2M 0 part ├─vda2 253:2 0 200M 0 part /boot/efi └─vda3 253:3 0 49.8G 0 part / vdb 253:16 0 40G 0 disk └─vdb1 253:17 0 40G 0 part
- /etc/fstab 配置错误，重启后实例无法启动怎么办？
可依照[Linux](../support/the-etc-fstab-file-of-the-linux-instance-is-incorrectly-configured-causing.md)[实例的/etc/fstab](../support/the-etc-fstab-file-of-the-linux-instance-is-incorrectly-configured-causing.md)[文件配置错误导致系统启动异常问题处理](../support/the-etc-fstab-file-of-the-linux-instance-is-incorrectly-configured-causing.md)，使用VNC进行远程连接实例，在紧急模式下，手动修改错误的挂载信息。
- 创建GPT分区时，显示not aligned分区未对齐如何解决？
运行以下命令，重新开始分区。本操作以数据盘/dev/vdb为例。
sudo parted /dev/vdb
在parted工具分区界面，输入以下内容，删除错误分区。
<错误分区number号>可以通过print指令查看。
重要
请在删除分区前，确保分区内无数据或者数据已备份。
rm <错误分区number号>
运行以下命令，保证开始位置与结束位置的单位为MiB、GiB，重新划分分区。以MiB为例：
mkpart data <开始容量>MiB <结束容量>MiB
- 创建文件系统时提示“Size of device /dev/vdb too big to be expressed”。
原因：若数据盘容量为16 TiB，需使用1.42及以上版本的e2fsprogs工具创建ext4文件系统。否则将报错：
mkfs.ext4: Size of device /dev/vdb too big to be expressed in 32 bits using a blocksize of 4096.
解决方案：安装高版本的e2fsprogs，例如1.42.8。
检查e2fsprogs当前的版本。
sudo rpm -qa | grep e2fsprogs
下载1.42.8版本的e2fsprogs。
也可以在[e2fsprogs](https://www.kernel.org/pub/linux/kernel/people/tytso/e2fsprogs/v1.42.8/?spm=a2c4g.11186623.2.14.Pb5baW)查看最新的软件包。sudo wget https://www.kernel.org/pub/linux/kernel/people/tytso/e2fsprogs/v1.42.8/e2fsprogs-1.42.8.tar.gz --no-check-certificate
编译高版本的工具。
解压软件包。
sudo tar xvzf e2fsprogs-1.42.8.tar.gz
进入软件包目录。
cd e2fsprogs-1.42.8
生成Makefile文件。
sudo ./configure
编译e2fsprogs。
sudo make
安装e2fsprogs。
sudo make install
检查是否成功更新版本。
sudo rpm -qa | grep e2fsprogs
- 如何通过API接口初始化数据盘？
调用[RunCommand](../developer-reference/api-ecs-2014-05-26-runcommand.md)接口向目标实例发送初始化指令，搭配调用[DescribeInvocations](../developer-reference/api-ecs-2014-05-26-describeinvocations.md)接口查询命令回执实现初始化并挂载文件系统操作。
- 安装初始化工具时，提示“404 Not Found”怎么解决？
CentOS 6、Debian 9/10/11操作系统已结束生命周期，需要先[切换](options-for-dealing-with-centos-linux-end-of-life.md)[Centos](options-for-dealing-with-centos-linux-end-of-life.md)[源地址](options-for-dealing-with-centos-linux-end-of-life.md)或[Debian 9/10/11](other-operating-systems.md)[源地址](other-operating-systems.md)后再进行工具安装
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
