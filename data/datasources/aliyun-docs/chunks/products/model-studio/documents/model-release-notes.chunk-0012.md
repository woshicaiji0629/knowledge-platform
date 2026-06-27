| 日期 | 功能模块 | 功能点 | 功能说明 |
| --- | --- | --- | --- |
| 12 月 31 日 | 计费 | 千问 VL 模型降价 | 千问视觉理解模型降价调整，降幅最高可达 85%。具体说明请参考 [通义千问](qwen-vl-model-billing-notice.md) [VL](qwen-vl-model-billing-notice.md) [系列模型降价通知](qwen-vl-model-billing-notice.md) 。 |
| 12 月 27 日 | 模型调优 | qwen2.5-7b-instruct 支持 SFT 调优 | qwen2.5-7b-instruct 支持 SFT 全参和高效调优。 |
| 12 月 27 日 | 模型部署 | 模型部署支持按调用量计费 | 按调用量计费的方式支持部署 qwen2.5-7B、14B、32B、72B 和 qwen2-7B 调优后的模型。 |
| 12 月 24 日 | 模型广场 | 新增 Context Cache 功能 | Context Cache 可以在推理时减少重复的运算量，提升响应速度，在不影响回复效果的情况下降低您的使用成本，详情请参见 [上下文缓存](context-cache.md) 。 当前支持 qwen-plus 模型。 |
| 12 月 20 日 | OPENAI 接口兼容 | batch 支持任务通知 batch 支持的模型新增两个。 | 提交 Batch 任务之后，可以通过查询 Batch 任务接口获取状态和信息，Batch 任务执行时间有时会比较长，持续查询 Batch 任务效率较低，Batch 支持任务完成之后通知，减少不必要的任务查询，提高效率。Batch 任务完成通知支持两种方式：Callback 回调和 EventBridge 消息。详情参见 [OpenAI](batch-interfaces-compatible-with-openai.md) [兼容-Batch（文件输入）](batch-interfaces-compatible-with-openai.md) 。 支持的模型新增：qwen-vl-max、qwen-vl-plus、qwq-32b-preview，计费说明点击 [百炼控制台](https://bailian.console.aliyun.com/cn-beijing?tab=model#/model-market/all) 进行查看。 |
| 12 月 20 日 | 模型广场 | 新增 search_options 参数 | 配置联网搜索相关的参数，如搜索来源、搜索数量等。可用于 qwen-max、qwen-plus、qwen-turbo 模型，使用方法请参见 [千问](qwen-api-refere
