## 常见问题
Q：怎么设置实例的Maxclients参数？
A：云数据库 Tair（兼容 Redis）不支持设置Maxclients参数，实例的最大连接数与实例规格有关，例如Tair内存型 4GB（tair.rdb.4g）实例的最大连接数为40000。您可以在[实例规格](../product-overview/overview-4.md)文档中找到各个规格的最大连接数信息。您可以通过[提升实例规格](change-the-configurations-of-an-instance.md)或[开启读写分离](enable-read-write-splitting.md)。提升实例的最大连接数。
