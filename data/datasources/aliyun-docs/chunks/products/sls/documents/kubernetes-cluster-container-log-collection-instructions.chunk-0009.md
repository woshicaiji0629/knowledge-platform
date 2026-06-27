## 日志采集原理
用户通过 kubectl 创建自定义资源 (CR)，定义采集规则。
loongcollector-operator 持续监听集群中CR资源的变化。
当检测到 CR 变化时，operator 将其转换为具体配置，并提交到日志服务。
loongcollector定时向日志服务发送心跳获取配置更新，拉取最新的采集配置并热加载。
loongcollector-ds 根据最新配置采集日志，并通过配置的接入点发送到 SLS。
