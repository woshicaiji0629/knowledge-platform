### 如何查看创建的自动快照？
策略执行后，会自动在[ECS](https://ecs.console.aliyun.com/snapshot)[控制台-快照](https://ecs.console.aliyun.com/snapshot)页面生成快照。
自动快照命名格式为auto2.0_yyyyMMdd_SnapshotPolicyId，快照来源为自动创建。其中：
auto2.0：表示自动快照。
手动快照和自动快照的区别请参见[手动快照和自动快照有什么区别？](../data-protection-and-recovery-faqs.md)
yyyyMMdd：创建快照的日期，y表示年、M表示月、d表示天。
SnapshotPolicyId：快照对应的自动快照策略ID。
例如，auto2.0_20241225_sp-2zeff8vy17u91rn5****表示2024年12月25日创建的一份自动快照，自动快照策略ID为sp-2zeff8vy17u91rn5****。
