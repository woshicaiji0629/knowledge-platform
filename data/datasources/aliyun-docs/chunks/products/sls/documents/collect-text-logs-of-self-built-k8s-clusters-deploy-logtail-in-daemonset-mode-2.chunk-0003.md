/sls.console.aliyun.com/lognext/crd-generator)，可视化填写参数，自动生成标准YAML文件。
方式二：手动编写YAML
结合本文档提供的典型场景示例与配置流程，根据实际业务需求手动编写 YAML 文件。建议按本文结构逐步构建配置：从极简配置起步 → 添加处理逻辑 → 启用高级功能。
对于本文未覆盖的复杂场景或需要深度定制的字段，可进一步参考[AliyunPipelineConfig](kubernetes-cr-parameter-description.md)[参数说明](kubernetes-cr-parameter-description.md)，获取完整字段列表、取值规则及插件能力详情。
一个完整的采集配置通常包含以下部分：
