## 在修改Logtail配置时添加SPL
登录[日志服务控制台](https://sls.console.aliyun.com)。
在Project列表区域，单击目标Project。
在日志存储>日志库页签中，单击目标日志库前面的>，依次选择数据接入>Logtail配置。
在Logtail配置列表中，单击目标Logtail配置后操作列的管理Logtail配置。
单击页面上方的编辑，在页面下方的处理配置区域，处理配置中处理模式选择SPL，然后单击保存。
全局配置

| 配置项 | 说明 |
| --- | --- |
| 配置名称 | Logtail 配置名称，在其所属 Project 内必须唯一。创建 Logtail 配置成功后，无法修改其名称。 |
| 日志主题类型 | 选择日志主题（Topic）的生成方式。更多信息，请参见 [日志主题](log-topics.md) 。 机器组 Topic ：设置为机器组的 Topic 属性，用于明确区分不同机器组产生的日志。 文件路径提取 ：设置为文件路径正则，则需要设置 自定义正则 ，用正则表达式从路径里提取一部分内容作为 Topic。用于区分不同源产生的日志。 自定义： 自定义日志主题。 |
| 高级参数 | 其它可选的与配置全局相关的高级功能参数，请参见 [创建](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) [Logtail](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) [流水线配置](https://next.api.aliyun.com/document/Sls/2020-12-30/CreateLogtailPipelineConfig?spm=api-workbench.api_explorer.0.0.4c5f31f27Lmdh1#request_params_desc) 。 |

输入配置
