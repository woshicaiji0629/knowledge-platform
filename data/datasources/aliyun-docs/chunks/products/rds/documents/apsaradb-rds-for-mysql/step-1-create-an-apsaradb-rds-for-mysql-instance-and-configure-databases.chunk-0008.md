oard/cn-hangzhou)，即可查看当前阿里云账号下所有数据库引擎的RDS实例总数量。在该页面您还可以看到实例的地域分布情况，以及各地域下正在运行中的RDS实例数量。
该页面同时展示即将到期和已过期的实例数量，并可在下方表格中按地域查看各状态实例的详细分布。
Q2：为什么创建实例后，实例列表看不到创建中的实例？

| 可能原因 | 说明 | 建议 |
| --- | --- | --- |
| 地域错误 | 您所在地域和您创建实例时选择的地域不一致。 | 在页面左上角切换地域。 |
| 可用区内资源不足 | 可用区内资源不足，导致创建失败。 创建失败您可以在 [订单列表](https://usercenter2.aliyun.com/order/list?pageIndex=1&pageSize=20) 里看到退款。 | 选择其它可用区后重试。 |
| RAM 权限策略禁止创建未加密的 RDS 实例 | 已配置 RAM 权限策略，禁止 RAM 用户创建未加密的 RDS 实例。 RAM 用户尝试创建高性能本地盘实例，实例创建失败（高性能本地盘实例无法在创建时设置磁盘加密）。 RAM 用户尝试创建云盘实例，但未设置云盘加密，实例创建失败。 更多信息，请参见 [通过](use-ram-policies-to-manage-the-permissions-of-ram-users-on-apsaradb-rds-instances.md) [RAM](use-ram-policies-to-manage-the-permissions-of-ram-users-on-apsaradb-rds-instances.md) [权限策略限制](use-ram-policies-to-manage-the-permissions-of-ram-users-on-apsaradb-rds-instances.md) [RAM](use-ram-policies-to-manage-the-permissions-of-ram-users-on-apsaradb-rds-instances.md) [用户权限](use-ram-policies-to-manage-the-permissions-of-ram-users-on-apsaradb-rds-instances.md) 。 | 创建实例时，存储类型选择云盘，选中云盘加密并设置密钥后重试。 |
