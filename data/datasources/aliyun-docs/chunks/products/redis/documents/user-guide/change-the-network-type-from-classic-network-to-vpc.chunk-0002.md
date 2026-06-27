## 常见问题
Q：切换专有网络时，无法选择交换机，是什么原因？
A：如果下拉框中没有可选的专有网络或交换机，说明实例所在的地域和可用区没有可用的专有网络或交换机。具体操作请参见[创建和管理专有网络](../../../vpc/documents/user-guide/create-and-manage-a-vpc.md)和[创建和管理交换机](../../../vpc/documents/user-guide/create-and-manage-vswitch.md)。
例如实例部署在华东1（杭州）可用区E，在选择专有网络后，如果没有可选的交换机则表示该专有网络在可用区E还未创建交换机（可能在其他可用区已创建）。请您先在华东1（杭州）可用区E创建交换机后重试。
Q：ECS实例与云数据库 Tair（兼容 Redis）在同一专有网络中，但位于不同的交换机（或不同可用区）时，能否通过专有网络连接云数据库 Tair（兼容 Redis）实例？
A：当ECS实例与云数据库 Tair（兼容 Redis）实例处于同一地域的同一专有网络内，即使它们位于不同交换机或可用区中，网络连通性也不会受到影响。请确保将ECS实例的内网IP地址添加到云数据库 Tair（兼容 Redis）实例的[IP](configure-whitelists.md)[白名单](configure-whitelists.md)中。
