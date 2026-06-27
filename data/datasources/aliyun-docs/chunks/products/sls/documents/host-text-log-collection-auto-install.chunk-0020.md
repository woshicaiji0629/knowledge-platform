# 配置用户自定义标识,如目录不存在请手动创建 echo "user-defined-1" > /etc/ilogtail/user_defined_id
Windows：在C:\LogtailData目录下新建user_defined_id文件，并写入用户自定义标识。（如目录不存在，请手动创建）
如果用户标识和机器组标识均配置无误，请参考[LoongCollector（Logtail）机器组问题排查思路](troubleshoot-the-errors-related-to-logtail-machine-groups.md)进一步排查。
日志采集无数据
检查是否有增量日志：配置LoongCollector（Logtail）采集后，如果待采集的日志文件没有新增日志，则LoongCollector（Logtail）不会采集该文件。
检查机器组心跳状态：前往资源组>机器组页面，单击目标机器组名称，在机器组配置>机器组状态区域，查看心跳状态。
如果心跳为OK，则表示机器组与日志服务 Project 连接正常。
如果心跳为FAIL：参考[机器组心跳连接为](host-text-log-collection-auto-install.md)[fail](host-text-log-collection-auto-install.md)进行排查。
确认LoongCollector（Logtail）采集配置是否已应用到机器组：即使LoongCollector（Logtail）采集配置已创建，但如果未将其应用到机器组，日志仍无法被采集。
前往资源组>机器组页面，单击目标机器组名称，进入机器组配置页面。
在页面中查看管理配置，左侧展示全部Logtail配置，右侧展示已生效Logtail配置。如果目标LoongCollector（Logtail）采集配置已移动到右侧生效区域，则表示该配置已成功应用到目标机器组。
如果目标LoongCollector（Logtail）采集配置未移动到右侧生效区域，请单击修改，在左侧全部Logtail配置列表中勾选目标LoongCollector（Logtail）配置名称，单击移动到右侧生效区域，完成后单击确定。
采集日志报错或格式错误
排查思路：这种情况说明网络连接和基础配置正常，问题主要出在日志内容与解析规则不匹配。您需要查看具体的错误信息来定位问题：
在Logtail配置页面，单击采集异常的LoongCollector（Logtail）配置名称，在日志采集错误页签下，单击时间选择设置查询时间。
在区域，查看错误日志的告警类型，并根据[采集数据常见错误类型](log-collection-error-type.md)查询对应的解决办法。
