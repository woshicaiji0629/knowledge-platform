## 步骤三：检查Logtail启动参数是否正确
ilogtail_config.json文件记录了Logtail的相关启动参数。
登录Logtail所在的机器。
查找ilogtail_config.json文件。
该文件在不同系统下的默认路径说明如下表所示：

| 操作系统 | Logtail | ilogtail_config.json 文件路径 |
| --- | --- | --- |
| Linux | Logtail（64 位程序） | /usr/local/ilogtail/ilogtail_config.json |
| Windows（64 位操作系统） | Logtail（64 位程序） | C:\Program Files\Alibaba\Logtail\ilogtail_config.json |
| Logtail（32 位程序） | C:\Program Files (x86)\Alibaba\Logtail\ilogtail_config.json |  |
| Windows （32 位操作系统） | Logtail（32 位程序） | C:\Program Files\Alibaba\Logtail\ilogtail_config.json |

打开ilogtail_config.json文件，确认配置文件参数是否正确。
{ "config_server_address" : "http://logtail.<config_region>.log.aliyuncs.com", "data_server_list" : [ { "cluster" : "<project地域>", "endpoint" : "<endpoint>" } ], ... }
如果ilogtail_config.json文件中的启动参数符合下述表格中的说明，则表示Logtail启动参数正确。
如果Logtail启动参数错误，请根据下述表格修改ilogtail_config.json文件，然后重启Logtail。具体操作，请参见[重启](troubleshoot-the-errors-related-to-logtail-machine-groups.md)[Logtail](troubleshoot-the-errors-related-to-logtail-machine-groups.md)。
Project地域信息请参见[开服地域](sls-supported-regions1.md)。
