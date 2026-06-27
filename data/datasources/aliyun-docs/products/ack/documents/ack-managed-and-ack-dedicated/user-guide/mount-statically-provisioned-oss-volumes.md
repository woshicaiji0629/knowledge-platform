# 使用ossfs 1.0挂载静态OSS存储卷-容器服务 Kubernetes 版 ACK(ACK)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ack/ack-managed-and-ack-dedicated/user-guide/mount-statically-provisioned-oss-volumes

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/ack/documents/ack-managed-and-ack-dedicated/product-overview.md)

- [快速入门](products/ack/documents/ack-managed-and-ack-dedicated/getting-started.md)

- [操作指南](products/ack/documents/ack-managed-and-ack-dedicated/user-guide.md)

- [实践教程](products/ack/documents/ack-managed-and-ack-dedicated/use-cases.md)

- [安全合规](products/ack/documents/ack-managed-and-ack-dedicated/security-and-compliance.md)

- [开发参考](products/ack/documents/ack-managed-and-ack-dedicated/developer-reference.md)

- [服务支持](products/ack/documents/ack-managed-and-ack-dedicated/support.md)

[首页](https://help.aliyun.com/zh)

# 使用ossfs 1.0挂载静态OSS存储卷

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/kubernetes)

[我的收藏](https://help.aliyun.com/my_favorites.html)

ossfs 1.0 支持以静态存储卷的方式，通过PV/PVC 将已有的 OSS Bucket 挂载为持久化存储。该方式适用于并发读、少量随机写以及需要修改文件权限的通用场景，如挂载配置文件、图片或视频资源等。

## 适用范围

集群和CSI组件（csi-plugin和csi-provisioner）版本需符合要求：

- 

通过RRSA鉴权方式挂载时：集群版本为1.26及以上，CSI版本为v1.30.4及以上。

若在1.30.4之前的版本中使用了RRSA功能，需参见[【产品变更】CSI ossfs](products/ack/documents/product-overview/announcement-on-csi-oss-driver-upgrade.md)[版本升级与挂载流程优化](products/ack/documents/product-overview/announcement-on-csi-oss-driver-upgrade.md)增加RAM角色授权配置。

- 

通过AccessKey鉴权方式挂载时：为确保挂载稳定性，CSI版本建议不低于 v1.18.8.45。

如需升级集群，请参见[手动升级集群](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/update-the-kubernetes-version-of-an-ack-cluster.md)；如需升级组件，请参见[升级](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/install-and-upgrade-the-csi-plug-in.md)[CSI](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/install-and-upgrade-the-csi-plug-in.md)[组件](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/install-and-upgrade-the-csi-plug-in.md)。

自CSI v1.30.4-*版本起，[OSS](products/ack/documents/product-overview/announcement-on-csi-oss-driver-upgrade.md)[静态卷挂载已依赖](products/ack/documents/product-overview/announcement-on-csi-oss-driver-upgrade.md)[csi-provisioner](products/ack/documents/product-overview/announcement-on-csi-oss-driver-upgrade.md)[组件](products/ack/documents/product-overview/announcement-on-csi-oss-driver-upgrade.md)。

## 步骤一：选择鉴权方式（RRSA或AccessKey）并准备访问凭证

为确保集群能够安全、合规地访问OSS Bucket资源，需先配置一种鉴权机制。

- 

[RRSA](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/mount-statically-provisioned-oss-volumes.md)[鉴权方式](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/mount-statically-provisioned-oss-volumes.md)：为 Pod 动态授予临时、自动轮换的 RAM 角色，实现应用级别的精细化权限隔离，安全性较高。

- 

[AccessKey](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/mount-statically-provisioned-oss-volumes.md)[鉴权方式](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/mount-statically-provisioned-oss-volumes.md)：将静态、长期的密钥存储在 Secret 中。配置简单，但安全性较低。

重要

- 

在1.26及以上版本的集群中，为避免因AccessKey轮转导致的ossfs重挂载和业务重启，建议使用RRSA鉴权方式。

- 

本示例中集群与[OSS Bucket](products/oss/documents/user-guide/create-a-bucket-4.md)处于同一阿里云账号下。如需[跨账号挂载](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-oss-volumes-1.md)[OSS Bucket](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-oss-volumes-1.md)，建议使用RRSA鉴权方式。

## RRSA方式

### 1. 在集群中启用RRSA

- 

在[ACK](https://cs.console.aliyun.com)[集群列表](https://cs.console.aliyun.com)页面，单击目标集群名称，选择集群信息。

- 

在基本信息页签的安全与审计区域，单击RRSA OIDC右侧的开启，按照页面提示在业务低峰期完成RRSA的启用。

当集群状态由更新中变为运行中，表明RRSA已成功启用。

重要

启用RRSA功能后，集群内新创建的ServiceAccount Token的最大有效期将限制为12小时。

### 2. 创建RAM角色并授权

创建一个供 Pod 扮演的 RAM 角色，以通过 RRSA 鉴权来访问 OSS 存储卷。

展开查看步骤

- 

创建一个RAM角色。

- 

访问[RAM](https://ram.console.aliyun.com/roles/create)[控制台-创建角色](https://ram.console.aliyun.com/roles/create)页面，选择信任主体类型为身份提供商，然后切换编辑器，进入可视化编辑页面。

- 

选择主体为身份提供商，单击编辑，参见以下说明完成配置。

主要配置如下，其余参数保持默认即可。详见[创建](products/ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[OIDC](products/ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[身份提供商的](products/ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[RAM](products/ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)[角色](products/ram/documents/user-guide/create-a-ram-role-for-a-trusted-idp.md)。

- 

- 

- 

- 

- 

| 配置项 | 描述 |
| --- | --- |
| 身份提供商类型 | OIDC 。 |
| 身份提供商 | 选择 ack-rrsa-<cluster_id> 。其中， <cluster_id> 为集群 ID。 |
| 条件 | 手动添加 oidc:sub。 条件键：选择 oidc:sub 。 运算符：选择 StringEquals 。 条件值：默认输入 system:serviceaccount:ack-csi-fuse:csi-fuse-ossfs 。 ack-csi-fuse ：ossfs 客户端所在的命名空间，不支持自定义。 csi-fuse-ossfs ：ServiceAccount 名称。 如需修改，请参见 [如何在](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-oss-volumes-1.md) [RRSA](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-oss-volumes-1.md) [鉴权方式中使用指定的](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-oss-volumes-1.md) [ARNs](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-oss-volumes-1.md) [或](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-oss-volumes-1.md) [ServiceAccount？](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-oss-volumes-1.md) 。 |
| 角色名称 | 本示例为 demo-role-for-rrsa。 |


- 

创建权限策略。

本示例遵循最小权限原则，[创建一个自定义权限策略](products/ram/documents/create-a-custom-policy.md)，授予访问目标OSS Bucket的权限（OSS只读权限或OSS读写权限）。

- 

访问[RAM](https://ram.console.aliyun.com/policies/create)[控制台-创建权限策略](https://ram.console.aliyun.com/policies/create)页面，切换为脚本编辑，按照页面提示配置策略脚本。

若已有授权OSS权限的RAM角色，修改其信任策略即可复用，请参见[使用已存在的](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[RAM](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[角色并授权](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)。

## OSS只读权限策略

替换<myBucketName>为实际Bucket名称。{ "Statement": [ { "Action": [ "oss:Get*", "oss:List*" ], "Effect": "Allow", "Resource": [ "acs:oss:*:*:<myBucketName>", "acs:oss:*:*:<myBucketName>/*" ] } ], "Version": "1" }

## OSS读写权限策略

替换<myBucketName>为实际Bucket名称。{ "Statement": [ { "Action": "oss:*", "Effect": "Allow", "Resource": [ "acs:oss:*:*:<myBucketName>", "acs:oss:*:*:<myBucketName>/*" ] } ], "Version": "1" }

- 

（可选）使用KMS托管的指定CMK ID加密OSS Object时，还需为该角色配置KMS权限，详见[使用](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/encrypt-an-oss-volume.md)[KMS](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/encrypt-an-oss-volume.md)[托管的指定](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/encrypt-an-oss-volume.md)[CMK ID](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/encrypt-an-oss-volume.md)[加密](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/encrypt-an-oss-volume.md)。

- 

将该策略授权给RAM角色。

- 

访问[RAM](https://ram.console.aliyun.com/roles)[控制台-角色](https://ram.console.aliyun.com/roles)页面，在RAM角色列表的操作列，单击目标角色对应的新增授权。

- 

在权限策略区域，按照页面提示搜索并选择上一步创建的权限策略，并完成授权的新增。

## AccessKey方式

创建具有OSS访问权限的RAM用户并获取其AccessKey，使其拥有OSS Bucket的操作权限。

- 

创建RAM用户（如有，可跳过）。

访问[RAM](https://ram.console.aliyun.com/users/create)[控制台-创建用户](https://ram.console.aliyun.com/users/create)页面，按照页面提示完成RAM用户的创建，如登录名称、密码等。

- 

创建权限策略。

本示例遵循最小权限原则，[创建一个自定义权限策略](products/ram/documents/create-a-custom-policy.md)，授予访问目标OSS Bucket的权限（OSS只读权限或OSS读写权限）。

- 

访问[RAM](https://ram.console.aliyun.com/policies/create)[控制台-创建权限策略](https://ram.console.aliyun.com/policies/create)页面，切换为脚本编辑，按照页面提示配置策略脚本。

## OSS只读权限策略

替换<myBucketName>为实际Bucket名称。{ "Statement": [ { "Action": [ "oss:Get*", "oss:List*" ], "Effect": "Allow", "Resource": [ "acs:oss:*:*:<myBucketName>", "acs:oss:*:*:<myBucketName>/*" ] } ], "Version": "1" }

## OSS读写权限策略

替换mybucket为实际Bucket名称。{ "Statement": [ { "Action": "oss:*", "Effect": "Allow", "Resource": [ "acs:oss:*:*:<myBucketName>", "acs:oss:*:*:<myBucketName>/*" ] } ], "Version": "1" }

使用控制台创建PV时，还需拥有oss:ListBuckets权限。

{ "Effect": "Allow", "Action": "oss:ListBuckets", "Resource": "*" }

- 

（可选）使用KMS托管的指定CMK ID加密OSS Object时，还需为该RAM用户配置KMS权限，详见[使用](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/encrypt-an-oss-volume.md)[KMS](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/encrypt-an-oss-volume.md)[托管的指定](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/encrypt-an-oss-volume.md)[CMK ID](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/encrypt-an-oss-volume.md)[加密](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/encrypt-an-oss-volume.md)。

- 

将该策略授权给RAM用户。

- 

访问[RAM](https://ram.console.aliyun.com/users)[控制台-用户](https://ram.console.aliyun.com/users)页面，在RAM用户列表的操作列，单击目标用户对应的添加权限。

- 

在权限策略区域，按照页面提示搜索并选择上一步创建的权限策略，并完成授权的新增。

- 

为RAM用户创建AccessKey，以便后续将其存储为Secret，供PV使用。

- 

访问[RAM](https://ram.console.aliyun.com/users)[控制台-用户](https://ram.console.aliyun.com/users)页面，在RAM用户列表单击目标用户，然后在AccessKey区域，单击创建 AccessKey。

- 

按照页面提示，在对话框进行AccessKey的创建，获取并妥善保管其AccessKey ID和AccessKey Secret。

## 步骤二：创建PV

创建PV，在集群中“注册”已有的OSS Bucket。

## RRSA方式

- 

创建pv-oss-rrsa.yaml。

apiVersion: v1 kind: PersistentVolume metadata: # PV名称 name: pv-oss # PV标签 labels: alicloud-pvname: pv-oss spec: capacity: # 定义存储卷容量 storage: 10Gi # 访问模式 accessModes: - ReadOnlyMany persistentVolumeReclaimPolicy: Retain csi: driver: ossplugin.csi.alibabacloud.com # 与PV名称（metadata.name）一致 volumeHandle: pv-oss volumeAttributes: # 替换为实际Bucket名称 bucket: "your-bucket-name" # 挂载Bucket的根目录或指定子目录 path: / # Bucket所在地域的Endpoint url: "http://oss-cn-hangzhou-internal.aliyuncs.com" otherOpts: "-o umask=022 -o max_stat_cache_size=100000 -o allow_other" authType: "rrsa" # 此前创建或修改的RAM角色 roleName: "demo-role-for-rrsa" # OSS请求签名版本 sigVersion: "v4"

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 描述 |
| --- | --- |
| storage | 定义 OSS 存储卷容量。此值仅用于匹配 PVC。 |
| accessModes | 配置访问模式，支持 ReadOnlyMany 和 ReadWriteMany 。 选择 ReadOnlyMany 时，ossfs 将以只读模式挂载 OSS Bucket。 |
| persistentVolumeReclaimPolicy | PV 回收策略。当前 OSS 存储卷仅支持 Retain ，即删除 PVC 时，PV 和 OSS Bucket 中的数据不会随之删除。 |
| driver | 定义驱动类型。使用阿里云 OSS CSI 插件固定为 ossplugin.csi.alibabacloud.com 。 |
| volumeHandle | 需与 PV 名称（ metadata.name ）保持一致。 |
| bucket | 待挂载的 OSS Bucket。 |
| path | CSI 组件版本需为 v1.14.8.32-c77e277b-aliyun 及以上。 指定挂载点相对于 Bucket 根目录的路径。默认为 / ，即挂载整个 Bucket。 [ossfs](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/ossfs-release-notes.md) [版本](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/ossfs-release-notes.md) 小于 1.91 时，指定的 path 必须在 OSS Bucket 中预先存在。详见 [ossfs 1.91](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/introduction-of-new-functions-and-performance-pressure-measurement-of-ossfs-version-1-91-and-above.md) [及以上版本新增功能说明](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/introduction-of-new-functions-and-performance-pressure-measurement-of-ossfs-version-1-91-and-above.md) |
| url | 待挂载 OSS 的 [访问域名](products/oss/documents/user-guide/regions-and-endpoints.md) （Endpoint）。 挂载节点和 Bucket 处于相同地域，或已打通 VPC 网络时，使用内网地址。 挂载节点和 Bucket 不同地域时，使用外网地址。 不同访问端口的常见填写格式如下： 内网格式： http://oss-{{regionName}}-internal.aliyuncs.com 或 https://oss-{{regionName}}-internal.aliyuncs.com 。 内网访问端口格式 vpc100-oss-{{regionName}}.aliyuncs.com 已废弃，请及时切换。 外网格式： http://oss-{{regionName}}.aliyuncs.com 或 https://oss-{{regionName}}.aliyuncs.com 。 |
| otherOpts | 为 OSS 存储卷输入定制化参数，格式为 -o *** -o *** ，例如 -o umask=022 -o max_stat_cache_size=100000 -o allow_other 。 展开查看说明 umask ：更改 ossfs 读文件的权限。 例如， umask=022 可将 ossfs 文件的权限变更为 755，解决通过 SDK、OSS 控制台等其他方式上传的文件（默认权限为 640）在挂载点内权限不足的问题。推荐在读写分离或多用户访问时配置。 max_stat_cache_size ：设置元数据缓存的条目上限（例如 100000 ），在内存中缓存文件元信息来提升 ls 、 stat 等操作的性能。 但该缓存无法及时感知通过 OSS 控制台、SDK、ossutil 等方式对文件的修改，可能导致应用读取数据不一致。在对数据一致性有强要求时可将其设为 0 （禁用缓存），或通过 stat_cache_expire 参数调低缓存的失效时间，但会牺牲读取性能。 allow_other ：允许除挂载用户外的其他用户访问挂载点中的文件和目录，适用于需要让非挂载用户也能访问数据的多用户共享环境。 更多可选参数，请参见 [挂载选项说明](products/oss/documents/developer-reference/common-options.md) 、 [ossfs 1.0](products/oss/documents/developer-reference/best-practices.md) [配置最佳实践](products/oss/documents/developer-reference/best-practices.md) 。 |
| authType | 配置为 rrsa ，使用 RRSA 方式鉴权。 |
| roleName | 配置为此前创建或修改的 RAM 角色。 如需为不同 PV 配置不同权限，可创建不同的 RAM 角色，并在 PV 中配置不同的 roleName 。 |
| sigVersion | 请求 OSS 服务端的请求签名版本。 "v1" （默认）：使用 OSS [签名版本](products/oss/documents/developer-reference/ddd-signatures-to-urls.md) [1](products/oss/documents/developer-reference/ddd-signatures-to-urls.md) 。 "v4" ：使用 OSS [签名版本](products/oss/documents/developer-reference/add-signatures-to-urls.md) [4（推荐）](products/oss/documents/developer-reference/add-signatures-to-urls.md) 。 |


若默认的RRSA鉴权不满足需求（如使用非默认ServiceAccount或第三方OIDC），可通过修改PV配置来指定具体的ARN或ServiceAccount，详见[如何在](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-oss-volumes-1.md)[RRSA](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-oss-volumes-1.md)[鉴权方式中使用指定的](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-oss-volumes-1.md)[ARNs](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-oss-volumes-1.md)[或](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-oss-volumes-1.md)[ServiceAccount？](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-oss-volumes-1.md)。

- 

创建PV。

kubectl create -f pv-oss-rrsa.yaml

## AccessKey方式

## kubectl

- 

创建oss-secret.yaml，将[步骤一](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/mount-statically-provisioned-oss-volumes.md)获取的AccessKey存储为Secret，供PV使用。

apiVersion: v1 kind: Secret metadata: name: oss-secret # 需与应用所在的命令空间保持一致 namespace: default stringData: # 替换为此前获取的AccessKey ID akId: <your AccessKey ID> # 替换为此前获取的AccessKey Secret akSecret: <your AccessKey Secret>

- 

创建Secret。

kubectl create -f oss-secret.yaml

- 

创建pv-oss-ram.yaml。

apiVersion: v1 kind: PersistentVolume metadata: # PV 名称 name: pv-oss # PV 标签 labels: alicloud-pvname: pv-oss spec: capacity: storage: 10Gi accessModes: - ReadOnlyMany persistentVolumeReclaimPolicy: Retain csi: driver: ossplugin.csi.alibabacloud.com # 需与PV名称（metadata.name）保持一致 volumeHandle: pv-oss # 指定通过Secret对象来获取AccessKey信息 nodePublishSecretRef: name: oss-secret namespace: default volumeAttributes: # 替换为实际Bucket名称 bucket: "your-bucket-name" url: "http://oss-cn-hangzhou-internal.aliyuncs.com" otherOpts: "-o umask=022 -o max_stat_cache_size=100000 -o allow_other" path: "/"

- 

- 

- 

- 

- 

- 

- 

- 

- 

| 参数 | 描述 |
| --- | --- |
| storage | 定义 OSS 存储卷容量。此值仅用于匹配 PVC。 |
| accessModes | 配置访问模式，支持 ReadOnlyMany 和 ReadWriteMany 。 选择 ReadOnlyMany 时，ossfs 将以只读模式挂载 OSS Bucket。 |
| persistentVolumeReclaimPolicy | PV 回收策略。当前 OSS 存储卷仅支持 Retain ，即删除 PVC 时，PV 和 OSS Bucket 中的数据不会随之删除。 |
| driver | 定义驱动类型。使用阿里云 OSS CSI 插件固定为 ossplugin.csi.alibabacloud.com 。 |
| nodePublishSecretRef | 指定 Secret，以在挂载 PV 时提供 AccessKey 信息。 |
| volumeHandle | 需与 PV 名称（ metadata.name ）保持一致。 |
| bucket | 待挂载的 OSS Bucket。 |
| url | 待挂载 OSS 的 [访问域名](products/oss/documents/user-guide/regions-and-endpoints.md) （Endpoint）。 挂载节点和 Bucket 处于相同地域，或已打通 VPC 网络时，使用内网地址。 挂载节点和 Bucket 不同地域时，使用外网地址。 不同访问端口的常见填写格式如下： 内网格式： http://oss-{{regionName}}-internal.aliyuncs.com 或 https://oss-{{regionName}}-internal.aliyuncs.com 。 内网访问端口格式 vpc100-oss-{{regionName}}.aliyuncs.com 已废弃，请及时切换。 外网格式： http://oss-{{regionName}}.aliyuncs.com 或 https://oss-{{regionName}}.aliyuncs.com 。 |
| otherOpts | 为 OSS 存储卷输入定制化参数，格式为 -o *** -o *** ，例如 -o umask=022 -o max_stat_cache_size=100000 -o allow_other 。 展开查看说明 umask ：更改 ossfs 读文件的权限。 例如， umask=022 可将 ossfs 文件的权限变更为 755，解决通过 SDK、OSS 控制台等其他方式上传的文件（默认权限为 640）在挂载点内权限不足的问题。推荐在读写分离或多用户访问时配置。 max_stat_cache_size ：设置元数据缓存的条目上限（例如 100000 ），在内存中缓存文件元信息来提升 ls 、 stat 等操作的性能。 但该缓存无法及时感知通过 OSS 控制台、SDK、ossutil 等方式对文件的修改，可能导致应用读取数据不一致。在对数据一致性有强要求时可将其设为 0 （禁用缓存），或通过 stat_cache_expire 参数调低缓存的失效时间，但会牺牲读取性能。 allow_other ：允许除挂载用户外的其他用户访问挂载点中的文件和目录，适用于需要让非挂载用户也能访问数据的多用户共享环境。 更多可选参数，请参见 [挂载选项说明](products/oss/documents/developer-reference/common-options.md) 、 [ossfs 1.0](products/oss/documents/developer-reference/best-practices.md) [配置最佳实践](products/oss/documents/developer-reference/best-practices.md) 。 |
| path | CSI 组件版本需为 v1.14.8.32-c77e277b-aliyun 及以上。 指定挂载点相对于 Bucket 根目录的路径。默认为 / ，即挂载整个 Bucket。 [ossfs](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/ossfs-release-notes.md) [版本](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/ossfs-release-notes.md) 小于 1.91 时，指定的 path 必须在 OSS Bucket 中预先存在。详见 [ossfs 1.91](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/introduction-of-new-functions-and-performance-pressure-measurement-of-ossfs-version-1-91-and-above.md) [及以上版本新增功能说明](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/introduction-of-new-functions-and-performance-pressure-measurement-of-ossfs-version-1-91-and-above.md) |
| sigVersion | 请求 OSS 服务端的请求签名版本。 "v1" （默认）：使用 OSS [签名版本](products/oss/documents/developer-reference/ddd-signatures-to-urls.md) [1](products/oss/documents/developer-reference/ddd-signatures-to-urls.md) 。 "v4" ：使用 OSS [签名版本](products/oss/documents/developer-reference/add-signatures-to-urls.md) [4（推荐）](products/oss/documents/developer-reference/add-signatures-to-urls.md) 。 |


- 

创建PV。

kubectl create -f pv-oss-ram.yaml

## 控制台

- 

将[步骤一](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/mount-statically-provisioned-oss-volumes.md)获取的AccessKey存储为Secret，供PV使用。

- 

在[ACK](https://cs.console.aliyun.com)[集群列表](https://cs.console.aliyun.com)页面，单击目标集群名称，在集群详情页左侧导航栏，选择配置管理>保密字典。

- 

单击使用YAML创建资源，按照页面提示，完成Secret的创建。

apiVersion: v1 kind: Secret metadata: name: oss-secret # 需与应用所在的命令空间保持一致 namespace: default stringData: # 替换为此前获取的AccessKey ID akId: <your AccessKey ID> # 替换为此前获取的AccessKey Secret akSecret: <your AccessKey Secret>

- 

在[ACK](https://cs.console.aliyun.com)[集群列表](https://cs.console.aliyun.com)页面，单击目标集群名称，在集群详情页左侧导航栏，选择存储>存储卷。

- 

在存储卷页面，单击创建，选择存储卷类型为OSS，按照页面配置并提交参数。

关键参数如下。

- 

- 

- 

- 

- 

- 

- 

| 配置项 | 说明 |
| --- | --- |
| 总量 | 所创建存储卷的容量。 |
| 访问模式 | 配置访问模式，支持 ReadOnlyMany 和 ReadWriteMany 。 选择 ReadOnlyMany 时，ossfs 将以只读模式挂载 OSS Bucket。 |
| 访问证书 | 配置访问 OSS 所需的保密字典，即 [步骤一](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/mount-statically-provisioned-oss-volumes.md) 获取的 AccessKey ID 和 AccessKey Secret。 |
| 可选参数 | 为 OSS 存储卷输入定制化参数，格式为 -o *** -o *** ，例如 -o umask=022 -o max_stat_cache_size=100000 -o allow_other 。 展开查看说明 umask ：更改 ossfs 读文件的权限。 例如， umask=022 可将 ossfs 文件的权限变更为 755，解决通过 SDK、OSS 控制台等其他方式上传的文件（默认权限为 640）在挂载点内权限不足的问题。推荐在读写分离或多用户访问时配置。 max_stat_cache_size ：设置元数据缓存的条目上限（例如 100000 ），在内存中缓存文件元信息来提升 ls 、 stat 等操作的性能。 但该缓存无法及时感知通过 OSS 控制台、SDK、ossutil 等方式对文件的修改，可能导致应用读取数据不一致。在对数据一致性有强要求时可将其设为 0 （禁用缓存），或通过 stat_cache_expire 参数调低缓存的失效时间，但会牺牲读取性能。 allow_other ：允许除挂载用户外的其他用户访问挂载点中的文件和目录，适用于需要让非挂载用户也能访问数据的多用户共享环境。 更多可选参数，请参见 [挂载选项说明](products/oss/documents/developer-reference/common-options.md) 、 [ossfs 1.0](products/oss/documents/developer-reference/best-practices.md) [配置最佳实践](products/oss/documents/developer-reference/best-practices.md) 。 |
| Bucket ID | 待使用的 OSS Bucket。 此处仅展示配置 AccessKey 后可获取到的 Bucket。 |
| OSS Path | CSI 组件版本需为 v1.14.8.32-c77e277b-aliyun 及以上。 指定挂载点相对于 Bucket 根目录的路径。默认为 / ，即挂载整个 Bucket。 [ossfs](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/ossfs-release-notes.md) [版本](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/ossfs-release-notes.md) 小于 1.91 时，指定的 path 必须在 OSS Bucket 中预先存在。详见 [ossfs 1.91](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/introduction-of-new-functions-and-performance-pressure-measurement-of-ossfs-version-1-91-and-above.md) [及以上版本新增功能说明](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/introduction-of-new-functions-and-performance-pressure-measurement-of-ossfs-version-1-91-and-above.md) |
| 访问域名 | 待挂载 OSS 的 [访问域名](products/oss/documents/user-guide/regions-and-endpoints.md) （Endpoint）。 挂载节点和 Bucket 处于相同地域，或已打通 VPC 网络时，使用内网地址。 挂载节点和 Bucket 不同地域时，使用外网地址。 不同访问端口的常见填写格式如下： 内网格式： http://oss-{{regionName}}-internal.aliyuncs.com 或 https://oss-{{regionName}}-internal.aliyuncs.com 。 内网访问端口格式 vpc100-oss-{{regionName}}.aliyuncs.com 已废弃，请及时切换。 外网格式： http://oss-{{regionName}}.aliyuncs.com 或 https://oss-{{regionName}}.aliyuncs.com 。 通过私网访问时默认使用 HTTP 协议。如需使用 HTTPS，请使用 [kubectl](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/mount-statically-provisioned-oss-volumes.md) 方式。 |


## 步骤三：创建PVC

创建PVC，为应用声明其所需的持久化存储容量。

## kubectl

- 

创建pvc-oss.yaml。

apiVersion: v1 kind: PersistentVolumeClaim metadata: # PVC 名称 name: pvc-oss namespace: default spec: # 配置访问模式。ReadOnlyMany表明ossfs将以只读模式挂载OSS Bucket accessModes: - ReadOnlyMany resources: requests: # 声明存储容量，不能大于存储卷总量 storage: 10Gi # 添加此行，明确指定不使用StorageClass storageClassName: "" selector: matchLabels: # 通过PV标签精确匹配PV alicloud-pvname: pv-oss

- 

创建PVC。

kubectl create -f pvc-oss.yaml

- 

确认PVC状态。

kubectl get pvc pvc-oss

输出中，PVC已绑定（Bound）PV。

NAME STATUS VOLUME CAPACITY ACCESS MODES STORAGECLASS VOLUMEATTRIBUTESCLASS AGE pvc-oss Bound pv-oss 10Gi ROX <unset> 6s

## 控制台

- 

在[ACK](https://cs.console.aliyun.com)[集群列表](https://cs.console.aliyun.com)页面，单击目标集群名称，在集群详情页左侧导航栏，选择存储>存储声明。

- 

在存储声明页面，单击创建，选择存储声明类型为OSS，按照页面提示完成参数的配置和提交。

关键参数如下。

| 配置项 | 说明 |
| --- | --- |
| 分配模式 | 选择已有存储卷。 若未创建存储卷，可设置 分配模式 为 创建存储卷 ，配置创建存储卷参数。 |
| 总量 | 所创建存储卷的容量，不超过存储卷容量。 |


## 步骤四：创建应用并挂载存储卷

在应用中引用PVC，完成挂载。

## kubectl

- 

创建oss-workload.yaml。

apiVersion: apps/v1 kind: Deployment metadata: name: oss-workload labels: app: nginx spec: replicas: 2 selector: matchLabels: app: nginx template: metadata: labels: app: nginx spec: containers: - name: nginx image: anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/nginx:1.14.1-8.6 ports: - containerPort: 80 volumeMounts: # 容器内的挂载路径 - name: pvc-oss mountPath: "/data" # 配置健康检查 livenessProbe: exec: command: - ls - /data initialDelaySeconds: 30 periodSeconds: 30 volumes: - name: pvc-oss persistentVolumeClaim: # 引用此前创建的PVC claimName: pvc-oss

- 

创建应用。

kubectl create -f oss-workload.yaml

- 

验证挂载结果。

- 

确认Pod处于Running状态。

kubectl get pod -l app=nginx

- 

进入Pod，查看挂载点。

kubectl exec -it <pod-name> -- ls /data

输出中，可查看OSS挂载路径下的数据。

## 控制台

- 

在[ACK](https://cs.console.aliyun.com)[集群列表](https://cs.console.aliyun.com)页面，单击目标集群名称，在集群详情页左侧导航栏，选择工作负载>无状态。

- 

在无状态页面，单击使用镜像创建。

- 

单击使用镜像创建，按照页面提示配置应用参数。

关键参数如下，其他参数保持默认即可。详见[创建无状态工作负载](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-a-stateless-application-by-using-a-deployment.md)[Deployment](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/create-a-stateless-application-by-using-a-deployment.md)。

- 

- 

| 配置页 | 参数 | 说明 |
| --- | --- | --- |
| 应用基本信息 | 副本数量 | Deployment 副本数量。 |
| 容器配置 | 镜像名称 | 用于部署应用的镜像地址，如 anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/nginx:1.14.1-8.6 。 |
| 所需资源 | 所需的 vCPU 和内存资源。 |  |
| 数据卷 | 单击 增加云存储声明（PersistentVolumeClaim） ，然后完成参数配置。 挂载源 ：选择之前创建的 PVC。 容器路径 ：输入 OSS 要挂载到的容器路径，如 /data 。 |  |
| 标签和注解 | Pod 标签 | 如名称为 app，值为 nginx。 |


- 

查看应用部署状态。

在无状态页面，单击应用名称，在容器组页签下，确认Pod已正常运行（状态为Running）。

## 步骤五：验证共享存储和持久化存储

### 验证共享存储

在一个Pod中创建文件，然后在另一个Pod中查看，以验证共享存储特性。

- 

查看Pod信息，在输出中获取Pod名称。

kubectl get pod -l app=nginx

- 

在一个Pod中创建tmpfile文件。 以名为oss-workload-66fbb85b67-d****的Pod为例：

- 

ReadWriteMany：在/data路径下创建tmpfile文件。

kubectl exec oss-workload-66fbb85b67-d**** -- touch /data/tmpfile

- 

ReadOnlyMany：通过[OSS](https://oss.console.aliyun.com/bucket)[控制台](https://oss.console.aliyun.com/bucket)、[cp（上传文件）](products/oss/documents/developer-reference/upload-objects-6.md)等方式上传tmpfile文件至OSS Bucket对应的路径。

- 

在另一个Pod挂载路径下查看文件。

以名为oss-workload-66fbb85b67-l****、挂载路径为data的Pod为例。

kubectl exec oss-workload-66fbb85b67-l**** -- ls /data | grep tmpfile

预期输出如下，Pod挂载路径下均存在此文件，表明两个Pod可共享数据。

tmpfile若无预期输出，请确认[CSI](products/ack/documents/product-overview/csi-plugin.md)[组件](products/ack/documents/product-overview/csi-plugin.md)版本是否为v1.20.7及以上版本。

### 验证持久化存储

删除并重建Pod，在新建的Pod中查看文件是否存在，验证数据的持久化存储。

- 

删除一个应用Pod以触发重建。

kubectl delete pod oss-workload-66fbb85b67-d****

- 

查看Pod，等待新Pod启动并进入Running状态。

kubectl get pod -l app=nginx

- 

查看/data路径下的文件。

以名为oss-workload-66fbb85b67-z****、挂载路径为data的Pod为例。

kubectl exec oss-workload-66fbb85b67-z**** -- ls /data | grep tmpfile

预期输出如下，tmpfile文件仍存在，表明数据可持久化存储。

tmpfile

## 功能已知影响

- 

数据完整性风险

- 

并发写一致性风险：为提升写操作稳定性，建议[升级](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/install-and-upgrade-the-csi-plug-in.md)[CSI](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/install-and-upgrade-the-csi-plug-in.md)[组件](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/install-and-upgrade-the-csi-plug-in.md)至v1.28及以上版本。但对于单文件并发写场景，OSS的“覆盖上传”特性仍可能导致数据覆盖，需在应用层保障数据一致性。

- 

数据同步与误删风险：挂载状态下，在应用Pod或宿主机上对挂载路径下的文件删除或变更操作会直接同步到OSS Bucket源文件。为避免数据误删除，建议为OSS Bucket开启[版本控制](products/oss/documents/user-guide/overview-78.md)。

- 

应用稳定性风险

- 

OOM风险：初次对大量文件（如超10万，具体取决于节点内存）进行readdir操作时（如Shell脚本中的ls命令），ossfs会因一次性加载全部元信息而消耗大量内存，可能导致进程OOM Killed，并引发挂载点不可用。

建议挂载OSS Bucket子目录或优化目录层级来规避此风险。

- 

挂载时间延长：在应用中配置securityContext.fsgroup会导致kubelet在挂载存储卷时递归修改文件权限（chmod/chown）。若文件数量庞大，将显著延长挂载时间，可能导致 Pod 启动严重延迟。

配置此参数时，如需减少挂载时间，请参见[OSS](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-oss-volumes-1.md)[存储卷挂载时间延长](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-oss-volumes-1.md)。

- 

密钥失效风险（AccessKey鉴权方式）：若PV引用的AccessKey失效或权限变更，关联应用会立即失去访问权限。

恢复访问需更新Secret中的凭证，并重启应用Pod以强制重新挂载（将导致业务中断），请在维护窗口期执行。详见[解决方案](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-oss-volumes-1.md)。

- 

成本风险

- 

碎片成本：当传输文件大于10 MB时，ossfs会将文件分片上传。若上传因业务自身重启等特殊原因意外中断，请[手动删除碎片](products/oss/documents/user-guide/delete-parts.md)或[通过生命周期规则删除碎片](products/oss/documents/user-guide/lifecycle-rules-based-on-the-last-modified-time.md)，避免碎片占用存储空间并产生费用。

## 资源释放指引

为避免产生预期外费用并确保数据安全，请遵循以下流程释放无需使用的资源。

- 

删除工作负载

- 

操作：删除所有使用相关PVC的应用，如Deployment、StatefulSet等，停止Pod并卸载存储卷。

- 

命令示例：kubectl delete deployment <your-deployment-name>

- 

删除PVC

- 

操作：删除应用关联的PVC。OSS静态卷的PV回收策略（persistentVolumeReclaimPolicy）仅支持Retain。因此，删除PVC后，其绑定的PV会进入Released状态，后端的OSS Bucket及其中的所有数据都会被完整保留。

- 

命令示例：kubectl delete pvc <your-pvc-name>

- 

删除PV

- 

操作：删除处于Released状态的PV。此操作仅移除Kubernetes中的资源定义，不会删除后端OSS Bucket中的数据。

- 

命令示例：kubectl delete pv <your-pv-name>

- 

删除Secret（可选）

- 

操作：删除为挂载OSS而创建的Secret。此操作仅移除Kubernetes中的Secret资源对象，不删除后端OSS Bucket中的数据。

- 

命令示例：kubectl delete secret <your-secret-name>

## 相关文档

- 

可通过CNFS托管OSS存储卷，以提升其性能和QoS控制，请参见[管理](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/manage-the-lifecycle-of-oss-buckets.md)[OSS](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/manage-the-lifecycle-of-oss-buckets.md)[生命周期](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/manage-the-lifecycle-of-oss-buckets.md)。

- 

为保护OSS中的静态敏感数据，建议开启服务端加密，请参见[加密](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/encrypt-an-oss-volume.md)[ossfs 1.0](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/encrypt-an-oss-volume.md)[存储卷](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/encrypt-an-oss-volume.md)。

- 

关于ossfs和OSS的常见问题，请参见[ossfs 1.0](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/ossfs1-0.md)、[ossfs 1.0](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-oss-volumes-1.md)[存储卷](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-oss-volumes-1.md)[FAQ](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/faq-about-oss-volumes-1.md)。

- 

启用[容器存储监控](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-csi-plugin-to-monitor-storage-resources-at-the-node-side.md)配置告警，及时发现存储卷的异常或性能瓶颈。

- 

与[ossfs 2.0](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/ossfs-2-0.md)相比，ossfs 1.0在随机写和并发写场景下能提供更可靠的数据一致性保障。但对于顺序读写场景，ossfs 2.0性能更优。

[上一篇：ossfs 1.0](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/ossfs1-0.md)[下一篇：使用ossfs 1.0动态存储卷](products/ack/documents/ack-managed-and-ack-dedicated/user-guide/use-dynamically-provisioned-oss-volumes.md)

该文章对您有帮助吗？

反馈

### 为什么选择阿里云

[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)

### 大模型

[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)

### 产品和定价

[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)

### 技术内容

[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)

### 权益

[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)

### 服务

[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)

### 关注阿里云

关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务

联系我们：4008013260

[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)

### 友情链接

[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)

© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )

[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
