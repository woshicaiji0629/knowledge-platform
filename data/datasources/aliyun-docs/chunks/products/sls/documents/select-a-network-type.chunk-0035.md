### Logtail插件日志（logtail_plugin.LOG）
logtail_plugin.LOG文件记录Logtail插件的运行日志，日志级别从低到高分别为INFO、WARN和ERROR，其中INFO类型的日志无需关注。
如果在诊断采集错误时，提示CANAL_RUNTIME_ALARM等错误，可以通过logtail_plugin.LOG文件排查。
说明
如果因插件异常提交[工单](https://selfservice.console.aliyun.com/ticket/category/sls/today)时，请在工单中上传该文件。
文件路径
主机环境

| 操作系统 | Logtail | logtail_plugin.LOG 文件路径 |
| --- | --- | --- |
| Linux | Logtail（64 位程序） | /usr/local/ilogtail/logtail_plugin.LOG |
| Windows（64 位操作系统） | Logtail（64 位程序） | C:\Program Files\Alibaba\Logtail\logtail_plugin.LOG |
| Logtail（32 位程序） | C:\Program Files (x86)\Alibaba\Logtail\logtail_plugin.LOG 说明 Windows 64 位操作系统支持运行 32/64 位应用程序，但是出于兼容性考虑，在 Windows 64 位操作系统上，Windows 会使用单独的 x86 目录来存放 32 位应用程序。 |  |
| Windows （32 位操作系统） | Logtail（32 位程序） | C:\Program Files\Alibaba\Logtail\logtail_plugin.LOG |
