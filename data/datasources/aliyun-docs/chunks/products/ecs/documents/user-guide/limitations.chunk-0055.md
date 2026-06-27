## 部署集

| 限制项 | 限制 | 提升限额方式 |
| --- | --- | --- |
| 单个阿里云账号在特定地域下可拥有的部署集的最大数量 | 请根据配额 ID q_deployment-set-count 查看对应配额，具体操作请参见 [查看或提升云服务器 ECS](quota-management.md) [配额](quota-management.md) 。 | [查看或提升云服务器 ECS](quota-management.md) [配额](quota-management.md) |
| 单个部署集内能容纳的实例数量 | 部署集内能容纳的实例数量和您选择的部署策略有关，请参见 [部署策略](overview-43.md) 。 | 无 |
| 部署集创建专有宿主机 | 部署集不支持创建专有宿主机。 | 无 |
| 地域与可用区限制 | 实例与部署集必须在同一地域；策略为网络低时延的部署集内的实例，必须都在同一可用区。 | 无 |
| 部署集内能创建的实例规格 | 不同部署策略仅支持创建特定的实例规格族，您可以调用 [DescribeDeploymentSetSupportedInstanceTypeFamily](../api-describedeploymentsetsupportedinstancetypefamily.md) 指定部署策略来获取各部署策略支持的实例规格族。 | 无 |
| 合并部署集 | 部署集之间不支持相互合并。 | 无 |

关于部署集的更多内容，请参见[部署集](overview-43.md)。
