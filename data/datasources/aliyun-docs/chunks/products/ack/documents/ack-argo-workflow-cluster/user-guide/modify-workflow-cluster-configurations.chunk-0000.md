## 修改数据面虚拟交换机
创建 ACS 实例时，您可以指定多个交换机来覆盖多个可用区。系统会将请求随机分散到所有指定的可用区，以均衡负载。
登录[容器](https://csnew.console.aliyun.com/#/next/argowf)[Argo](https://csnew.console.aliyun.com/#/next/argowf)[工作流集群控制台](https://csnew.console.aliyun.com/#/next/argowf)，单击目标集群名称。
在集群信息页面中，选择基础信息页签，在下方找到关联云资源-交换机，单击编辑。
重要
指定多可用区（交换机）时，需要注意以下使用限制：
指定的多个交换机必须处于同一VPC。
最多可以指定10个交换机。
