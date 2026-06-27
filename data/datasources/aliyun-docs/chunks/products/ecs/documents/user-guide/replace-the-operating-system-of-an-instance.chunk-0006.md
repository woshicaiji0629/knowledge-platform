## 常见问题
为什么更换操作系统时看不到某些镜像（包括自定义镜像）？
镜像与实例规格的特性不匹配：支持NVMe的实例规格只能选择支持NVMe的镜像，因此请确保镜像已安装NVMe驱动，并将镜像的NVMe驱动属性[修改](modify-the-attributes-of-a-custom-image.md)为支持，该镜像才会显示在镜像列表中；仅支持UEFI启动模式的实例规格只能选择UEFI版本的镜像，若为自定义镜像可更换镜像启动模式解决。
操作系统与实例规格处理器不兼容：部分实例规格（如8代实例）对支持的操作系统有限制。
[AMD](../compatibility-between-amd-instance-types-and-operating-systems.md)[实例规格与操作系统兼容性说明](../compatibility-between-amd-instance-types-and-operating-systems.md)
[Intel](../intel-instance-specifications-and-operating-system-compatibility.md)[实例规格与操作系统兼容性说明](../intel-instance-specifications-and-operating-system-compatibility.md)
[倚天处理器实例兼容的操作系统](the-migration-process.md)
Windows操作系统版本对CPU核数和内存大小有限制：使用Windows镜像时，实例规格内存需大于等于1 GiB。内存低于1 GiB的实例只能选择Linux镜像。
Red Hat镜像只能匹配经过红帽官方认证的实例规格。
部分裸金属、本地SSD型等实例对操作系统的驱动程序、内核有限制：需选择与实例规格处理器匹配的镜像。
更多详情，请参见[为什么创建](../why-am-i-unable-to-see-my-custom-images-when-i-create-ecs-instances.md)[ECS](../why-am-i-unable-to-see-my-custom-images-when-i-create-ecs-instances.md)[实例时看不到某些镜像？](../why-am-i-unable-to-see-my-custom-images-when-i-create-ecs-instances.md)
该文章对您有帮助吗？
反馈
