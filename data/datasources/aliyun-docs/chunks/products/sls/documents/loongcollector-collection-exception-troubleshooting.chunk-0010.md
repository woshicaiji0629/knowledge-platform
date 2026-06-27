TCH_ALARM | 完整正则模式下，日志内容和正则表达式不匹配。 | 复制错误信息中的日志样例重新匹配，并生成新的正则表达式。 |
| PARSE_LOG_FAIL_ALARM | JSON、分隔符等模式下，由于日志格式不符合定义而解析失败。 | 单击错误信息，查看失败的详细报错。 |
| CATEGORY_CONFIG_ALARM | 采集配置不合法。 | 常见的错误为正则表达式提取文件路径作为 Topic 失败。 详细的解决方案： [使用](https://help.aliyun.com/practice_detail/458811?spm=5176.2020520112.0.0.5f8634c0sLkkbX) [CloudLens](https://help.aliyun.com/practice_detail/458811?spm=5176.2020520112.0.0.5f8634c0sLkkbX) [排查](https://help.aliyun.com/practice_detail/458811?spm=5176.2020520112.0.0.5f8634c0sLkkbX) [iLogtail](https://help.aliyun.com/practice_detail/458811?spm=5176.2020520112.0.0.5f8634c0sLkkbX) [采集配置错误问题](https://help.aliyun.com/practice_detail/458811?spm=5176.2020520112.0.0.5f8634c0sLkkbX) 。 |
| LOGTAIL_CRASH_ALARM | 因超过服务器资源使用上限而崩溃。 | [修改](loongcollector-management-linux.md) [CPU、内存使用上限。](loongcollector-management-linux.md) |
| REGISTER_INOTIFY_FAIL_ALARM | 在 Linux 系统中注册日志监听失败，可能由于没有文件夹权限或文件夹被删除。 | 检查采集器是否有权限访问该文件夹，或者该文件夹是否被删除。 |
| DISCARD_DATA_ALARM | 配置使用的 CPU 资源不够或网络发送流控导致数据丢失 | [修改](loongcollector-management-linux.md) [CPU](loongcollector-management-linux.md) [使用上限或网络发送并发限制](loongcollector-management-linux.md) 。 |
| SEND_DATA_FAIL_ALARM | 发送数据失败，可能原因： 阿里云账号未创建 AccessKey。 客户端
