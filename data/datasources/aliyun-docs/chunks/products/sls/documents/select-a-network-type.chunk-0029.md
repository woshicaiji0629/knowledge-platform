### Logtail采集配置文件（user_log_config.json）
user_log_config.json文件记录Logtail从日志服务获取的Logtail采集配置信息，文件类型为JSON，每次Logtail采集配置更新时会同步更新该文件。可通过user_log_config.json文件确认Logtail采集配置是否已经下发到服务器。Logtail采集配置文件存在，且内容与日志服务上的Logtail采集配置一致，表示Logtail采集配置已下发。
重要
除手动配置AccessKey信息、数据库密码等敏感信息外，不建议修改该文件。
文件路径
主机环境

| 操作系统 | Logtail | user_log_config.json 文件路径 |
| --- | --- | --- |
| Linux | Logtail（64 位程序） | /usr/local/ilogtail/user_log_config.json |
| Windows（64 位操作系统） | Logtail（64 位程序） | C:\Program Files\Alibaba\Logtail\user_log_config.json |
| Logtail（32 位程序） | C:\Program Files (x86)\Alibaba\Logtail\user_log_config.json 说明 Windows 64 位操作系统支持运行 32/64 位应用程序，但是出于兼容性考虑，在 Windows 64 位操作系统上，Windows 会使用单独的 x86 目录来存放 32 位应用程序。 |  |
| Windows （32 位操作系统） | Logtail（32 位程序） | C:\Program Files\Alibaba\Logtail\user_log_config.json |
