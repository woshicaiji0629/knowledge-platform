### 创建快照
调用[CreateSnapshot](../api-createsnapshot.md)接口创建快照。
场景示例：为ESSD云盘d-bp14bjlwo3t3owin****创建一个快照（快照名称为demoname，描述为demo，保留时间：3天）。
请求示例
aliyun ecs CreateSnapshot \ --DiskId d-bp14bjlwo3t3owin**** \ --SnapshotName demoname \ --Description demo \ --RetentionDays 3
返回示例
{ "RequestId": "DFB0B01F-420D-4932-911E-7328920C2012", "SnapshotId": "s-bp1eyr9nxxoo9icj****" }
