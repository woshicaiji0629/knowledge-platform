## Tag分类
Tag字段类似于字段索引，包含key和value两部分。例如：__tag__:__inode__:263554，__tag__:__inode__为Tag名称（key），263554为Tag值（value）。
Tag根据来源主要分为两类：
Agent相关：与采集 Agent 本身相关，不依赖插件。 如 IP、主机名称等。
输入插件相关：依赖输入插件，由输入插件提供并富化相关信息到日志中。如文件 inode、读取偏移量、Pod 名称、Namespace、镜像名称等。
