### 安全组快照
安全组快照可自动备份安全组规则。当安全组规则发生变更时，系统会自动创建快照。通过快照可恢复指定时间点的安全组规则，防止因误操作导致规则丢失。
重要
安全组规则变更后，系统将在5分钟后创建快照。若5分钟内发生多次变更，系统仅会基于首次变更前的规则创建一次快照。
安全组快照使用对象存储服务（OSS）存储备份数据。OSS为按量计费服务，使用安全组快照会产生相应的OSS存储和请求费用。
创建快照策略
前往[ECS](https://ecs.console.aliyun.com/securityGroupSnapshotPolicy)[控制台-安全组快照](https://ecs.console.aliyun.com/securityGroupSnapshotPolicy)，单击新建安全组快照策略。
在新建快照策略对话框中，配置以下信息：
策略名称：输入快照策略的名称。
策略状态：选择启用或禁用。仅当策略为启用状态时，才会为关联的安全组创建快照。
快照保留时间：设置快照保留天数，范围为1-30天，默认值为1天。超过保留时间的快照将被自动删除。
OSS 存储配置：配置用于存储快照数据的OSS Bucket。若Bucket名称留空，系统将使用默认Bucket。
单击确定。
首次创建快照策略时，系统会提示授权服务关联角色（SLR）ALIYUNSECURITYGROUPSNAPSHOTROLE以访问OSS存储桶。若该角色已存在，则无需重复授权。
关联安全组到快照策略
创建快照策略后，需将其与安全组关联，才能开始备份安全组规则。
关联安全组到快照策略时，系统会立即为该安全组创建一次快照。
前往[ECS](https://ecs.console.aliyun.com/securityGroupSnapshotPolicy)[控制台-安全组快照](https://ecs.console.aliyun.com/securityGroupSnapshotPolicy)，找到目标快照策略，在操作列单击关联安全组。
在关联安全组对话框中，选择要关联的安全组。
一个快照策略最多可关联10个安全组，一个安全组可关联多个策略不同的快照策略。
单击确定完成关联。
从快照恢复规则
重要
恢复操作会立即生效，当前所有规则将被快照中的规则完全覆盖。恢复后无法撤销。
前往[ECS](https://ecs.console.aliyun.com/securityGroup)[控制台-安全组](https://ecs.console.aliyun.com/securityGroup)页面，单击目标安全组ID进入安全组详情页。
在安全组详情页，切换至快照列表页签，找到目标快照，在操作列单击恢复快照。
在恢复安全组快照对话框中，确认恢复信息。
在入方向和出方向页签下，对比当前安全组规则和恢复后
