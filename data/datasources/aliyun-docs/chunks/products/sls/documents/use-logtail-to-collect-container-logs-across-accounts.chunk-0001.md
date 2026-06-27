## loongcollector 组件配置
设置阿里云账号A为用户标识。
使用阿里云账号B登录[容器服务管理控制台](https://cs.console.aliyun.com/)。
在集群列表页面，单击目标集群名称。
在左侧导航栏，选择应用>Helm。
在Helm页面，选择kube-system命名空间，单击loongcollector应用操作列的更新。
在更新发布的弹框的目标 Helm Chart 的参数配置（Values）区域：
配置aliUid：配置阿里云账号A的ID，多个账号之间使用半角逗号（,）相隔，例如17****397,12****456。
记录baseMachineGroupName的值：该值为机器组用户标识参数，在创建日志服务机器组时需设置用户自定义标识为该值，例如：k8s-group-cc47****54428。在 Helm Chart更新发布对话框的目标版本参数配置区域，accessKeyID和accessKeySecret字段以及clusterAgent字段为需要重点填写的配置项。确认参数后，勾选免责声明并单击确定完成更新。
勾选我已知晓更新时当前参数会被上述内容全量覆盖，并了解相关风险《免责声明》，单击确定更新发布loongcollector应用。
在左侧导航栏，单击工作负载>守护进程集，在kube-system命名空间下，单击loongcollector-ds进入详情页面，确认各个容器组的状态为Running且创建时间为您更新配置后的时间，以确保更新生效。
