## 排查容器日志采集是否异常
如果您在日志服务控制台的预览或LogStore查询页面未查到日志，则说明日志服务未采集到您的容器日志。请确认容器状态，然后执行如下检查。
重要
采集容器文件中的日志时，需注意如下事项。
Logtail只采集增量日志。如果下发Logtail配置后，日志文件无更新，则Logtail不会采集该文件中的日志。更多信息，请参见[读取日志](log-collection-process-of-logtail.md)。
只支持采集容器默认存储或挂载到本地的文件中的日志，暂不支持其他存储方式。
采集到日志后，您需要先创建索引，才能在LogStore中查询和分析日志。具体操作，请参见[创建索引](create-indexes.md)。
查看机器组心跳是否存在异常。具体操作，请参见[排查机器组心跳是否异常](what-do-i-do-if-an-error-occurs-when-i-use-logtail-to-collect-logs-from-containers.md)。
检查Logtail配置是否正确。
检查Logtail配置中的IncludeLabel、ExcludeLabel、IncludeEnv、ExcludeEnv等配置是否符合您的采集需求。
说明
其中此处的Label为容器Label，即Docker inspect中的Label，不是Kubernetes中的Label。
您可以将IncludeLabel、ExcludeLabel、IncludeEnv和ExcludeEnv配置临时去除，查看是否可以正常采集到日志。如果可以，则说明是上述参数的配置存在问题。
