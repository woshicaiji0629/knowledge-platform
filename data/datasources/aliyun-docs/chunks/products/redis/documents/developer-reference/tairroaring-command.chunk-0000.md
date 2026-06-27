## TairRoaring简介
Bitmap（又名Bitset）是一种常用的数据结构，使用少量的存储空间来实现海量数据的查询优化。尽管Bitmap相比常规基于Hash结构的实现节省了大量内存空间，但是常规Bitmap对于稀疏场景下的数据存储仍不够友好，因此有了各种压缩Bitmap的实现（Compressed bitmap），Roaring Bitmap就是业界公认的一种更高效和均衡的Bitmap压缩存储的实现。
TairRoaring在此基础上完成大量优化：
通过2层索引和多种动态容器（Container），平衡了多种场景下性能和空间效率。
使用了包括SIMD instructions、Vectorization、PopCnt算法等多种工程优化，提升了计算效率，实现了高效的时空效率。
基于Tair提供的强大计算性能和极高的稳定性，为用户场景保驾护航。
典型场景
适用于直播、音乐、电商等行业，通过用户多维度标签，进行个性化推荐、精准营销等场景。
发布记录
重要
V2版本Breaking Change公告：
TR.RANGEINTARRAY：V1版本的TR.RANGEINTARRAY命令名称修改为V2版本的TR.RANGE，其内容无变化。
TR.SETRANGE：V1版本的TR.SETRANGE命令的返回值为OK，V2版本返回值为成功设置bit值为1的数量，其他内容无变化。
2021年9月13日发布TairRoaring V1版本，请将小版本升级至1.7.20及以上。
2022年3月11日发布TairRoaring V2版本，请将小版本升级至1.7.27及以上。
该版本优化了部分命令的实现，提升了性能。新增TR.SETBITS、TR.CLEARBITS等9个命令，向前兼容扩展2个命令，更新1个命令，更名1个命令。
2022年4月20日发布TairRoaring V2.2版本，请将小版本升级至1.8.1及以上。
该版本新增TR.JACCARD、TR.CONTAINS、TR.RANK命令，更新部分命令在key不存在时的返回错误（移除了ERR key not found）。
