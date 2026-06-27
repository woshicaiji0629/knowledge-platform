## logtail-ds 组件配置
设置阿里云账号A为用户标识。
使用阿里云账号B登录[容器服务管理控制台](https://cs.console.aliyun.com)。
在集群列表页面中，单击目标集群。
在左侧导航栏中，选择配置管理>配置项。
选择命名空间为kube-system，然后在配置项列表中单击alibaba-log-configuration对应的编辑。
在编辑面板中，完成如下操作，然后单击确定。
在log-ali-uid配置项中增加阿里云账号A的ID，然后记录log-machine-group配置项的值（例如k8s-group-cc47****54428），在创建机器组时需设置用户自定义标识为该值。
多个账号之间使用半角逗号（,）相隔，例如17****397,12****456。
重启logtail-ds，使配置生效。
在logtail-ds详情页面，确认各个容器组的状态为Running且创建时间为您更新配置后的时间。
