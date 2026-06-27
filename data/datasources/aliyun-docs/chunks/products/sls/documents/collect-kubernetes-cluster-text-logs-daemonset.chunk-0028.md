# 配置用户自定义标识,如目录不存在请手动创建 echo "user-defined-1" > /etc/ilogtail/user_defined_id
Windows：在C:\LogtailData目录下新建user_defined_id文件，并写入用户自定义标识。（如目录不存在，请手动创建）
如果用户标识和机器组标识均配置无误，请参考[LoongCollector（Logtail）机器组问题排查思路](troubleshoot-the-errors-related-to-logtail-machine-groups.md)进一步排查。
采集日志报错或格式错误
排查思路：这种情况说明网络连接和基础配置正常，问题主要出在日志内容与解析规则不匹配。您需要查看具体的错误信息来定位问题：
在Logtail配置页面，单击采集异常的LoongCollector（Logtail）配置名称，在日志采集错误页签下，单击时间选择设置查询时间。
在区域，查看错误日志的告警类型，并根据[采集数据常见错误类型](log-collection-error-type.md)查询对应的解决办法。
