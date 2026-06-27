### 步骤一：日志接入（以 Session 日志为例）
Session 日志是安全审计的核心数据源，记录了每一轮对话、每一次工具调用、每一笔 Token 消耗。
前置准备
已[创建](manage-a-project.md)[Project](manage-a-project.md)（如openclaw-observability）且[已创建](manage-a-logstore.md)[LogStore](manage-a-logstore.md)。
确保 OpenClaw 所在 ECS / 自建服务器已[安装](loongcollector-installation-linux.md)[LoongCollector](loongcollector-installation-linux.md)。
接入流程
登录[日志服务控制台](https://sls.console.aliyun.com/)，选择右侧的快速接入数据并选择接入卡片，选择OpenClaw-会话日志，选择目标Project与LogStore。
在机器组配置下的源机器组列表中选择安装LoongCollector时创建的机器组添加到应用机器组列表中。
若机器组心跳异常请参考[心跳异常问题汇总排查](troubleshooting-of-abnormal-heartbeat-problems.md)。
在Logtail配置页，日志服务已自动填充内置的采集配置，若无需修改可直接单击下一步。
配置名称已默认配置。可按需修改。
其他全局配置下的日志主题类型已默认配置。
关于日志主题类型：LoongCollector支持从文件路径中自动提取topic和session_id，如文件路径经过自定义与预填不匹配需要自行调整。
文件路径已默认自动填充。
关于文本文件路径：预填的文件路径是假设用户在Linux主机使用非root用户默认安装的路径，如与实际情况不符，请注意修改。
处理模式中默认配置了处理插件组合。
关于时间解析：OpenClaw默认输出日志中的时区为0时区，如进行过自定义，请同步修改时间解析插件中的时区，避免时间错配。
在查询分析配置页，日志服务会自动生成内置索引与报表。后续可在查询分析与仪表盘中查看。
内置索引如下：
仪表盘如下：
OpenClaw 行为分析大盘
OpenClaw 审计大盘
OpenClaw 指标大盘
OpenClaw Token 分析大盘
