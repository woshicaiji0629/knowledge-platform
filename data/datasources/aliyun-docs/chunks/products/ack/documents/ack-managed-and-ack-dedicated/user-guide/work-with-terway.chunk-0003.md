## 重要说明
Terway 配置文件eni-config包含大量系统参数，修改、删除非允许的字段，可能会造成网络中断、Pod无法创建等异常。可修改配置参数声明在[自定义](terway-configuration-parameters.md)[Terway](terway-configuration-parameters.md)[配置参数](terway-configuration-parameters.md)。
Terway组件使用CRD来跟踪资源状态，若您误操作系统资源，可能会造成网络中断、Pod无法创建等异常。

| 资源名称 | 资源类型 | 用户是否可以操作 CRD | 用户是否可以操作 CR |
| --- | --- | --- | --- |
| podnetworkings.network.alibabacloud.com | 用户资源 | 否 | 是 |
| podenis.network.alibabacloud.com | 系统资源 | 否 | 否 |
| networkinterfaces.network.alibabacloud.com | 系统资源 | 否 | 否 |
| nodes.network.alibabacloud.com | 系统资源 | 否 | 否 |
| noderuntimes.network.alibabacloud.com | 系统资源 | 否 | 否 |
| *.cilium.io | 系统资源 | 否 | 否 |
| *.crd.projectcalico.org | 系统资源 | 否 | 否 |
