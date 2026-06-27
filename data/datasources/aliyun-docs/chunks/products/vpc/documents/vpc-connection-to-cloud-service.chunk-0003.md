## 网关终端节点
结合网关终端节点的终端节点策略与OSS的Bucket授权策略，可以降低未授权访问风险，实现双向鉴权：
源端控制：VPC侧仅允许该VPC访问指定Bucket，不允许该VPC访问其他Bucket。
目的端控制：OSS侧仅允许指定VPC访问该Bucket，不允许其他VPC访问。
