## 将非加密云盘转换为加密云盘
已有的非加密云盘无法直接加密，需要利用加密自定义镜像或加密快照，通过更换操作系统或新建云盘间接实现。
系统盘
[为目标实例创建自定义镜像](create-a-custom-image-from-an-instance.md)。
[复制自定义镜像](copy-an-image.md)时选择加密复制，将非加密镜像复制为加密镜像。
选择任一方式，间接实现加密系统盘。
使用加密镜像[更换原](replace-the-operating-system-of-an-instance-1.md)[ECS](replace-the-operating-system-of-an-instance-1.md)[实例的操作系统](replace-the-operating-system-of-an-instance-1.md)。
[使用加密镜像创建新实例](create-an-ecs-instance-by-using-a-custom-image.md)。
数据盘
为数据盘[手动创建单个快照](create-a-snapshot.md)。
将快照[复制为加密快照](copy-a-snapshot.md)。
[使用加密快照创建数据盘](create-a-disk-from-a-snapshot.md)。
将创建的加密云盘[挂载](attach-a-data-disk.md)至原ECS实例。
