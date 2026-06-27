### Agent相关Tag
该类 Tag 不依赖任何输入插件，属于全局参数。您可以在创建采集配置或者修改采集配置时添加配置参数，本文以修改采集配置为例，创建采集配置请参见[创建采集配置](manage-logtail-configurations-for-log-collection.md)。
登录[日志服务控制台](https://sls.console.aliyun.com)。在Project列表区域，单击目标Project。
单击日志存储下您的Logstore，在Logtail配置中添加Logtail配置，单击立即接入，本例使用正则-文本日志，表示将以正则匹配的方式解析文本日志。
在Logtail配置列表中，单击目标Logtail采集配置。
在Logtail配置页面，单击编辑。
在全局配置中单击其他全集配置，在高级参数后边单击，配置Agent自身相关Tag。
{ "PipelineMetaTagKey": { "HOST_NAME": "sourceName", "AGENT_TAG": "__default__", "HOST_ID": "__default__", "CLOUD_PROVIDER": "__default__" } }

| 参数名 | 类型 | 是否必填 | 默认值 | 样例 | 说明 |
| --- | --- | --- | --- | --- | --- |
| PipelineMetaTagKey | object | 否 | 空 | {"HOST_NAME":"__hostname__"} | key 为 Tag 参数名，value 为 Tag 在日志中的字段名。当 value 为__default__时，取默认值。当 value 为空字符串时，表示删除 Tag。 可配置 Tag 如下： HOST_NAME：主机名。默认添加，默认值为"__hostname__"。 AGENT_TAG：用户自定义标识。默认添加，默认值为"__user_defined_id__"。该参数仅适用于 [用户自定义标识机器组](machine-group-overview.md) ，而 [IP](machine-group-overview.md) [地址机器组](machine-group-overview.md) 不包含此参数。 HOST_ID：主机 ID。默认不添加，默认值为"__host_id__"。 CLOUD_PROVIDER：云厂商。默认不添加，默认值为"__cloud_provider__"。 |
