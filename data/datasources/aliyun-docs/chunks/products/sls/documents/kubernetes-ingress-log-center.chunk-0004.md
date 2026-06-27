## 资产说明
所有资产都在您选择的Project下，Project内的资产如下：
Logstore
访问日志Logstore用于存储Kubernetes Ingress访问日志，该Logstore为您自定义创建的Logstore。
该Logstore默认开启索引，并配置部分字段的索引。您可以增加索引字段，修改索引后只对新数据生效。您还可以对历史数据重建索引。具体操作，请参见[重建索引](reindex-logs-for-a-logstore.md)。
您可以自定义修改日志存储时间。具体操作，请参见[修改](manage-a-logstore.md)[Logstore](manage-a-logstore.md)[配置](manage-a-logstore.md)。
巡检结果Logstore用于存储巡检结果。开通日志中心功能后，自动生成该专属Logstore，其名称为访问日志Logstore名称-metrics-result。
重要
请勿删除Kubernetes Ingress访问日志相关的Logstore，否则将无法正常采集日志到日志服务。
请勿删除访问日志Logstore中的部分字段的索引，否则指标转换会失败。
Metricstore
监控指标Metricstore用于存储聚合后的指标信息。开通日志中心功能后，自动生成该专属Metricstore，其名称为访问日志Logstore名称-metrics。
说明
监控指标Metricstore存储的是聚合后的指标，数据量相比原始访问日志大大降低，非常适用于长期存储。
聚合规则
