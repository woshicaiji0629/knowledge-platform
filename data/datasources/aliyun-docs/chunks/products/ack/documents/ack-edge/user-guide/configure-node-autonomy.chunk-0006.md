## 配置缓存组件
当前EdgeHub会将节点上的组件所需要的相关数据进行缓存，在云边断网时确保这些组件可以正常运行，磁盘缓存目录为/etc/kubernetes/cache。
说明
缓存的数据指的是与API Server进行交互的数据，比如Pod、ConfigMap等资源信息，不包含业务数据。
如果您有组件需要在边缘节点断网的情况下依赖API Server的数据信息来正常运行，可以按照如下步骤进行配置。
获取您的开发人员提供的User-Agent，如果是社区组件，可以在社区内进行查询。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，在左侧导航栏选择集群列表。
在集群列表页面，单击目标集群名称，然后在左侧导航栏，选择配置管理>配置项。
切换命名空间为kube-system，找到名称为edge-hub-cfg的ConfigMap，在右侧单击YAML 编辑。
将您的User-Agent添加到cache_agents配置项中，然后单击确定。
您可以登录节点，进入/etc/kubernetes/cache目录，查看是否有名为您的User-Agent的目录。
配置完成后，对应的组件和API Server之间交互的数据都会保存到节点的磁盘里。如果您开启了节点自治，组件将会从本地磁盘获取数据，从而确保正常运行。
