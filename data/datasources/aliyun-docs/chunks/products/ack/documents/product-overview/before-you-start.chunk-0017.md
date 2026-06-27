### 存储相关高危操作

| 高危操作 | 影响 | 恢复方案 |
| --- | --- | --- |
| 控制台手动解挂云盘。 | Pod 写入报 IO Error。 | 重启 Pod，手动清理节点挂载残留。 |
| 节点上 umount 磁盘挂载路径 | Pod 写入本地磁盘。 | 重启 Pod。 |
| 节点上直接操作云盘。 | Pod 写入本地磁盘。 | 不可恢复。 |
| 多个 Pod 挂载相同云盘。 | Pod 写入本地磁盘或者报错 IO Error。 | 确保一个云盘给一个 Pod 使用。 重要 云盘为阿里云存储团队提供的非共享存储，只能同时被一个 Pod 挂载。 |
| 手动删除 NAS 挂载目录。 | Pod 写入报 IO Error。 | 重启 Pod。 |
| 删除正在使用的 NAS 盘或挂载点。 | Pod 出现 IO Hang。 | 重启 ECS 节点。重启具体操作，请参见 [重启](../../../ecs/documents/user-guide/restart-instances.md) [ECS](../../../ecs/documents/user-guide/restart-instances.md) [实例](../../../ecs/documents/user-guide/restart-instances.md) 。 |
