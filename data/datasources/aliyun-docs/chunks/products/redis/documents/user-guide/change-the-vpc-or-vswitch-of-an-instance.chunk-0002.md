## 影响
切换过程中会有30秒闪断，请在业务低峰期操作并确保应用程序具有重连机制。
切换专有网络或交换机会造成虚拟IP地址（Virtual IP address）的变更，如果应用程序使用虚拟IP地址连接实例，会因为虚拟IP地址的变更导致连接失败。
说明
切换专有网络或交换机不会引起实例连接地址的变化（例如r-hp3bpn39cs1vu****.redis.hangzhou.rds.aliyuncs.com），推荐应用程序使用连接地址连接实例。
VIP的变更会短暂影响到[DMS](https://help.aliyun.com/zh/dms/product-overview/what-is-dms#task-1919582)的使用，变更结束后会自动恢复正常。
切换完成后，请及时清理客户端的缓存 ，否则可能出现只能读取数据，无法写入数据的情况。
