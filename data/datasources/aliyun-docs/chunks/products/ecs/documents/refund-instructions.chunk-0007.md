### 退订包年包月ECS实例
退订操作
准备工作。
在退订资源前，请务必确认即将退订的ECS实例内没有您所需的数据，或需要的数据已完成备份或迁移。
您可以[使用实例创建自定义镜像](user-guide/create-a-custom-image-from-an-instance.md)备份数据。
您可以把ECS实例内的数据迁移至另一台新购的ECS实例，操作参见[跨账号和同账号](https://help.aliyun.com/zh/smc/user-guide/migrate-servers-between-ecs-instances#task-2534321)[ECS](https://help.aliyun.com/zh/smc/user-guide/migrate-servers-between-ecs-instances#task-2534321)[实例间迁移](https://help.aliyun.com/zh/smc/user-guide/migrate-servers-between-ecs-instances#task-2534321)。
申请自助退订。
在[资源退订](https://billing-cost.console.aliyun.com/refund/)页面的退订资源页签下，单击选择普通云资源页签。
根据商品名称、实例ID及订单时间筛选，找到并勾选需退订的资源后，单击退订资源或批量退订资源发起退订。
仅非全额退订类型的资源支持批量退订，单次最多可操作50个实例。退订后资源保留说明
为避免误操作导致数据丢失，包年包月实例退款后进入退款后过期状态，相关资源会保留一定时间。若误操作退订，可在实例资源释放前，尽快前往访问[ECS](https://ecs.console.aliyun.com)[管理控制台](https://ecs.console.aliyun.com)，手动续费已退订实例。
重要
以下期限是最长保留时间，实际释放时间可能提前，建议您退订前做好数据备份或迁移。已操作退订的ECS实例续费恢复后，实例仍可能会产生数据丢失、固定公网IP变动等影响。
vCPU、内存、固定公网IP在退款后24小时内释放。
云盘在退款后15天内释放。
