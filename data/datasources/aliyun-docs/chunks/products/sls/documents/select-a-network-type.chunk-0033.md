### Logtail运行日志（ilogtail.LOG）
ilogtail.LOG文件记录了Logtail的运行日志，日志级别从低到高分别为INFO、WARN和ERROR，其中INFO类型的日志无需关注。
如果采集异常，请先诊断采集错误，根据具体的错误类型和Logtail运行日志排查问题。更多信息，请参见[如何查看](user-guide/how-do-i-view-logtail-collection-errors.md)[Logtail](user-guide/how-do-i-view-logtail-collection-errors.md)[采集错误信息](user-guide/how-do-i-view-logtail-collection-errors.md)。
说明
如果因Logtail采集异常提交[工单](https://selfservice.console.aliyun.com/ticket/category/sls/today)时，请同时上传该日志。
文件路径
主机环境

| 操作系统 | Logtail | ilogtail.LOG 件路径 |
| --- | --- | --- |
| Linux | Logtail（64 位程序） | /usr/local/ilogtail/ilogtail.LOG |
| Windows（64 位操作系统） | Logtail（64 位程序） | C:\Program Files\Alibaba\Logtail\ilogtail.LOG |
| Logtail（32 位程序） | C:\Program Files (x86)\Alibaba\Logtail\ilogtail.LOG 说明 Windows 64 位操作系统支持运行 32/64 位应用程序，但是出于兼容性考虑，在 Windows 64 位操作系统上，Windows 会使用单独的 x86 目录来存放 32 位应用程序。 |  |
| Windows （32 位操作系统） | Logtail（32 位程序） | C:\Program Files\Alibaba\Logtail\ilogtail.LOG |
