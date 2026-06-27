### 配置的优先级
ossutil 按以下顺序读取配置：
命令行选项(如-i,-k,-e) >环境变量(如OSS_ACCESS_KEY_ID) >配置文件(~/.ossutilconfig)
说明
从 2.2.0 版本开始，支持通过--ignore-env-var 命令行选项忽略 OSS_为前缀的环境变量配置。
从 2.3.0 版本开始，--job、--parallel、--bigfile-threshold、--part-size、--write-buffer-size选项支持通过配置文件设置。在配置文件对应 profile 段下以key=value格式追加（例如job=10），或通过ossutil config set写入。命令行选项的优先级高于配置文件。
