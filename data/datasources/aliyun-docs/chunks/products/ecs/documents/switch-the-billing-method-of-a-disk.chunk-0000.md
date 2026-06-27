## 前提条件
需要转换的块存储设备为云盘，弹性临时盘及本地盘不能单独转换，只能随实例一起转换计费方式。具体操作，请查看[实例包年包月转按量付费](change-the-billing-method-of-an-instance-from-subscription-to-pay-as-you-go-1.md)和[实例按量付费转包年包月](change-the-billing-method-of-an-ecs-instance-from-pay-as-you-go-to-subscription-1.md)。
需要转换的计费方式为包年包月或按量付费。抢占式实例的基础计费方式或节省计划、存储容量单位包等优化成本的计费方式不支持转换。
请确保实例状态为运行中（Running）或已停止（Stopped）。
请确保云盘满足以下条件：
云盘状态为使用中（In_use）。
云盘未开启多重挂载功能，开启多重挂载功能的云盘不支持转换云盘计费方式。更多信息，请参见[云盘多重挂载功能](user-guide/enable-multi-attach.md)。
操作前5分钟内未成功修改过云盘基础计费方式。
