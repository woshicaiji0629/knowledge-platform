### 为什么托管实例注册成功但显示状态异常？
若托管的实例显示注册成功，但云助手控制台显示云助手状态异常，可以查看云助手日志是否出现invalid timestamp错误。
说明
云助手默认日志路径如下，<version>为云助手Agent的具体版本号。
Linux实例
CoreOS操作系统：/opt/local/share/aliyun-assist/<version>/log
其他操作系统（Alibaba Cloud Linux、Ubuntu、Debian、RedHat、SUSE Linux Enterprise Server和OpenSUSE等）：/usr/local/share/aliyun-assist/<version>/log
Windows实例：C:\ProgramData\aliyun\assist\<version>\log
云助手日志中出现invalid timestamp错误的示例如下。其中code:400、errCode:BAD_REQUEST、errMsg:invalid timestamp为关键错误信息。
M/s1Kpi+KHyHOSytaIf6q7qPc8cGRXbaKR4ZtzJMOKTRoW1V1Y2t6cMaW7v9pZY9phJKeqQo4TMtAZasr/68EqS3xfaYmBRpvlnqvR6b3CR0336R1OQ== time="2023-09-04T16:54:37+08:00" level=info msg="https://cn-shanghai.axt.aliyuncs.com/luban/api/metrics {\"code\":400,\"errCode\":\"_BAD_REQUEST_\",\"errMsg\":\"invalid timestamp: 1693817677756,\"instanceId\":\"mi-sh03vea8ivh50qo\",\"requestId\":\"efb3ccca-7834-43e2-b0ce-1f5aacb37aad\" {\"eventId\":\"agent.startup\",\"category\":\"STARTUP\",\"subCategory\":\"\",\"eventLevel\":\"INFO\",\"eventTime\":\"1693817677755\",\"common\":\"\",\"arch\":\"amd64\",\"instanceId\":\"\",\"unknown\",\"osVersion\" \"Linux_#1 SMP Tue Mar 31 23:36:51 UTC 2020_x86_64\",\"virtualType\":\"unknown\",\"distribution\":\"\",\"
