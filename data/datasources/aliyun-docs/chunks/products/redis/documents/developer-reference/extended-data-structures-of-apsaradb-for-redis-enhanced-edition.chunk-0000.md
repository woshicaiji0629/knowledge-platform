# Tair扩展数据结构概览
云数据库 Tair（兼容 Redis）与开源Redis相同，支持String、List、Hash、Set、Sorted Set、Stream等数据类型，能够满足大部分场景下的开发需求，但无法直接满足一些复杂场景的业务需求，需要通过开发大量代码、使用Lua脚本等复杂的方式实现。Tair（企业版）集成了多个自研的数据结构，包括[exString](tairsting-command.md)（包含[Redis String](cas-cad-command.md)[命令增强](cas-cad-command.md)）、[exHash](the-tairhash-command.md)、[exZset](tairzset-command.md)、[GIS](tairgis-command.md)、[Bloom](tairbloom-command.md)、[Doc](tairdoc-command.md)、[TS](the-tickets-command.md)、[Cpc](taircpc-command.md)、[Roaring](tairroaring-command.md)、[Search](tairsearch.md)和[Vector](tairvector.md)，从多方面扩展Redis的适用性，降低复杂场景下业务的开发难度，同时可以帮助您精简大量代码并提高业务整体性能，使您专注于业务创新。
说明
[内存型](../product-overview/dram-based-instances.md)（兼容Redis 7.0、6.0）兼容所有数据结构。
[内存型](../product-overview/dram-based-instances.md)（兼容Redis 5.0）兼容除TairVector以外的所有数据结构。
[持久内存型](../product-overview/persistent-memory-optimized-instances-1.md)兼容[exString](tairsting-command.md)（包含[Redis String](cas-cad-command.md)[命令增强](cas-cad-command.md)）、[exHash](the-tairhash-command.md)和[Cpc](taircpc-command.md)。
