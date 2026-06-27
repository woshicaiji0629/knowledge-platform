## 注意事项
升级数据库版本时，实例将先升级备（Replica）实例或准备新实例，到达指定的执行时间后，执行主备切换或实例切换，完成升级操作。在实例切换阶段，实例最多将存在60秒以内的只读状态（等待数据完全同步），同时会发生秒级的连接闪断，请确保应用程序具备重连机制。
升级Proxy版本：
若实例为云原生版，实例中的Proxy节点将依次进行重启，所有连接会断开，请确保业务具备重连机制。
若实例为经典版，实例将采用热升级技术，新版本代理节点会根据旧版本代理节点的客户端连接信息来恢复连接，可实现连接不中断（可能出现毫秒级的延迟抖动）。但BLOCK、Transactions、Pub/Sub等类型的命令将会中断，请确保业务中的这些命令具备重连机制。若客户端使用直连地址连接实例，则所有命令都不受影响。
较新的小版本可能只在部分地域灰度发布。系统会自动检测实例的小版本，若控制台上小版本升级、代理版本升级按钮处于无法单击的状态，表示当前实例的小版本已经是最新。
除非特别说明，实例内核的小版本均会确保兼容性，因此您无需担心升级可能带来的兼容型问题，更多信息请参见[Tair](../support/apsaradb-for-redis-enhanced-edition-1.md)[小版本发布日志](../support/apsaradb-for-redis-enhanced-edition-1.md)、[Redis](../support/apsaradb-for-redis-community-edition.md)[开源版小版本发布日志](../support/apsaradb-for-redis-community-edition.md)与[Proxy](../support/apsaradb-for-redis-proxy-nodes.md)[小版本发布日志](../support/apsaradb-for-redis-proxy-nodes.md)。
警告
升级小版本不会改变实例的连接地址、数据、白名单配置以及已创建的账号密码等配置信息，但仍然建议您：
在业务低峰期进行升级。
确保应用程序具备重连机制。
