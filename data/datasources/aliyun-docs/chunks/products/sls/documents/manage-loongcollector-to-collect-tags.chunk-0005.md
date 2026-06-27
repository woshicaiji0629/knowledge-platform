### 输入插件相关Tag
该类Tag与输入插件强相关，它是输入插件配置的一部分，可通过输入配置的高级参数进行设置。您可以在创建采集配置或者修改采集配置时添加配置参数，本文以修改采集配置为例，创建采集配置请参见[创建采集配置](manage-logtail-configurations-for-log-collection.md)。
重要
目前，该功能仅适用于文件采集和新版标准输出采集插件。
登录[日志服务控制台](https://sls.console.aliyun.com)。在Project列表区域，单击目标Project。
单击日志存储下您的Logstore，在Logtail配置中添加Logtail配置，单击立即接入，本例使用正则-文本日志，表示将以正则匹配的方式解析文本日志。
在Logtail配置列表中，单击目标Logtail采集配置。
在Logtail配置页面，单击编辑。
在输入配置中单击其他输入配置，在高级参数后边单击，配置输入插件相关Tag。
重要
在输入配置设置FileOffsetKey，采集配置的自动生成索引会将该Tag字段（__file_offset__）设置成索引字段，收费标准请参见[计费说明](create-indexes.md)。如果无需对该某字段建立索引，可以删除该字段的索引，同时保留其 Tag 字段。具体操作，请参见[更新索引](create-indexes.md)。
该Tag不会在查询分析页面的上层显示，具有独特的属性和功能，并且Tag名称为__file_offset__。
在查询分析页面中，__file_offset__字段显示在左侧显示字段列表和日志详情区域中，其值为文件读取偏移量（如1465）。
{ "Tags": { "FileInodeTagKey": "__default__", "FilePathTagKey": "__default__" }, "FileOffsetKey":"__default__" }
