。若执行 Lua 的实例账号权限为只读时， 仍会开启检查。 1 （默认）：检查。 |
| sentinel_compat_enable | 在集群架构代理模式或读写分离架构，开启或关闭哨兵（Sentinel）兼容模式，可选值： 1 ：开启。 0 （默认）：关闭。 |
| transfer_subscrible_to_psubscrible_enable | 开启或关闭 SUBSCRIBE 转 PSUBSCRIBE 功能，取值： 0 （默认）：关闭，二者不转换。 1 ：开启该功能，代理节点会将 SUBSCRIBE 转换成 PSUBSCRIBE 处理。 说明 当在 Lua 中使用了 PUB 或 SUB 类命令，导致在订阅的通道无法收到通知时，可以开启该功能。 |
