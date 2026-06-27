t 设置生命周期规则、访问权限等。 | [对象标签](object-tagging-8.md) |
| 上传文件 | 创建存储空间后，您可以通过多种上传方式将任意类型文件上传到该存储空间。 | [上传文件](upload-objects-to-oss.md) |  |
| 下载文件 | 文件上传至存储空间后，您可以通过多种下载方式将文件下载至浏览器默认路径或本地指定路径。 | [下载文件](download-files.md) |  |
| 列举文件 | Bucket 内的 Object 默认按照字母序排列。您可以结合实际场景列举当前 Bucket 的所有 Object、指定前缀的 Object、指定个数的 Object 等。 | [列举文件](list-objects-18.md) |  |
| 删除文件 | OSS 支持一次删除单个或者多个文件、碎片等。您可以定期删除过期文件，节省您的存储空间。 | [删除文件](delete-objects-18.md) |  |
| 拷贝文件 | 拷贝文件是指在不改变文件内容的情况下，将同一地域下的源 Bucket 内的文件复制到目标 Bucket。 | [拷贝文件](copy-objects-16.md) |  |
| 解冻文件 | 归档存储、冷归档存储或者深度冷归档存储类型的 Object 需要解冻（Restore）之后才能读取。 | [解冻文件](restore-objects-for-access.md) |  |
| 重命名文件 | OSS 不支持直接对 Object 进行重命名。如果您需要在同一个 Bucket 内对 Object 进行重命名，您可以通过 CopyObject 接口将源 Object 拷贝至目标 Object，然后通过 DeleteObject 接口删除源 Object。 | [重命名文件](rename-objects.md) |  |
| 分享文件 | 文件上传至存储空间后，您可以将文件 URL 分享给第三方，供其下载或预览。 | [分享文件](share-objects-by-url.md) |  |
| 搜索文件 | OSS 支持文件和文件夹搜索功能，您可以在存储空间中快速查找目标文件。 | [搜索文件](search-for-objects.md) |  |
| 软链接 | 软链接功能用于快速访问 Bucket 内的常用 Object。设置软链接后，您可以使用类似于 Windows 的快捷方式，通过软链接文件快速打开 Object。 | [软链接](configure-symbolic-links.md) |  |
| 管理文件元信息 | OSS 存储的文件（Object）信息包含 Key、Data 和 Object Meta。Object Meta 是对文件的属性描述，包括 H
