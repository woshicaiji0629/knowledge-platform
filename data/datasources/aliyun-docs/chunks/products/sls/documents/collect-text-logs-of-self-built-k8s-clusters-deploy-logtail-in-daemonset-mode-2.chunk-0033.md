##

| 关键字段详解 | 示例 |
| --- | --- |
| TopicType topic 类型，可选值： machine_group_topic ：机器组 topic，用于区分来自不同机器组的日志。 filepath ：文件路径提取，用于区分不同用户或应用产生的日志数据。 custom ：自定义，使用自定义的静态日志主题。 | 机器组 Topic spec: config: global: #将应用该配置的机器组 Topic 作为 Topic TopicType: machine_group_topic 文件路径提取 spec: config: global: TopicType: filepath # Topic 格式。当 TopicType 取值为 filepath 或 custom 时必填。 # 提取结果为__topic__: userA，__topic__: userB，__topic__: userC TopicFormat: \/data\/logs\/(.*)\/serviceA\/.* 自定义 spec: config: global: TopicType: custom # Topic 格式。当 TopicType 取值为 filepath 或 custom 时必填。 TopicFormat: customized:// + 自定义主题名 |
| TopicFormat Topic 格式。当 TopicType 取值为 filepath 或 custom 时必填。 |  |
