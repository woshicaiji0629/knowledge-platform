## 适用范围
请确保云盘满足以下任一条件：
云盘已挂载到ECS实例，且实例状态为运行中（Running）或已停止（Stopped）。
云盘状态为待挂载（Available），且曾挂载至ECS实例。
通过调用[DescribeDisks](../developer-reference/api-ecs-2014-05-26-describedisks.md)，查看AttachedTime字段可判断云盘是否存在挂载历史。
