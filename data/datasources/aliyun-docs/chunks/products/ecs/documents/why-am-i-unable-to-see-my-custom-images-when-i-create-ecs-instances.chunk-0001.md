### 镜像和实例规格的特性不匹配

| 常见的不匹配原因 | 解决方案 |
| --- | --- |
| 镜像和实例规格的 NVMe 属性不匹配 选择了支持 NVMe 的实例规格，就只能选择支持 NVMe 的镜像（即镜像中包含了 NVMe 驱动且已支持 NVMe 属性）。 | 若目标镜像为自定义镜像，且业务需通过 NVMe 提升存储性能或实现云盘多重挂载。请确保该镜像安装了 NVMe 驱动，且已将镜像的属性 NVMe 驱动 设置为 支持 。更多信息，请参见 [如何为已有自定义镜像安装](adapt-linux-custom-images-to-nvme-based-system-disks.md) [NVMe](adapt-linux-custom-images-to-nvme-based-system-disks.md) [驱动？](adapt-linux-custom-images-to-nvme-based-system-disks.md) 。 说明 关于 NVMe 的更多介绍，请参见 [NVMe](user-guide/nvme-protocol.md) [协议概述](user-guide/nvme-protocol.md) 。 您可以通过 API 接口查询实例规格（ [DescribeInstanceTypes](developer-reference/api-ecs-2014-05-26-describeinstancetypes.md) ）和镜像（ [DescribeImages](developer-reference/api-ecs-2014-05-26-describeimages.md) ）是否支持 NVMe（字段为 NvmeSupport ）。 |
| 镜像和所选实例规格的启动模式不匹配 例如您选择了仅支持 UEFI 启动模式的安全增强型实例规格，则仅能选择 UEFI 版本的镜像。 | 若目标镜像为自定义镜像，可更换镜像的启动模式使之与目标实例匹配。具体操作，请参见 [实例启动模式](user-guide/instance-startup-mode.md) 。 |
