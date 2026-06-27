## 修改MetricStore配置
在时序存储>日志库页签中，将鼠标悬浮在目标MetricStore上，选择修改。
在MetricStore属性页面中，单击修改。
基础信息
数据保存时间：参数说明请参见[创建](manage-a-metricstore.md)[MetricStore](manage-a-metricstore.md)。
自动分裂Shard：开启后支持自动分裂更多Shard以提供更大的写入能力，参见[管理](manage-shards.md)[Shard](manage-shards.md)。
最大分裂数：限制单Store最大可分裂的Shard个数，最多支持自动分裂至256个readwrite状态的Shard。
记录外网IP：打开记录外网IP开关后，日志服务自动把以下信息添加到日志的Tag字段中。
__client_ip__：日志来源设备的公网IP地址。
__receive_time__：日志到达服务端的时间，格式为Unix时间戳，表示从1970-1-1 00:00:00 UTC计算起的秒数。
Shard管理：
创建MetricStore时，默认为MetricStore创建2个Shard。在后续使用中，您可以根据业务需求分裂或合并Shard。具体操作，请参见[管理](manage-shards.md)[Shard](manage-shards.md)。
查询加速配置
Prometheus Query计算引擎默认不对执行结果进行缓存，每次查询都需全量读取所有数据并重新执行计算；并且标准计算引擎仅支持单节点上执行单协程化计算，在时间线多、查询时间段长、计算逻辑复杂等场景下性能较差。为提供更高效的PromQL计算，SLS时序计算引擎引入了全局缓存、并发计算两项计算增强能力。详细设计原理与配置方式参见[查询加速](speed-up-promql.md)。
写入配置
由于MetricStore对指标数据按时间顺序组织存储的特性，若时序库中乱序写入过多脏数据（例如，实时MetricStore中持续乱序写入数月前的数据、或因机器时钟问题致使生成非法数据等场景）会严重影响时序库的查询性能。
MetricStore支持过滤掉异常时间点的监控数据，在写入配置页面中配置左/右时间段窗口即可。“左/右区间”配置项的单位是秒，以数据到达SLS 服务时间为基准，合法数据写入时间为【数据到达时间-左区间，数据到达时间+右区间】，如超出范围，进行数据抛弃操作，当区间为【0,0】时，不进行数据写入时间范围规则判断。
说明
此特性仅对按Prometheus Remote Write协议写入的数据有效，采集接入方式参见[通过](collect-metric-data-from-prometheus-by-using-the-remote-write-protocol.md)[R
