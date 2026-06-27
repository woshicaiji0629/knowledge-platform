| 错误码 | 错误说明 | 解决方法 |
| --- | --- | --- |
| LOG_GROUP_WAIT_TOO_LONG_ALARM | 数据包从产生到发送的过程中等待的时间较长。 | 检查发送是否正常，或是否存在数据量超过默认配置、配额不足或网络存在问题。 |
| LOGFILE_PERMINSSION_ALARM | 无权限读取指定文件。 | 检查服务器 LoongCollector 的启动账号，建议以 root 方式启动。 |
| SPLIT_LOG_FAIL_ALARM | 行首正则与日志行首匹配失败，无法对日志做分行。 | 检查行首正则正确性。 若是单行日志可以配置为 .* 。 |
| MULTI_CONFIG_MATCH_ALARM | 默认情况下，一个文件只能匹配一个配置。当多个配置匹配同一个文件时，只会生效一个。 Docker 标准输出可以被多个配置采集。 | 删除多余的采集配置。 修改相关配置， [实现一个文件中的日志被采集多份](what-do-i-do-if-i-want-to-use-multiple-logtail-configurations-to-collect-logs-from-a-log-file.md) 。 详细的解决方案： [使用](https://help.aliyun.com/practice_detail/440520?spm=5176.2020520112.0.0.5f8634c0sLkkbX) [CloudLens](https://help.aliyun.com/practice_detail/440520?spm=5176.2020520112.0.0.5f8634c0sLkkbX) [排查](https://help.aliyun.com/practice_detail/440520?spm=5176.2020520112.0.0.5f8634c0sLkkbX) [iLogtail](https://help.aliyun.com/practice_detail/440520?spm=5176.2020520112.0.0.5f8634c0sLkkbX) [文件重复配置问题](https://help.aliyun.com/practice_detail/440520?spm=5176.2020520112.0.0.5f8634c0sLkkbX) 。 |
| REGEX_MATCH_ALARM | 完整正则模式下，日志内容和正则表达式不匹配。 | 复制错误信息中的日志样例重新匹配，并生成新的正则表达式。 |
| PARSE_LOG_FAIL_ALARM | JSON、分隔符等模式下，由于日志格式不符合定义而解析失败。 | 单击错误信息，查看失败的详细报错。 |
| CATEGORY_CON
