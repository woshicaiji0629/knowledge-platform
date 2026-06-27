### 通过SDK下载
当您需要下载更大数量的日志时，可通过SDK下载。
说明
SDK下载日志接口就是查询日志的接口。
Python SDK示例如下：
import os import time from aliyun.log import LogClient from aliyun.log import GetLogsRequest # 日志服务的服务接入点。 endpoint = 'cn-qingdao.log.aliyuncs.com' # 本示例从环境变量中获取AccessKey ID和AccessKey Secret。 accessKeyId = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_ID', '') accessKey = os.environ.get('ALIBABA_CLOUD_ACCESS_KEY_SECRET', '') # Project名称。 project = 'Project名称' # Logstore名称。 logstore = 'Logstore名称' client = LogClient(endpoint, accessKeyId, accessKey) request = GetLogsRequest("project1", "logstore1", fromTime=int(time()-3600), toTime=int(time()), topic='', query="*", line=100, offset=0, reverse=False) # 或者 # request = GetLogsRequest("project1", "logstore1", fromTime="2018-1-1 10:10:10", toTime="2018-1-1 10:20:10", topic='', query="*", line=100, offset=0, reverse=False) res = client.get_logs(request) res.log_print()
更多信息，请参见[SDK](developer-reference/overview-of-log-service-sdk.md)[参考概述](developer-reference/overview-of-log-service-sdk.md)。
该文章对您有帮助吗？
反馈
