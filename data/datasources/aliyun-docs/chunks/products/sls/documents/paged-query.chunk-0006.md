## Java代码示例
更多信息，请参见[Java SDK](developer-reference/overview-of-log-service-sdk-for-java.md)[概述](developer-reference/overview-of-log-service-sdk-for-java.md)。
int log_offset = 0; int log_line = 500; String origin_query = "* | select count(1) , url group by url limit " while (true) { GetLogsResponse res4 = null; // 对于每个Offset，一次读取500行日志。如果读取失败，最多重复读取3次。 query = origin_query + log_offset + "," + log_line; for (int retry_time = 0; retry_time < 3; retry_time++) { GetLogsRequest req4 = new GetLogsRequest(project, logstore, from, to, topic, query); res4 = client.GetLogs(req4); if (res4 != null && res4.IsCompleted()) { break; } Thread.sleep(200); } System.out.println("Read log count:" + String.valueOf(res4.GetCount())); log_offset += log_line; if (res4.GetCount() == 0) { break; } }
该文章对您有帮助吗？
反馈
