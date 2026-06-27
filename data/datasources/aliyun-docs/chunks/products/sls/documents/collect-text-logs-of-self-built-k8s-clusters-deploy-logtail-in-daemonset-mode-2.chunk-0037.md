##

| 关键字段详解 | 示例 # ...在 spec.config 下... inputs: - Type: input_file # 文件路径黑名单，排除指定条件的文件。路径必须为绝对路径，支持使用 * 通配符。 ExcludeFilePaths: - /var/log/*.log # 文件名黑名单，排除指定条件的文件。支持使用 * 通配符。 ExcludeFiles: - test # 目录黑名单，排除指定条件的文件。路径必须为绝对路径，支持使用 * 通配符。 ExcludeDirs: - /var/log/backup* |
| --- | --- |
| ExcludeFilePaths 文件路径黑名单，排除指定条件的文件。路径必须为绝对路径，支持使用 * 通配符。 |  |
| ExcludeFiles 文件名黑名单，排除指定条件的文件。支持使用 * 通配符。 |  |
| ExcludeDirs 目录黑名单，排除指定条件的文件。路径必须为绝对路径，支持使用 * 通配符。 |  |
