## 步骤二：创建LoongCollector采集配置
登录[日志服务控制台](https://sls.console.aliyun.com)。
- 在接入数据区域，选择JSON-文本日志。
选择目标Project和LogStore，单击下一步。
创建机器组。
单击主机场景>ECS>创建机器组，在创建机器组面板中，选择与Project同地域的ECS实例，单击创建机器组。
如果ECS与日志服务不同地域，如果Zabbix是安装在自建集群或其他云厂商服务器上，需要手动安装。具体操作，请参见[安装采集器](loongcollector-installation-linux.md)。
等待安装完成，填写名称后单击确定。
点击下一步，如果心跳为FAIL，点击自动重试后等待两分钟左右直到心跳变为OK，点击下一步。此处自动安装LoongCollector同时也为您配置了IP类型机器组，如果您希望修改为用户自定义标识机器组，您可以参考[机器组与采集配置关联指南](machine-group-and-collection-configuration-association-guide.md)。
创建采集配置，单击下一步。
Zabbix监控数据为JSON类型，所以推荐使用JSON模式进行数据采集。其中日志路径需设置为您在[步骤一：配置数据存储路径](collect-zabbix-data.md)中设置的数据存储路径，其他参数详情请参见[使用](collect-logs-in-json-mode.md)[JSON](collect-logs-in-json-mode.md)[模式采集日志](collect-logs-in-json-mode.md)。
日志服务默认开启全文索引。您也可以根据采集到的日志，手动创建字段索引，或者单击自动生成索引，日志服务将自动生成字段索引。更多信息，请参见[创建索引](create-indexes.md)。
查询分析日志。
单击查询日志，系统将跳转至LogStore查询分析页面。
您需要等待1分钟左右，待索引生效后，才能在原始日志页签中，查看已采集到的日志。查询和分析日志的详细步骤，请参见[查询与分析快速指引](quick-guide-to-query-and-analysis.md)。
说明
如果需要查询日志中的所有字段，建议使用全文索引。如果只需查询部分字段、建议使用字段索引，减少索引流量。如果需要对字段进行分析（SELECT语句），必须创建字段索引。
该文章对您有帮助吗？
反馈
