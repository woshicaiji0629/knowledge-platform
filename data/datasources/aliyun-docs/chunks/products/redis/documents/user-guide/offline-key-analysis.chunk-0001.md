## 适用范围
单副本实例不支持该功能。
[磁盘型](../product-overview/essd-based-instances-1.md)实例在小版本2.7.0之前不支持此功能，可[升级小版本](update-the-minor-version.md)至最新版本使用此功能。
如果实例规格已发生变更，则不支持分析实例变更前的备份文件。
离线全量Key分析功能只支持分析Redis开源版数据结构和以下Tair自研数据结构：TairString、TairHash、TairGIS、TairBloom、TairDoc、TairCpc、TairZset，若存在其他Tair自研数据结构会导致分析任务失败。
