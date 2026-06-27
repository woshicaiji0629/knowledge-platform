## 工作原理
创建CR资源：用户通过 kubectl 提交ClusterAliyunPipelineConfigYAML 文件，定义采集规则。
控制器监听变化：loongcollector-operator 持续监听集群中CR资源的变更。
同步配置：当检测到 CR 变化时，operator 将其转换为具体配置，并提交到指定Project。
采集器拉取最新配置：loongcollector-ds定时向日志服务发送心跳获取配置更新，拉取最新的采集配置并热加载。
开始采集与上报：loongcollector-ds 根据最新配置采集日志，并通过配置的接入点发送到 SLS。
