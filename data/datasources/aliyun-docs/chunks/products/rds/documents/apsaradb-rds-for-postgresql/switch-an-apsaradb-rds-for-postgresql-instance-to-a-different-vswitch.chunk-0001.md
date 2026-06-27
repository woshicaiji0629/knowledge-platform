## 影响
切换过程会有30秒闪断，请确保应用程序具有重连机制。
切换虚拟交换机会造成虚拟IP（VIP）的变更，请您在应用程序中尽量使用[连接地址](configure-endpoints-2.md)进行连接，不要使用IP地址。
VIP的变更会短暂影响到[DMS](https://help.aliyun.com/zh/dms/product-overview/what-is-dms)、[DTS](https://help.aliyun.com/zh/dts/product-overview/what-is-dts#concept-26592-zh)的使用，变更结束后会自动恢复正常。
客户端的DNS缓存会导致只能读取数据，无法写入数据，请及时清理缓存。
