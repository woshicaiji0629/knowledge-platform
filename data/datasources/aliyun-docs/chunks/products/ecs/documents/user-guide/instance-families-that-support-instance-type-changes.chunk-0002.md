择自定义镜像，单击检查操作链接。
阅读相关风险信息后，勾选申请放开限制的勾选框后，单击确定，等待1分钟左右。
3. 检查当前实例NVMe驱动与目标规格兼容性
从第8代及以后规格（如g8i、c8i、r8i、u2i、g8a、c8a、r8a、u2a等）开始，ECS 实例主要通过NVMe协议与云盘通信，必须安装相应的驱动。以下变配场景，需要检查原实例的NVMe驱动：
场景一：从7代及以下规格变配到8代及以上规格
原ECS实例必须安装NVMe驱动，或实例使用的镜像进行支持安装NVMe驱动。
场景二：当前实例规格为8代及以上
原ECS实例必须安装NVMe驱动才支持变配。
实例规格的“代系”信息可通过实例规格族名称判断。[实例规格命名规则](instance-specification-naming-and-classification.md)
检查&安装NVMe驱动的方法
在[ECS](https://ecs.console.aliyun.com/server/region)[控制台-实例](https://ecs.console.aliyun.com/server/region)找到待变配实例，选择>设置 NVMe 驱动状态。
如果已安装NVMe驱动，可以看到状态为已安装。
若未安装，单击一键安装，安装NVMe驱动，系统会自动修改NVMe驱动状态为已安装。
相关API
查询实例规格是否支持NVMe：调用[DescribeInstanceTypes](../developer-reference/api-ecs-2014-05-26-describeinstancetypes.md)，若支持，则NvmeSupport=required。
查询镜像是否支持NVMe：调用[DescribeImages](../developer-reference/api-ecs-2014-05-26-describeimages.md)，若支持，则NvmeSupport=supported。
4. 检查云盘类型兼容性
不同的实例规格支持的云盘类型不同。例如，g7规格族仅支持ESSD系列云盘。如果当前实例挂载了目标规格不支持的云盘，则不支持变更。
在变更规格的操作页面，如果存在云盘兼容性问题，系统会自动检测并提示您需要同时变更云盘类型。如下图所示，请留意相关提示和费用变化。
