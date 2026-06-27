内容执行 JSON 展开时发生错误。 | 查看详细报错，检查所处理的内容以及相关的配置，确定是否有配置错误或不合法日志。 |
| CANAL_RUNTIME_ALARM | MySQL Binlog 插件运行时错误。 | 查看详细报错进一步排查。一般与所连接的 MySQL master 相关。 |
| CHECKPOINT_INVALID_ALARM | Checkpoint 解析失败。 | 查看详细报错，根据其中检查点内容（前 1024 个字节）以及具体错误信息进一步排查。 |
| DIR_EXCEED_LIMIT_ALARM | 同时监听的目录数超出限制。 | 检查当前 LogStore 的采集配置是否包含较多的目录数，合理设置监控目录最大深度。 详细的解决方案： [使用](https://help.aliyun.com/practice_detail/458757?spm=5176.2020520112.0.0.5f8634c0sLkkbX) [CloudLens](https://help.aliyun.com/practice_detail/458757?spm=5176.2020520112.0.0.5f8634c0sLkkbX) [排查文件、目录数超限问题](https://help.aliyun.com/practice_detail/458757?spm=5176.2020520112.0.0.5f8634c0sLkkbX) 。 |
| DOCKER_FILE_MAPPING_ALARM | 执行命令添加 Docker 文件映射失败。 | 查看详细报错，根据具体错误信息进一步排查。 |
| DOCKER_FILE_MATCH_ALARM | 无法在 Docker 容器中查找到指定文件。 | 查看详细报错，根据其中的容器信息以及查找的文件路径进一步排查。 |
| DOCKER_REGEX_COMPILE_ALARM | service_docker_stdout 插件错误，根据配置中的 BeginLineRegex 编译失败。 | 查看详细报错，检查其中的正则表达式是否正确。 |
| DOCKER_STDOUT_INIT_ALARM | service_docker_stdout 插件初始化失败。 | 查看详细报错，报错根据内容分为如下类型。 host...version...error ：检查配置中指定的 Docker Engine 是否可访问。 load checkpoint error ：加载检查点失败，如无影响可忽略此错误。 container... ：指定容器存在非法 Label 值，目前仅允许配置 stdout 和 stderr。请结合详细错误进行检查。 |
| DOCKER_STDOUT_START_ALARM | servic
