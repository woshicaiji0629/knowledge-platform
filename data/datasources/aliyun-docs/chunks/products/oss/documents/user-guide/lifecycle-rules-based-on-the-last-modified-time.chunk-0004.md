### 覆盖语义
PutBucketLifecycle为覆盖语义。例如，某个Bucket已配置了生命周期规则Rule1，您需要在Rule1基础上继续追加生命周期规则Rule2，您需要执行以下操作。
获取Rule1。
叠加Rule2。
更新规则为（Rule1+Rule2）。
