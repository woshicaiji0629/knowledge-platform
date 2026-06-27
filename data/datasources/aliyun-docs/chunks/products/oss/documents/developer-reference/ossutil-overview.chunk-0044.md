### 命令列表
ossutil 提供了三类命令：
高级命令
用于常用的存储空间或者对象的操作场景，例如存储空间创建、删除、数据拷贝、对象属性修改等。

| 命令名 | 含义 |
| --- | --- |
| [mb](mb-create-storage-space.md) | 创建存储空间 |
| [rb](rb-delete-bucket.md) | 删除存储空间 |
| [du](du-get-size.md) | 获取存储或者指定前缀所占的存储空间大小 |
| [stat](stat2.md) | 显示存储空间或者对象的描述信息 |
| [mkdir](mkdir-create-directory.md) | 创建一个名字有后缀字符 / 的对象 |
| [append](append-append-upload.md) | 将内容上传到追加类型的对象末尾 |
| [cat](cat-output-file-contents.md) | 将对象内容连接到标准输出 |
| [ls](ls-list-resources-under-the-account-level.md) | 列举存储空间或者对象 |
| [cp](cp-upload-download-and-copy-files.md) | 上传、下载或拷贝对象 |
| [rm](rm-deleted.md) | 删除存储空间里的对象 |
| [set-props](set-props-set-object-properties.md) | 设置对象的属性 |
| [presign](presign-generate-presigned-url.md) | 生成对象的预签名 URL |
| [restore](restore-unfrozen-file.md) | 恢复冷冻状态的对象为可读状态 |
| [revert（恢复版本）](revert-recovery-version.md) | 将对象恢复成指定的版本 |
| [sync](sync-synchronizing-files.md) | 将本地文件目录或者对象从源端同步到目的端 |
| [hash](hash-calculate-crc64-or-md5.md) | 计算文件/对象的哈希值 |

API级命令，提供了API操作的直接访问，支持该接口的配置参数。
说明
仅列举部分命令，可以通过ossutil api -h查看所有命令。
