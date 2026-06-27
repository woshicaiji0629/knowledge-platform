# 使用CR实例管理采集配置
CRD（[CustomResourceDefinition](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/)）允许用户定义自定义资源类型，日志服务利用CRD定义了自己的资源类型，您可以通过创建CR（CustomResource）实例来管理采集配置。本文主要介绍日志服务的两类CRD（AliyunPipelineConfig和AliyunLogConfig）的区别和优势。
