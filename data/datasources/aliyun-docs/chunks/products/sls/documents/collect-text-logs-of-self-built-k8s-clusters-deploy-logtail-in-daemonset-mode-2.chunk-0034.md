## 过滤
只采集符合条件的容器，多个条件之间为“且”的关系，任意条件为空表示忽略该条件；条件支持使用正则表达式。
核心配置：在[spec.config.inputs](kubernetes-cr-parameter-description.md)中配置ContainerFilters容器过滤相关参数。
