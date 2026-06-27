## 适用范围
要使用节省停机模式，ECS 实例必须同时满足以下所有条件：
计费方式：按量付费（包括抢占式实例）。
网络类型：仅支持专有网络实例。
实例规格：
不包含本地盘。例如，[大数据型（d](big-data-instance-families.md)[系列）](big-data-instance-families.md)、[本地](instance-families-with-local-ssds.md)[SSD](instance-families-with-local-ssds.md)[型（i](instance-families-with-local-ssds.md)[系列）](instance-families-with-local-ssds.md)等规格族不支持。可在[实例规格族](overview-of-instance-families.md)中的本地存储列查询是否包含本地盘。
不包含持久内存。例如，re6p、re6p-redis 等规格族不支持。可在[实例规格族](overview-of-instance-families.md)中的持久内存列查询是否包含持久内存。
