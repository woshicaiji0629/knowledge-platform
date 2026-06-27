## 大Key和热Key的统计排名机制
为避免对数据库造成额外的资源占用，本功能仅会统计客户端操作（读、写）过的Key，并仅保留和展示每种Key类型的Top数量，而不会实时扫描数据库中的所有Key。同时，在实例重启后或HA切换后，原先统计的TopKey信息将被清空，统计将重新开始，因此长时间未操作过的Key可能不会被纳入统计。如需了解数据库中所有Key的内存占用、数量分布等信息，请使用[离线全量](offline-key-analysis.md)[Key](offline-key-analysis.md)[分析](offline-key-analysis.md)功能。
