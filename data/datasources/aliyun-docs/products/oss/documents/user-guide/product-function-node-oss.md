# 产品功能特性全景概览-对象存储-阿里云

Source: https://help.aliyun.com/zh/oss/user-guide/product-function-node-oss

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/oss/documents/user-guide.md)

- [开发参考](products/oss/documents/developer-reference.md)

- [产品计费](products/oss/documents/billing.md)

- [常见问题](products/oss/documents/oss-faq.md)

- [动态与公告](products/oss/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 功能特性

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/oss)

[我的收藏](https://help.aliyun.com/my_favorites.html)

## 数据管理

| 功能集 | 功能 | 功能描述 | 参考文档 |
| --- | --- | --- | --- |
| 存储类型 | 标准存储 | 提供高可靠、高可用、高性能的对象存储服务，面向温热数据，适合支持频繁的数据访问。 | [标准存储](products/oss/documents/user-guide/overview-53.md) |
| 低频访问存储 | 提供高持久性、较低存储成本的对象存储服务。有最小计量单位（64 KB）和最低存储时间（30 天）的要求。支持数据实时访问，访问数据时会产生数据取回费用，适用于较低访问频率（平均每月访问频率 1 到 2 次）的业务场景。 | [低频访问存储](products/oss/documents/user-guide/overview-53.md) |  |
| 归档存储 | 提供高持久性、更低存储成本的对象存储服务。有最小计量单位（64 KB）和最低存储时间（60 天）要求。数据需解冻（约 1 分钟）后访问，解冻会产生数据取回费用。适用于数据长期保存的业务场景，例如档案数据、医疗影像、科学资料、影视素材等。 | [归档存储](products/oss/documents/user-guide/overview-53.md) |  |
| 冷归档存储 | 提供高持久性、比归档存储的存储成本更低的对象存储服务。有最小计量单位（64 KB）和最低存储时间（180 天）的要求。数据需解冻后访问，解冻时间根据数据大小和选择的解冻模式决定，解冻会产生数据取回费用以及取回请求费用。适用于需要超长时间存放的冷数据。 | [冷归档存储](products/oss/documents/user-guide/overview-53.md) |  |
| 深度冷归档存储 | 提供高持久性、比冷归档存储成本更低的对象存储服务。有最小计量单位（64 KB）和最低存储时间（180 天）的要求。数据需解冻后访问，解冻时间根据数据大小和选择的解冻模式决定，解冻会产生数据取回费用以及取回请求费用。存储成本最低，但需要较长时间的解冻。 | [深度冷归档存储](products/oss/documents/user-guide/overview-53.md) |  |
| 存储空间管理（Bucket） | 镜像回源 | 配置了镜像回源规则后，当请求者访问 Bucket 中一个不存在的 Object 时，OSS 会向回源规则指定的源站获取这个文件。在获取到目标文件后，OSS 会将文件返回给请求者并存入 Bucket。 | [镜像回源](products/oss/documents/back-to-origin-configuration-overview.md) |
| 静态网站托管 | OSS 支持静态网站托管功能，您可以将您的存储空间配置成静态网站托管模式，并通过存储空间域名访问该静态网页。 | - |  |
| 传输加速 | OSS 支持传输加速服务，可优化互联网传输链路和协议栈，大幅减少数据远距离传输超时的比例，极大地提升用户上传和下载体验。 | [传输加速](products/oss/documents/user-guide/transfer-acceleration.md) |  |
| 创建存储空间 | 在上传文件（Object）到 OSS 之前，您需要创建一个用于存储文件的存储空间（Bucket）。存储空间具有各种配置属性，包括地域、访问权限、存储类型等。您可以根据实际需求，创建不同类型的存储空间来存储不同的数据。 | [创建存储空间](products/oss/documents/user-guide/create-a-bucket-4.md) |  |
| 存储空间清单 | OSS 支持清单功能，您可以使用存储空间清单功能导出指定对象的元数据信息，如文件大小、加密状态等。 | [存储空间清单](products/oss/documents/user-guide/bucket-inventory.md) |  |
| 归档直读 | 归档直读是指直接访问归档存储类型的文件，而无需先对其解冻。归档直读适用于实时读取极低频访问数据的场景。 | [归档直读](products/oss/documents/user-guide/archive-direct-reading.md) |  |
| 资源组 | 资源组是一种基于资源的权限管理方式。您可以根据不同的业务需求对存储空间（Bucket）进行分组，为不同的资源组设置不同的访问权限，实现资源组范围内的权限管理。 | [资源组](products/oss/documents/user-guide/configure-a-resource-group.md) |  |
| 请求者付费 | 请求者付费模式是指由请求者支付访问 Bucket 内数据时产生的费用，而 Bucket 拥有者仅支付存储费用。当您希望共享数据，但又不希望支付因共享数据产生的额外费用时，您可以开启此功能。 | [请求者付费](products/oss/documents/user-guide/enable-pay-by-requester-1.md) |  |
| 删除存储空间 | 当您不再需要保留某个存储空间时，可将其删除，以免产生额外费用。 | [删除存储空间](products/oss/documents/user-guide/delete-buckets.md) |  |
| 存储空间标签 | 您可以通过 Bucket 的标签功能， 对 Bucket 进行分类管理。例如通过不同的标签来标记不同用途的 Bucket，对拥有指定标签的 Bucket 设置访问权限等。 | [存储空间标签](products/oss/documents/user-guide/manage-bucket-tags.md) |  |
| 对象管理（Object） | 对象标签 | OSS 支持使用标签对 Bucket 中的 Object 进行分类，您可以针对同标签的 Object 设置生命周期规则、访问权限等。 | [对象标签](products/oss/documents/user-guide/object-tagging-8.md) |
| 上传文件 | 创建存储空间后，您可以通过多种上传方式将任意类型文件上传到该存储空间。 | [上传文件](products/oss/documents/user-guide/upload-objects-to-oss.md) |  |
| 下载文件 | 文件上传至存储空间后，您可以通过多种下载方式将文件下载至浏览器默认路径或本地指定路径。 | [下载文件](products/oss/documents/user-guide/download-files.md) |  |
| 列举文件 | Bucket 内的 Object 默认按照字母序排列。您可以结合实际场景列举当前 Bucket 的所有 Object、指定前缀的 Object、指定个数的 Object 等。 | [列举文件](products/oss/documents/user-guide/list-objects-18.md) |  |
| 删除文件 | OSS 支持一次删除单个或者多个文件、碎片等。您可以定期删除过期文件，节省您的存储空间。 | [删除文件](products/oss/documents/user-guide/delete-objects-18.md) |  |
| 拷贝文件 | 拷贝文件是指在不改变文件内容的情况下，将同一地域下的源 Bucket 内的文件复制到目标 Bucket。 | [拷贝文件](products/oss/documents/user-guide/copy-objects-16.md) |  |
| 解冻文件 | 归档存储、冷归档存储或者深度冷归档存储类型的 Object 需要解冻（Restore）之后才能读取。 | [解冻文件](products/oss/documents/user-guide/restore-objects-for-access.md) |  |
| 重命名文件 | OSS 不支持直接对 Object 进行重命名。如果您需要在同一个 Bucket 内对 Object 进行重命名，您可以通过 CopyObject 接口将源 Object 拷贝至目标 Object，然后通过 DeleteObject 接口删除源 Object。 | [重命名文件](products/oss/documents/user-guide/rename-objects.md) |  |
| 分享文件 | 文件上传至存储空间后，您可以将文件 URL 分享给第三方，供其下载或预览。 | [分享文件](products/oss/documents/user-guide/share-objects-by-url.md) |  |
| 搜索文件 | OSS 支持文件和文件夹搜索功能，您可以在存储空间中快速查找目标文件。 | [搜索文件](products/oss/documents/user-guide/search-for-objects.md) |  |
| 软链接 | 软链接功能用于快速访问 Bucket 内的常用 Object。设置软链接后，您可以使用类似于 Windows 的快捷方式，通过软链接文件快速打开 Object。 | [软链接](products/oss/documents/user-guide/configure-symbolic-links.md) |  |
| 管理文件元信息 | OSS 存储的文件（Object）信息包含 Key、Data 和 Object Meta。Object Meta 是对文件的属性描述，包括 HTTP 标准属性（HTTP Header）和用户自定义元数据（User Meta）两种。您可以通过设置 HTTP 标准属性来自定义 HTTP 请求的策略，例如文件（Object）缓存策略、强制下载策略等。您还可以通过设置用户自定义元数据来标识 Object 的用途或属性等。 | [管理文件元信息](products/oss/documents/user-guide/manage-object-metadata-10.md) |  |
| 管理目录 | 与传统文件系统中的层级结构不同，OSS 内部使用扁平结构存储数据。即所有数据均以 Object 的形式保存在 Bucket 中。为方便您对 Object 进行分组并简化权限管理，您可以创建目录，然后将目标 Object 存放至指定目录。当您不需要保留该目录时，还可以通过多种方式删除目录。 | [管理目录](products/oss/documents/user-guide/manage-directories.md) |  |
| 数据索引 | 如果您希望从 Bucket 存储的海量 Object 中快速查找与指定的 Object 名称、ETag、存储类型、大小、最后修改时间等条件匹配的 Object，您可以使用数据索引功能。通过数据索引功能，您可以在查找目标 Object 时指定过滤条件，对查询结果按需选择排序和聚合的方式，提升查找目标 Object 的效率。 | [数据索引](products/oss/documents/user-guide/scalar-retrieval.md) |  |
| 通过云存储网关挂载 OSS | 通过云存储网关挂载 OSS，您可以将 OSS 映射为一个共享的文件存储系统，实现多个用户在不同地点和设备上共享访问 OSS 数据。挂载完成后，您可以像使用本地文件夹和磁盘一样操作 OSS 资源。 | [通过云存储网关挂载](products/oss/documents/user-guide/use-csg-to-attach-oss-buckets-to-ecs-instances.md) [OSS](products/oss/documents/user-guide/use-csg-to-attach-oss-buckets-to-ecs-instances.md) |  |


## 数据安全和保护能力

| 功能集 | 功能 | 功能描述 | 参考文档 |
| --- | --- | --- | --- |
| 访问控制 | Bucket ACL | 当您希望粗粒度地控制某个 Bucket 的读写权限，即 Bucket 内的所有 Object 均为统一的读写权限时，您可以选择使用 Bucket ACL 的方式。Bucket ACL 包含公共读、公共读写和私有。您可以在创建 Bucket 时设置 Bucket ACL，也可以在创建 Bucket 后根据自身的业务需求修改 Bucket ACL。 | [Bucket ACL](products/oss/documents/user-guide/bucket-acl-2.md) |
| Object ACL | 当您希望针对 Bucket 中的某个具体的 Object 设置特定的读写权限时，可以使用 Object ACL。通过设置 Object ACL，可以精确控制某个 Object 的访问权限，且不影响 Bucket 中其他 Object 的访问权限。Object ACL 包含公共读、公共读写、私有。您可以在上传 Object 时设置 ACL，也可以在 Object 上传后根据自己的业务需求随时修改 ACL。 | [Object ACL](products/oss/documents/user-guide/object-acl.md) |  |
| Bucket Policy | OSS 支持面向资源的授权方式，允许在 Bucket 级别而不是用户级别设置权限策略。使用 Bucket Policy 可以授权当前云账号或者其他阿里云账号下单个或多个 RAM 用户、RAM 角色等访问 Bucket 内的指定资源。Bucket Policy 除提供策略语法的授权方式以外，还提供了图形化界面的授权方式，助力您结合业务场景，快速完成授权。 | [Bucket Policy](products/oss/documents/user-guide/use-bucket-policy-to-grant-permission-to-access-oss.md) |  |
| 防盗链 | 通过在 OSS 中配置基于请求标头 Referer 的访问规则，可以阻止某些 Referer 访问您的 OSS 文件，从而防止其他网站盗用您的文件，并避免由此引起的不必要的流量费用增加。 | [防盗链](products/oss/documents/user-guide/hotlink-protection.md) |  |
| 跨域资源共享 CORS | 默认情况下，由于同源策略（Same-Origin Policy）的限制，网页浏览器在执行 JavaScript 时会限制跨域请求，只允许请求同一域或源的资源。跨域资源共享 CORS（Cross-Origin Resource Sharing）简称跨域访问，允许网页浏览器向不同域或源的服务器发起跨域请求。通过跨域设置可以实现在您的网站上使用 JavaScript 请求非同源的 OSS 对象链接而不会出现跨域问题。 | [跨域资源共享](products/oss/documents/user-guide/configure-cross-origin-resource-sharing.md) [CORS](products/oss/documents/user-guide/configure-cross-origin-resource-sharing.md) |  |
| 数据保护 | 同城冗余 | OSS 采用多可用区（AZ）内的数据冗余存储机制，将用户的数据冗余存储在同一地域（Region）的多个可用区。当某个可用区不可用时，仍然能够保障数据的正常访问。OSS 同城冗余存储提供 99.9999999999%（12 个 9）的数据设计持久性。 | [同城冗余](products/oss/documents/user-guide/zrs.md) |
| 跨区域复制 | 跨区域复制（Cross-Region Replication）是指将相同或者不同账号某个地域下源存储空间（Bucket）中 Object 的创建、更新和删除等操作自动、异步（近实时）地复制到另一个地域下的目标 Bucket，以实现合规、降低延时、确保安全性和可用性等目的。 | - |  |
| 同区域复制 | 同区域复制（Same-Region Replication）是指将源存储空间（Bucket）中的文件（Object）的创建、更新和删除等操作自动、异步（近实时）地复制到相同地域下的目标 Bucket。 | [同区域复制](products/oss/documents/user-guide/srr.md) |  |
| 版本控制 | 版本控制是针对 Bucket 级别的数据保护功能。开启版本控制后，针对数据的覆盖和删除操作将会以历史版本的形式保存下来。您在错误覆盖或删除 Object 后，能够将存储在 Bucket 中的 Object 恢复至任意时刻的历史版本。 | - |  |
| 数据复制时间控制（RTC） | OSS 数据复制时间控制 RTC（Replication Time Control）可满足您在跨区域复制数据的合规性要求或者业务需求。开启 RTC 后，OSS 会在几秒内复制您上传到 OSS 的大多数对象（Object），并在 10 分钟内复制 99.99%的对象。此外，RTC 功能还提供了数据复制的准实时监控，方便您查看复制任务的各项指标。 | [数据复制时间控制（RTC）](products/oss/documents/user-guide/rtc.md) |  |
| 定时备份 | 为了避免因误删除、误修改、误覆盖操作等情况引起的数据丢失或受损，您可以通过云备份对存储空间（Bucket）内的文件（Object）进行定期备份。当您的 Object 意外丢失时，可通过云备份进行恢复。云备份对支持配置灵活备份策略，将数据备份至云端，您可以随时查看和恢复数据。 | [定时备份](products/oss/documents/user-guide/configure-scheduled-backup.md) |  |
| 安全合规 | 服务器端加密 | 当您在设置了服务器端加密的 Bucket 中上传 Object 时，OSS 对收到的文件进行加密，再将得到的加密文件持久化保存。当您通过 GetObject 请求下载文件时，OSS 自动将加密文件解密后返回给用户，并在响应头中返回 x-oss-server-side-encryption，用于声明该文件进行了服务器端加密。 | [服务器端加密](products/oss/documents/user-guide/server-side-encryption-8.md) |
| 客户端加密 | OSS 客户端加密是在数据上传至 OSS 之前，由用户在本地对数据进行加密处理，确保只有密钥持有者才能解密数据，增强数据在传输和存储过程中的安全性。 | [客户端加密](products/oss/documents/user-guide/client-side-encryption.md) |  |
| 合规保留策略 | OSS 保留策略具有 WORM（Write Once Read Many）特性，满足用户以不可删除、不可篡改方式保存和使用数据。如果您希望指定时间内任何用户（包括资源拥有者）均不能修改和删除 OSS 某个 Bucket 中的 Object，您可以选择为 Bucket 配置保留策略。在保留策略指定的 Object 保留时间到期之前，仅支持在 Bucket 中上传和读取 Object。Object 保留时间到期后允许修改或删除。 | [合规保留策略](products/oss/documents/user-guide/oss-retention-policies.md) |  |
| 敏感数据保护 | 敏感数据保护是一款识别、分类、分级和保护 Bucket 中敏感数据的原生服务，可满足数据安全、个人信息保护等相关法规的合规要求。 | [敏感数据保护](products/oss/documents/user-guide/sddp.md) |  |
| OSS 高防 | OSS 高防是 OSS 结合 DDoS 高防推出的 DDoS 攻击代理防护服务。当受保护的 Bucket 遭受大流量攻击时，OSS 高防会将攻击流量牵引至高防集群进行清洗，并将正常访问流量回源到目标 Bucket，确保业务的正常进行。 | [OSS](products/oss/documents/user-guide/oss-ddos-protection.md) [高防](products/oss/documents/user-guide/oss-ddos-protection.md) |  |
| 日志转存 | 访问 OSS 的过程中会产生大量的访问日志。您可以通过日志转存功能将这些日志按照固定命名规则，以小时为单位生成日志文件写入您指定的 Bucket。对于已存储的日志，您可以通过阿里云日志服务或搭建 Spark 集群等方式进行分析。 | [日志转存](products/oss/documents/user-guide/logging.md) |  |
| 实时日志查询 | 访问 OSS 的过程中会产生大量的访问日志。实时日志查询功能将 OSS 与日志服务 SLS 相结合，允许您在 OSS 控制台直接查询 OSS 的访问日志，帮助您完成 OSS 访问的操作审计、访问统计、异常事件回溯和问题定位等工作，提升您的工作效率并更好地帮助您基于数据进行决策。 | [实时日志查询](products/oss/documents/user-guide/real-time-log-query.md) |  |
| OSS 内容安全功能 | 如果您希望检测 OSS 存储的图片是否包含违规内容，例如图片内容是否涉黄、涉政、涉恐、涉暴等，您可以选择 OSS 提供的内容安全检测服务。OSS 内容安全服务具有通用性强、易用性高、价格实惠的特点。通过 OSS 内容安全检测服务可以帮助您提高图片内容审核效率，及时发现并处理违规图片，提升内容安全和用户体验。 | [内容安全检测](products/oss/documents/user-guide/check-content-security.md) |  |


## 数据处理

| 功能集 | 功能 | 功能描述 | 参考文档 |
| --- | --- | --- | --- |
| 数据湖 | OSS Select | 您可以使用 SelectObject 对目标文件执行 SQL 语句，返回执行结果。 | [OSS Select](products/oss/documents/user-guide/query-objects.md) |
| OSS 加速器 | 随着 AI、数据仓库、大数据分析等业务发展，越来越多运行在 OSS 上的业务对于数据的访问延迟和吞吐量有了更高的要求。OSS 推出加速器功能，可以将 OSS 中的热点 Object 缓存在 NVMe SSD 高性能存储介质上，提供毫秒级低延迟和高吞吐量的数据访问服务。 | - |  |
| OSS-HDFS 服务 | OSS-HDFS 服务（JindoFS 服务）是一个云原生数据湖存储功能。基于统一的元数据管理能力，完全兼容 HDFS 文件系统接口，满足大数据和 AI 等领域的数据湖计算场景。 | [OSS-HDFS](products/oss/documents/user-guide/oss-hdfs.md) [服务](products/oss/documents/user-guide/oss-hdfs.md) |  |
| 数据处理 | 图片处理 | 针对 OSS 内存储的图片文件，您可以在 GetObject 请求中携带图片处理参数对图片文件进行处理。例如添加图片水印、转换格式等。 | - |
| ZIP 包解压 | 当您需要批量上传文件、按特定目录结构上传文件、上传完整的文件或对文件快速进行资源分发时，可以配置解压规则，上传 ZIP 文件到 OSS 指定路径，触发函数计算自动解压，并将解压后内容保存回 OSS。 | [ZIP](products/oss/documents/user-guide/zip-package-decompression.md) [包解压](products/oss/documents/user-guide/zip-package-decompression.md) |  |
| 智能媒体 | OSS 与智能媒体管理（IMM）深度结合，支持媒体处理、文档处理等丰富的数据分析处理操作。 | [智能媒体](products/oss/documents/user-guide/intelligent-media-management-imm.md) |  |
| 事件通知 | 当您需要对 OSS 中的文件变动进行实时处理、同步、监听、业务触发、日志记录等操作时，您可以通过设置 OSS 的事件通知规则，自定义关注的文件，并及时收到相关通知。 | [事件通知](products/oss/documents/user-guide/event-notifications.md) |  |
| OSS 对象 FC（Object FC） | 基于 OSS 对象 FC（Object FC），用户可以在发送 OSS GetObject 等请求时自动触发函数计算服务，并将处理后的数据结果进行返回。OSS 对象 FC（Object FC）帮助用户在保持对象存储语义的情况下，无缝集成自定义的数据处理能力。 | [对象](products/oss/documents/user-guide/create-object-fc-access-point.md) [FC](products/oss/documents/user-guide/create-object-fc-access-point.md) [接入点](products/oss/documents/user-guide/create-object-fc-access-point.md) |  |


## 常用工具

| 功能集 | 功能 | 功能描述 | 参考文档 |
| --- | --- | --- | --- |
| 客户端管理 | 命令行工具 ossutil | ossutil 支持通过 Windows、Linux 和 macOS 系统以命令行方式管理 OSS 数据。 | - |
| 图形化工具 ossbrowser | ossbrowser 2.0 是一款用于管理 OSS 的免费图形化桌面客户端。该客户端支持 Windows、macOS 和 Linux 操作系统，提供直观的图形用户界面，使您能够高效地执行各种操作，包括文件的上传、下载和删除。由于其本地部署特性，ossbrowser 2.0 可在您的设备上直接运行，确保操作的流畅性。 | [图形化工具](products/oss/documents/developer-reference/ossbrowser-2-0-overview.md) [ossbrowser 2.0](products/oss/documents/developer-reference/ossbrowser-2-0-overview.md) |  |
| 访问接入 | ossfs | 对于原来需要直接读写本地文件的应用程序，为了让应用程序能在不作修改的情况下直接访问对象存储 OSS 的数据，您可以使用 ossfs 将 OSS 的 Bucket 挂载到 Linux 系统中，并将其映射到本地目录，从而能够像处理本地文件那样直接操作 OSS 中的数据，实现文件共享。 | - |
| ossftp | ossftp 是一个特殊的 FTP server，可以将对文件、文件夹的操作映射为对 OSS 的操作，使您可以基于 FTP 协议来管理存储在 OSS 上的文件。 | - |  |
| OSS Connector | 提供计算生态直接读写 OSS 的能力 | [OSS Connector](products/oss/documents/developer-reference/oss-connector-overview.md) |  |


## 部署形态

| 功能集 | 功能 | 功能描述 | 参考文档 |
| --- | --- | --- | --- |
| 部署形态 | OSS ON 云盒 | OSS ON 云盒为云盒（CloudBox）产品提供了非结构化数据本地存储、本地访问、以及本地处理的能力。您可以在 OSS ON 云盒中创建 Bucket，并使用与公共云一致的 API、SDK 访问云盒中的 OSS。 | - |


[上一篇：什么是对象存储OSS](products/oss/documents/user-guide/what-is-oss.md)[下一篇：选型指导](products/oss/documents/user-guide/selection-guidance-selection-guidance.md)

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
