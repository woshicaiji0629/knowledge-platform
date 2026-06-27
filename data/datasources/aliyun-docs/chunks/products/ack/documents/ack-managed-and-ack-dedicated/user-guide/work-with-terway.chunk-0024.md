### TC Filter 规则

| 接口 | 方向 | 程序 | 优先级 | 功能 |
| --- | --- | --- | --- | --- |
| ethx | toContainer | VLAN Untag | 20000 | 去 vlan 标签 |
| ethx | toContainer | cil_from_netdev | 25000 | cilium svc/网络策略 |
| veth | toContainer | cil_to_container | 25000 | cilium svc/网络策略 |
| veth | fromContainer | cil_from_container | 25000 | cilium svc/网络策略 |
| ethx | fromContainer | cil_to_netdev | 25000 | cilium svc/网络策略 |
| ethx | fromContainer | VLAN Tag | 50001 | 添加 vlan 标签 |
