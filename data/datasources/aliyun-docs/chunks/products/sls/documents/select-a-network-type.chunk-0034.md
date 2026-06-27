序，但是出于兼容性考虑，在 Windows 64 位操作系统上，Windows 会使用单独的 x86 目录来存放 32 位应用程序。 |  |
| Windows （32 位操作系统） | Logtail（32 位程序） | C:\Program Files\Alibaba\Logtail\ilogtail.LOG |

容器环境：
ilogtail.LOG文件存储在Logtail容器中，文件路径为/usr/local/ilogtail/ilogtail.LOG。
文件示例
$tail /usr/local/ilogtail/ilogtail.LOG [2018-09-13 01:13:59.024679] [INFO] [3155] [build/release64/sls/ilogtail/elogtail.cpp:123] change working dir:/usr/local/ilogtail/ [2018-09-13 01:13:59.025443] [INFO] [3155] [build/release64/sls/ilogtail/AppConfig.cpp:175] load logtail config file, path:/etc/ilogtail/conf/ap-southeast-1/ilogtail_config.json [2018-09-13 01:13:59.025460] [INFO] [3155] [build/release64/sls/ilogtail/AppConfig.cpp:176] load logtail config file, detail:{ "config_server_address" : "http://logtail.ap-southeast-1-intranet.log.aliyuncs.com", "data_server_list" : [ { "cluster" : "ap-southeast-1", "endpoint" : "ap-southeast-1-intranet.log.aliyuncs.com" } ]
