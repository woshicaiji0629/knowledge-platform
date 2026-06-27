## 准备工作
已创建名为web-project的Project。具体操作，请参见[管理](manage-a-project.md)[Project](manage-a-project.md)。
在Project（web-project）中创建名为website_log的源LogStore。具体操作，请参见[管理](manage-a-logstore.md)[LogStore](manage-a-logstore.md)。
已采集网站访问日志到源LogStore（website_log）。具体操作，请参见[数据采集概述](data-collection-overview.md)。
在Project（web-project）中创建目标LogStore（website_fail）。
如果您使用的是RAM用户，则需要先授予RAM用户数据加工操作权限。具体操作，请参见[授权](authorized-ram-user-operation-data-processing.md)[RAM](authorized-ram-user-operation-data-processing.md)[用户操作数据加工](authorized-ram-user-operation-data-processing.md)。
已配置源LogStore和目标LogStore的索引。具体操作，请参见[创建索引](create-indexes.md)。
说明
数据加工任务不依赖索引，但若不配置索引，将无法执行查询和分析操作。
