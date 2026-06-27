### spec.enableUpgradeOverride
可选，是否允许覆盖旧配置。用于解决新旧版采集配置之间的冲突问题，默认为false。
true：loongcollector-operator会对已有的AliyunLogConfig定义的采集配置进行覆盖升级。
false：采集配置存在冲突，AliyunPipelineConfig应用失败。
使用场景：当集群中存在AliyunLogConfig定义的采集配置、且与当前的AliyunPipelineConfig指向同一个采集配置时，就会发生冲突。
同一个采集配置的定义：
Project 相同
AliyunLogConfig：使用集群默认 Project 或spec.project
AliyunPipelineConfig：使用spec.project.name
采集配置名称相同
AliyunLogConfig：spec.logtailConfig.configName
AliyunPipelineConfig：metadata.name
覆盖升级过程：
新配置生效
ClusterAliyunPipelineConfig被应用，更新采集配置。
旧配置清理
如果更新成功，控制器会自动删除集群中对应的AliyunLogConfig资源。
完成迁移
完成从旧方式到新方式的平滑过渡。
该文章对您有帮助吗？
反馈
