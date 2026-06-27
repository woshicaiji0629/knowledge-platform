| 配置项 | 说明 |
| --- | --- |
| 总量 | 所创建存储卷的容量。 |
| 访问模式 | 配置访问模式，支持 ReadOnlyMany 和 ReadWriteMany 。 选择 ReadOnlyMany 时，ossfs 将以只读模式挂载 OSS Bucket。 |
| 访问证书 | 配置访问 OSS 所需的保密字典，即 [步骤一](mount-statically-provisioned-oss-volumes.md) 获取的 AccessKey ID 和 AccessKey Secret。 |
| 可选参数 | 为 OSS 存储卷输入定制化参数，格式为 -o *** -o *** ，例如 -o umask=022 -o max_stat_cache_size=100000 -o allow_other 。 展开查看说明 umask ：更改 ossfs 读文件的权限。 例如， umask=022 可将 ossfs 文件的权限变更为 755，解决通过 SDK、OSS 控制台等其他方式上传的文件（默认权限为 640）在挂载点内权限不足的问题。推荐在读写分离或多用户访问时配置。 max_stat_cache_size ：设置元数据缓存的条目上限（例如 100000 ），在内存中缓存文件元信息来提升 ls 、 stat 等操作的性能。 但该缓存无法及时感知通过 OSS 控制台、SDK、ossutil 等方式对文件的修改，可能导致应用读取数据不一致。在对数据一致性有强要求时可将其设为 0 （禁用缓存），或通过 stat_cache_expire 参数调低缓存的失效时间，但会牺牲读取性能。 allow_other ：允许除挂载用户外的其他用户访问挂载点中的文件和目录，适用于需要让非挂载用户也能访问数据的多用户共享环境。 更多可选参数，请参见 [挂载选项说明](../../../../oss/documents/developer-reference/common-options.md) 、 [ossfs 1.0](../../../../oss/documents/developer-reference/best-practices.md) [配置最佳实践](../../../../oss/documents/developer-reference/best-practices.md) 。 |
| Bucket ID | 待使用的 OSS Bucket。 此处仅展示配置 AccessKey 后可获取到的 Bucket。 |
| OSS Path | CSI 组件版本需为 v1.14.8.32-c77e277b-aliyun 及以上。 指定挂载点相对于 Bucket 根目录的路径。默认为 / ，即挂载整个 Bucket。 [ossfs](ossfs-
