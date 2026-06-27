_list": ["/tmp"] |
| host_path_blacklist | String | 全局主机路径黑名单，黑名单为子串匹配。 Linux 系统下多个子串以半角冒号（:）分隔。 Windows 系统下多个子串以半角分号（;）分隔。 例如 "host_path_blacklist" : "/volumes/kubernetes.io~csi/nas-" 表示禁止采集 NAS 挂载数据。 仅 Linux Logtail 1.8.0 及以上版本或 Windows Logtail 1.8.0.0 及以上版本支持该参数。 | "host_path_blacklist" : "/volumes/kubernetes.io~csi/nas-" |
| LOGTAIL_LOG_LEVEL | String | 日志打印级别，需通过环境变量进行配置。默认值：空，表示 info，可选值 trace、debug、info、warning、error 和 fatal。 仅 Linux Logtail 1.8.0 及以上版本或 Windows Logtail 1.8.0.0 及以上版本支持该参数。 | LOGTAIL_LOG_LEVEL=info |
| FORCE_RELEASE_STOP_CONTAINER_FILE | Boolean | 配置方式：仅支持通过环境变量方式进行配置。 功能描述：当该参数设置为 true 时，Logtail 会在业务容器退出时立即释放容器文件句柄。此操作可防止因文件句柄未释放而导致容器无法正常退出。 注意事项： 此时无法保证容器内数据采集的完整性。 建议在业务退出前增加几秒的延迟，以确保日志能够完整采集。 支持版本： Linux Logtail 2.1.6 及以上版本 | " FORCE_RELEASE_STOP_CONTAINER_FILE " : "true" |
| default_reader_flush_timeout | int | 最后一行日志完整性判定超时，默认值：60，单位：秒。 仅 Logtail 2.0.0 及以上版本支持该参数。 | " default_reader_flush_timeout " : 1 |
