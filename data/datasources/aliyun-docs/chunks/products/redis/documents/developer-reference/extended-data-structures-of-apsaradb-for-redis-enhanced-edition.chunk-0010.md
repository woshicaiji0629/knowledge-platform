## 常见问题
Q：云数据库 Tair（兼容 Redis）是否支持Redis stack server？
A：由于Redis开源协议限制，阿里云Redis开源版、Tair（企业版）均不支持Redis stack server。
为解决该问题，Tair（企业版）推出自研的扩展数据结构，包括[exString](tairsting-command.md)（包含[Redis String](cas-cad-command.md)[命令增强](cas-cad-command.md)）、[exHash](the-tairhash-command.md)、[exZset](tairzset-command.md)、[GIS](tairgis-command.md)、[Bloom](tairbloom-command.md)、[Doc](tairdoc-command.md)、[TS](the-tickets-command.md)、[Cpc](taircpc-command.md)、[Roaring](tairroaring-command.md)、[Search](tairsearch.md)和[Vector](tairvector.md)，整体比Redis stack server支持更多的数据结构，而部分数据结构在性能上也优于Redis stack server。
Q：如何对Tair扩展数据结构设置过期时间（TTL）？
A：其中exString、exHash、Cpc可通过自身命令直接设置TTL，而其他Tair扩展数据结构均可以通过EXPIRE | EXPIREAT <Keyname>命令（例如EXPIRE foo 60），设置该Key的过期时间。
Q：如何查询已购实例支持哪些扩展数据结构？
A：扩展数据结构的支持范围取决于实例版本和形态。登录Tair控制台，在实例详情页确认实例的版本类型（开源版或企业版）和形态，再对照以下说明确认支持范围：
开源版：仅支持标准Redis命令，不支持Tair扩展数据结构。
[内存型](../product-overview/dram-based-instances.md)：支持全部Tair扩展数据结构。
[持久内存型](../product-overview/persistent-memory-optimized-instances-1.md)：仅支持exString（包含Redis String命令增强）、exHash和Cpc。
磁盘型：不支持Tair扩展数据结构。
该文章对您有帮助吗？
反馈
