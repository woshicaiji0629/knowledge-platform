achine-groups.md)[机器组无心跳](troubleshoot-the-errors-related-to-logtail-machine-groups.md)进行排查。
创建Logtail配置，单击下一步，创建Logtail配置。全局配置、输入配置和处理插件相同，处理配置中处理模式选择SPL。
全局配置

| 配置项 | 说明 |
| --- | --- |
| 配置名称 | Logtail 配置名称，在其所属 Project 内必须唯一。创建 Logtail 配置成功后，无法修改其名称。 |
| 日志主题类型 | 选择日志主题（Topic）的生成方式。更多信息，请参见 [日志主题](log-topics.md) 。 机器组 Topic ：设置为机器组的 Topic 属性，用于明确区分不同机器组产生的日志。 文件路径提取 ：设置为文件路径正则，则需要设置 自定义正则 ，用正则表达式从路径里提取一部分内容作为 Topic。用于区分不同源产生的日志。 自定义： 自定义日志主题。 |
| 高级参数 | 其它可选的与配置全局相关的高级功能参数，请参见 [创建](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) [Logtail](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) [流水线配置](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) 。 |

输入配置
