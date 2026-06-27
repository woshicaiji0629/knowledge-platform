## 限制未授权的跨账号连接
默认情况下，RAM 用户只要拥有vpc:CreateVpcPeerConnection与vpc:AcceptVpcPeerConnection权限，即可与任意账号建立 VPC 对等连接。如需仅允许 RAM 用户与组织内或指定的对端账号建立连接，避免敏感数据通过未授权的跨账号网络通道泄露，可以在 RAM 自定义策略中使用acs:TargetRDId、acs:TargetRDPath等全局 Condition Key，约束可连接的对端账号。
