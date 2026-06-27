### 控制台
登录[日志服务控制台](https://sls.console.aliyun.com)。在Project列表区域，单击目标Project。
在日志存储>日志库页签，单击+图标。
在创建Logstore页面中，进行配置后，单击确定。
LogStore类型：默认Standard。
计费模式：
[按使用功能计费（不支持更改）](pay-as-you-go.md)：按实际使用的每一项资源（如存储、索引、读写次数等）独立计费，并提供月度免费额度，便于小规模场景控制支出。
[按写入数据量计费](billing-items-in-the-pay-per-data-write-mode.md)：只为原始写入数据付费，30天内存储及主流功能免费使用，成本结构更简单、更划算。
快速判断：存储天数越接近30天，索引字段数量越接近全文索引越适合按写入数据量计费。
LogStore名称：在该Project内必须唯一，作为LogStore的唯一标识，创建后无法更改。
数据保存时间：默认为30天。
其余配置保持默认值即可。
LogStore全量参数列表（可展开）
