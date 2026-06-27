## 创建Helm应用
以通过控制台使用Helm部署Dify应用为例。确保ACK 集群至少有 2 核 CPU 和 4 GB 内存 的可用资源。
为 Dify 创建其依赖的 CNFS 和 NAS 存储类。
登录[容器服务管理控制台](https://cs.console.aliyun.com)，选择集群列表。在集群列表页面，单击目标集群名称，然后选择存储>存储类。
在存储类页面，单击使用YAML创建资源，将以下YAML内容复制到模板内，然后单击创建。
如果系统提示已存在同名资源，说明集群已自动创建CNFS及NAS存储类，可直接进行部署应用操作。 创建NAS存储会产生费用，详情请参见[NAS](https://help.aliyun.com/zh/nas/product-overview/billable-items/)[计费](https://help.aliyun.com/zh/nas/product-overview/billable-items/)。apiVersion: storage.alibabacloud.com/v1beta1 kind: ContainerNetworkFileSystem metadata: name: cnfs-nas-filesystem spec: description: "cnfs" type: nas reclaimPolicy: Retain # 仅支持Retain，删除CNFS时不会删除后端的NAS实例。 --- apiVersion: storage.k8s.io/v1 kind: StorageClass metadata: name: alibabacloud-cnfs-nas mountOptions: - nolock,tcp,noresvport - vers=3 parameters: volumeAs: subpath # 每个PVC都会在NAS下创建一个独立的子目录。 containerNetworkFileSystem: cnfs-nas-filesystem # 关联到上面定义的CNFS实例。 path: "/" provisioner: nasplugin.csi.alibabacloud.com reclaimPolicy: Retain allowVolumeExpansion: true # 可选：指定为true则允许对存储卷的目录配额进行扩容。
部署Dify应用。
在集群详情页面，选择应用>Helm。在Helm页面，单击创建。
基本信息：在Chart中搜索ack-dify，勾选搜索结果。
参数配置：Chart版本选择最新版。
访问Dify应用。
为ack-dify服务开启公网访问功能。
公网访问便于演示操作，如果在生产环境中部署，为了应用数据安全，建议开启访问控制功能。
选择网
