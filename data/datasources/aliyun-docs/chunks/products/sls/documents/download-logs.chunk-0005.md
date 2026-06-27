## 通过OpenAPI下载
[CreateDownloadJob - 创建日志下载任务](developer-reference/api-sls-2020-12-30-createdownloadjob.md)：
重要
超过单次下载的最大数量时，仅下载最大支持的数量。如果您需要下载全量日志，可缩小查询的时间范围，分多次下载。
单个阿里云账号最多支持3个并发下载操作（总下载次数无限制）。超出3个并发下载操作或多个RAM用户同时操作时，可能报错，此时您可等待其他操作完成后，再重试。
支持保存最近1天内的导出记录，超过1天的导出记录被自动清除。
在遇到网络错误或者查询不精确时，系统会自动重试下载任务。如果重试3次后，仍无法完成下载，则下载任务为失败状态。
OpenAPI 批量下载注意事项：
索引配置要求：调用 GetLogs API 或执行 SQL 查询时，需确保查询字段已在 LogStore 的索引属性中配置。如果查询字段未配置索引，将报ParameterInvalid错误。索引配置方法请参见[创建索引](developer-reference/api-sls-2020-12-30-createdownloadjob.md)。
下载指定字段：若只需下载特定字段（如 message），应在 SQL 中使用 SELECT 语句过滤，例如* | SELECT message，然后执行下载操作，以减少不必要的数据量。
