## 步骤一：创建并配置ECS实例
- 登录[专有网络管理控制台](https://vpcnext.console.aliyun.com/vpc)。
在左侧导航栏，单击交换机。
选择交换机的地域，本文选择华东2（上海）。
在交换机页面，找到目标交换机，然后在操作列选择添加云产品>ECS实例。
在云服务器ECS购买页面的自定义购买页签下，创建2台ECS实例，并将IPv4 ECS修改实例名称为ECS01，将IPv6 ECS修改实例名称为ECS02，两台ECS实例绑定的安全组均需要放行80端口。具体操作，请参见[自定义购买实例](../../../../ecs/documents/user-guide/create-an-instance-by-using-the-wizard.md)。
单击查看本文ECS实例的配置

| ECS 实例名称 | 地域 | VPC 名称 | 交换机 | IP 版本 | 镜像 |
| --- | --- | --- | --- | --- | --- |
| ECS01 | 华东 2（上海） | VPC1 | 可用区 E 的 VSW1 | IPv4 | Alibaba Cloud Linux 3.2104 LTS 64 位 |
| ECS02 | 华东 2（上海） | VPC1 | 可用区 G 的 VSW2 | IPv6 说明 创建具有 IPv6 地址的实例时，需在 IPv6 处选中 免费分配 IPv6 地址 。 | Alibaba Cloud Linux 3.2104 LTS 64 位 |
