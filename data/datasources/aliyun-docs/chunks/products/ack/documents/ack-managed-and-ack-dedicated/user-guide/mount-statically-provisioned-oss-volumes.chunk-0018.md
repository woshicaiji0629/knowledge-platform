| 参数 | 描述 |
| --- | --- |
| storage | 定义 OSS 存储卷容量。此值仅用于匹配 PVC。 |
| accessModes | 配置访问模式，支持 ReadOnlyMany 和 ReadWriteMany 。 选择 ReadOnlyMany 时，ossfs 将以只读模式挂载 OSS Bucket。 |
| persistentVolumeReclaimPolicy | PV 回收策略。当前 OSS 存储卷仅支持 Retain ，即删除 PVC 时，PV 和 OSS Bucket 中的数据不会随之删除。 |
| driver | 定义驱动类型。使用阿里云 OSS CSI 插件固定为 ossplugin.csi.alibabacloud.com 。 |
| nodePublishSecretRef | 指定 Secret，以在挂载 PV 时提供 AccessKey 信息。 |
| volumeHandle | 需与 PV 名称（ metadata.name ）保持一致。 |
| bucket | 待挂载的 OSS Bucket。 |
| url | 待挂载 OSS 的 [访问域名](../../../../oss/documents/user-guide/regions-and-endpoints.md) （Endpoint）。 挂载节点和 Bucket 处于相同地域，或已打通 VPC 网络时，使用内网地址。 挂载节点和 Bucket 不同地域时，使用外网地址。 不同访问端口的常见填写格式如下： 内网格式： http://oss-{{regionName}}-internal.aliyuncs.com 或 https://oss-{{regionName}}-internal.aliyuncs.com 。 内网访问端口格式 vpc100-oss-{{regionName}}.aliyuncs.com 已废弃，请及时切换。 外网格式： http://oss-{{regionName}}.aliyuncs.com 或 https://oss-{{regionName}}.aliyuncs.com 。 |
| otherOpts | 为 OSS 存储卷输入定制化参数，格式为 -o *** -o *** ，例如 -o umask=022 -o max_stat_cache_size=100000 -o allow_other 。 展开查看说明 umask ：更改 ossfs 读文件的权限。 例如， umask=022 可将 ossfs 文件的权限变更为 755，解决通过 SDK、OSS 控制台等其他方式上传的文件（默认权限为 640）在挂载点内权限不足的问题。推荐在读写分离或多用户访问时配置。 max_stat_cache_size
