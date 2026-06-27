## 步骤一：安装或升级安全策略管理组件
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择安全管理>策略管理。
在策略管理页面，根据页面提示安装或升级组件。
启用安全策略管理功能时，需安装以下组件。以下组件本身不收取费用，但会占用您的Pod资源。
gatekeeper组件：基于OPA策略引擎的Kubernetes策略准入控制器，便于您管理和应用集群内的OPA策略，实现命名空间标签管理等功能。
说明
仅支持使用ACK集群提供的gatekeeper组件。如您通过其他途径安装了gatekeeper组件，请卸载后重新安装。关于gatekeeper组件的版本发布信息，请参见[gatekeeper](../../product-overview/gatekeeper.md)。
日志采集组件：用于收集和检索不符合策略约束的拦截或告警事件。
policy-template-controller组件：基于阿里云策略模板开发的Kubernetes控制器，便于您更好地管理基于不同策略模板部署的策略实例和集群整体的治理状态。
