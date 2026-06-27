## TairVector简介
TairVector采用多层Hash的数据结构，如下所示：TairVector提供了HNSW（Hierarchical Navigable Small World）和暴力搜索（Flat Search）两种索引算法：
HNSW：以图结构构建向量检索的索引，支持异步空间回收，可以在保证高查询精度的同时，均衡实时更新的性能表现。
暴力搜索：具有100%查询精度，插入数据速度快，适用于小规模数据集。
同时，TairVector支持欧式距离（Euclidean distance）、向量内积（Internal product）、余弦距离（Cosine distance）和Jaccard距离（Jaccard distance）等多种距离函数。相对于传统的向量检索服务，TairVector的优势如下：
所有数据均在内存中，支持实时更新索引，具有更短的读写时延。
优化内存数据结构，占用空间更小。
开箱即用，以云服务的方式整体申请即可使用，整体架构简单高效，没有复杂组件依赖。
支持向量检索与全文检索组合的混合检索。
支持创建标量（标签属性等）倒排索引，并提供先标量后向量的KNN检索特性。
发布记录
2022年10月13日随Tair内存型（兼容Redis 6.0）首次发布TairVector。
2022年11月22日发布6.2.2.0版本，新增支持Jaccard距离函数、TVS.GETINDEX命令支持统计每个索引的内存占用（index_data_size和attribute_data_size）。
2022年12月26日发布6.2.3.0版本，支持集群代理模式，新增FLOAT16的向量数据类型，新增TVS.MINDEXKNNSEARCH、TVS.MINDEXMKNNSEARCH命令。
2023年07月04日发布6.2.8.2版本，支持余弦距离、支持HNSW索引垃圾自动回收。
2023年08月03日发布23.8.0.0版本，支持对Index中的key级别设置TTL（新增TVS.HEXPIREAT、TVS.HPEXPIREAT等命令），支持对指定Key列表进行向量近邻查询（新增TVS.GETDISTANCE命令），支持全文检索（更新TVS.CREATEINDEX、TVS.KNNSEARCH等命令），可以实现向量检索与全文检索组合的混合检索。
2024年06月06日发布24.5.1.0版本，新增TVS.KNNSEARCHFIELD、TVS.MINDEXKNNSEARCHFIELD命令，支持在近邻查询时返回标签属性信息。
2024年07月22日发布24.7.0.0版本，支持在稀疏向量中使用HNSW索引。
