确。
ilogtail_config.json文件中的config_server_address参数和data_server_list参数的值取决于安装时选择的安装命令，如果其中的地域和日志服务所在地域不一致或地址无法联通，说明安装时选择了错误的命令。这时Logtail无法正常采集日志，需重新安装。
文件路径
主机环境

| 操作系统 | Logtail | ilogtail_config.json 文件路径 |
| --- | --- | --- |
| Linux | Logtail（64 位程序） | /usr/local/ilogtail/ilogtail_config.json |
| Windows（64 位操作系统） | Logtail（64 位程序） | C:\Program Files\Alibaba\Logtail\ilogtail_config.json |
| Logtail（32 位程序） | C:\Program Files (x86)\Alibaba\Logtail\ilogtail_config.json 说明 Windows 64 位操作系统支持运行 32/64 位应用程序，但是出于兼容性考虑，在 Windows 64 位操作系统上，Windows 会使用单独的 x86 目录来存放 32 位应用程序。 |  |
| Windows （32 位操作系统） | Logtail（32 位程序） | C:\Program Files\Alibaba\Logtail\ilogtail_config.json |
