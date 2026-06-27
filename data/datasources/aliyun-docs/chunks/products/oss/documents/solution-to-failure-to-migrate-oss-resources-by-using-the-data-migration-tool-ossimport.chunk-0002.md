## 解决方案
当迁移失败时，执行bash console.sh stat命令查看迁移任务的状态，如果JobState为failed，则迁移任务失败，请查看迁移失败的日志，根据日志中的报错信息参见以下内容进行解决，您可以在解决这些问题后使用retry命令进行重试：
说明：OSS迁移失败的日志路径为master/jobs/[$JobName]/failed_tasks/[$TaskName]/audit.log。
- [$JobName]：任务名字，字符串。
- [$TaskName]：Task名称。
