## 修改Tag值
重要
目前，该功能仅适用于文件采集和新版标准输出采集插件。
通过SPL处理插件管理Tag字段，修改Tag的值。使用SPL处理Tag字段时，需要遵循以下规则：
SPL将字段__tag__:作为 Tag 的标识，并在SPL处理过程中自动为所有Tag字段添加该前缀。因此，在编写SPL语句时，需确保字段名包含此前缀以正确引用 Tag 相关数据。
在SPL输出中，所有以Tag为前缀的字段均会被识别为Tag，这种方法可用于增加Tag。
本文在[修改采集配置时添加](use-logtail-spl-to-parse-logs.md)[SPL](use-logtail-spl-to-parse-logs.md)，以__tag__ :sourceName为例，为了更便捷地查询日志，可通过在日志采集配置中将值修改为user_module，从而用应用名称区分不同日志。创建采集配置时添加SPL请参见[创建采集配置时添加](use-logtail-spl-to-parse-logs.md)[SPL](use-logtail-spl-to-parse-logs.md)。
在Project列表区域，单击目标Project。
在日志存储>日志库页签中，单击目标日志库前面的>，依次选择数据接入>Logtail配置。
在Logtail配置列表中，单击目标Logtail配置后操作列的管理Logtail配置。
单击页面上方的编辑，在页面下方的处理配置区域，处理配置中处理模式选择SPL，然后单击保存。
SPL语句设置为：* | extend "__tag__:sourceName"='user_module'
在对应的日志库右侧的图标，选择查询分析，查看当前LogStore的日志。
__tag__:sourceName的字段值为user_module。
