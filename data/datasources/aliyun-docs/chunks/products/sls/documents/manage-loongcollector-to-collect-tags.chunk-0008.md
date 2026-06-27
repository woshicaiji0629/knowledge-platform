## 查看Tag
在Project列表区域，单击目标Project。
在对应的日志库右侧的图标，选择查询分析，查看当前LogStore的日志。
Tag字段展示在日志页面的最上方一行。
[Agent](manage-loongcollector-to-collect-tags.md)[相关](manage-loongcollector-to-collect-tags.md)[Tag](manage-loongcollector-to-collect-tags.md)
__tag__:sourceName：设置的Tag key为PipelineMetaTagKey.HOST_NAME，默认value为__tag__:__hostname__,设置value为__tag__:sourceName，代表来源主机名称。
__tag__:__host_id__：设置的Tag key为PipelineMetaTagKey.HOST_NAME。该参数value使用默认值__host_id__。
__tag__:__cloud_provider__：设置的Tag key为PipelineMetaTagKey.CLOUD_PROVIDER。该参数value使用默认值__cloud_provider__。
__tag__:__user_defined_id__：设置的Tag key为AGENT_TAG，即该参数仅适用于[用户自定义标识机器组](machine-group-overview.md)，而[IP](machine-group-overview.md)[地址机器组](machine-group-overview.md)不包含此参数。
[输入插件相关](manage-loongcollector-to-collect-tags.md)[Tag](manage-loongcollector-to-collect-tags.md)
__tag__:__inode__：设置的Tag key为Tags.FileInodeTagKey，该参数value使用默认值__inode__。
__tag__:__path__：设置的Tag key为Tags.FilePathTagKey，该参数value使用默认值__path__。
__file_offset__：设置的Tag key为FileOffsetKey，该参数value使用默认值__file_offset__。
重要
在输入配置设置FileOffsetKey，采集配置的自动生成索引会将该Tag字段（__file_offset__）设置成索引字段，收费标准请参见[计费说明](create-indexes.md)。如果无需对该某字段建立索引，可以删除该字段的索引，同时保留其 Tag 字段。具体操作，请参见[更新索引](create-ind
