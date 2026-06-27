| 参数 | 描述 |
| --- | --- |
| storage | 定义 OSS 存储卷容量。此值仅用于匹配 PVC。 |
| accessModes | 配置访问模式，支持 ReadOnlyMany 和 ReadWriteMany 。 选择 ReadOnlyMany 时，ossfs 将以只读模式挂载 OSS Bucket。 |
| persistentVolumeReclaimPolicy | PV 回收策略。当前 OSS 存储卷仅支持 Retain ，即删除 PVC 时，PV 和 OSS Bucket 中的数据不会随之删除。 |
| driver | 定义驱动类型。使用阿里云 OSS CSI 插件固定为 ossplugin.csi.alibabacloud.com 。 |
| volumeHandle | 需与 PV 名称（ metadata.name ）保持一致。 |
| bucket | 待挂载的 OSS Bucket。 |
| path | CSI 组件版本需为 v1.14.8.32-c77e277b-aliyun 及以上。 指定挂载点相对于 Bucket 根目录的路径。默认为 / ，即挂载整个 Bucket。 [ossfs](ossfs-release-notes.md) [版本](ossfs-release-notes.md) 小于 1.91 时，指定的 path 必须在 OSS Bucket 中预先存在。详见 [ossfs 1.91](introduction-of-new-functions-and-performance-pressure-measurement-of-ossfs-version-1-91-and-above.md) [及以上版本新增功能说明](introduction-of-new-functions-and-performance-pressure-measurement-of-ossfs-version-1-91-and-above.md) |
| url | 待挂载 OSS 的 [访问域名](../../../../oss/documents/user-guide/regions-and-endpoints.md) （Endpoint）。 挂载节点和 Bucket 处于相同地域，或已打通 VPC 网络时，使用内网地址。 挂载节点和 Bucket 不同地域时，使用外网地址。 不同访问端口的常见填写格式如下： 内网格式： http://oss-{{regionName}}-internal.aliyuncs.com 或 https://oss-{{regionName}}-internal.aliyuncs.com 。 内网访问端口格式 vpc100-oss-{{regionName}}.aliyuncs.co
