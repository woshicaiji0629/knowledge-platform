all-the-cloud-assistant-agent.md)[Agent](install-the-cloud-assistant-agent.md)。
在控制台查看云助手Agent状态。
如果云助手Agent状态为正常，说明异常已解决。
如果云助手Agent状态还是异常，需要查看云助手日志来具体分析。
云助手默认日志路径：C:\ProgramData\aliyun\assist\<version>\log，<version>为云助手Agent的具体版本号。
该目录下重点关注aliyun_assist_main.log及其日期轮转备份文件（如aliyun_assist_main.log.20230912），通过查看这些日志文件定位云助手 Agent 异常原因。
