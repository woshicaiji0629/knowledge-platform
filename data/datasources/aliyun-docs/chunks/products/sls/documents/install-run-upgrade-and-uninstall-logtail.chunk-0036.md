## ACK集群升级方式
一般情况下，推荐您使用自动升级方式。如果您在logtail-ds的DaemonSet中或者在alibaba-log-controller的Deployment中修改过参数（例如环境变量），那么为了使您的修改不被重置，请使用手动升级方式。
自动升级
重要
自动升级会重置您在logtail-ds和alibaba-log-controller中手动修改的配置。
登录[容器服务管理控制台](https://cs.console.aliyun.com)。
在集群列表页面中，单击目标集群最右侧的更多>运维管理>组件管理
在日志与监控页签中，找到logtail-ds，然后单击升级。
在升级组件对话框中，单击确定。
重要
如果无法升级到最新版本的Logtail，说明您的Kubernetes集群版本太旧。请先升级Kubernetes集群或者使用手动升级方式。
执行升级操作后，您可以在容器服务管理控制台上查看logtail-ds pod状态。如果logtail-ds pod状态都为Running，表示升级成功。
手动升级
重要
手动升级不会根据最新版本的Logtail组件更新您的配置，部分特性优化可能不可用。
手动升级包括升级logtail-ds和alibaba-log-controller。一般情况下，您只需要升级logtail-ds即可获取新版本Logtail提供的采集能力。当您需要获取新版Logtail CRD方式的采集能力时，需要升级alibaba-log-controller。以下步骤以logtail-ds为例。
登录[容器服务管理控制台](https://cs.console.aliyun.com)。
在集群列表页面中，单击目标集群最右侧的更多>运维管理>组件管理
选择工作负载>守护进程集。
说明
当您要升级alibaba-log-controller时，请选择工作负载>无状态，然后在kube-system命名空间下，找到alibaba-log-controller，完成升级。
选择命名空间为kube-system，然后单击logtail-ds对应的编辑。
检查如下环境变量是否存在。
如果不存在ALIYUN_LOGTAIL_CONFIG、ALIYUN_LOGTAIL_USER_ID、ALIYUN_LOGTAIL_USER_DEFINED_ID这三个环境变量，可能是因为您的Logtail版本太旧，请升级。
单击镜像Tag对应的选择镜像Tag。
在镜像Tag对话框中，单击最新版本，然后单击确定。
在页面右侧，单击更新。
执行升级操作后，您可以在容器服务管理控制台上查看logtail-ds pod状态。如果logtail-ds pod状态都为Running，表示升级成功。
