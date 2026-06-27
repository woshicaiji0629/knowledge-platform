MB |
| 1,000,000 | 2 MB | 2 MB | 4 MB |
| 10,000,000 | 16 MB | 32 MB | 32 MB |
| 100,000,000 | 128 MB | 256 MB | 256 MB |
| 1,000,000,000 | 2 GB | 2 GB | 4 GB |

创建超大容量的Key时，您需要关注错误率（error_rate）的精度，超大容量和超高精度的Key可能会因为实例内存不足而导致创建失败。
由于TairBloom只能插入新元素且无法删除已有元素，因此TairBloom的内存占用量只会增加不会减少。为防止TairBloom越来越大，甚至导致Redis内存溢出（Out Of Memory），向您提供如下使用建议。
拆分业务数据：拆分、细化业务数据，避免将大量数据存入一个TairBloom中，这样不仅会导致这个key过大，影响查询性能，同时也会由于这个key中插入了过多数据，大部分的查询流量都会请求到这个key所在的Redis实例上，从而造成热点key，甚至发生访问倾斜的情况。
请拆分业务数据，将数据分散到多个TairBloom中，若您的实例为集群实例，您可以将TairBloom分散到集群内的各个实例上，均衡内存容量与流量，充分发挥分布式集群的优势。
定期重建：如果业务允许，您可以定期重建TairBloom，通过DEL删除TairBloom，从后端数据库拉取数据并重建TairBloom，以控制TairBloom的大小。
您也可以在初期创建多个TairBloom，并采用多个TairBloom轮转切换的方式实现控制单个TairBloom的大小。该方案的优点为仅需创建一次TairBloom，无需频繁地重建TairBloom，缺点是需要创建多个TairBloom，会浪费部分内存空间。
