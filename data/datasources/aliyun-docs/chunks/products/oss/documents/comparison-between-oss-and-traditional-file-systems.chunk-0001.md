## 概念对应
下表为OSS与文件系统的概念对应说明。

| 对象存储 OSS | 文件系统 |
| --- | --- |
| Object | 文件 |
| Bucket | 主目录 |
| Region | 无 |
| Endpoint | 无 |
| AccessKey | 无 |
| 无 | 多级目录 |
| GetService | 获取主目录列表 |
| GetBucket | 获取文件列表 |
| PutObject | 写文件 |
| AppendObject | 追加写文件 |
| GetObject | 读文件 |
| DeleteObject | 删除文件 |
| 无 | 修改文件内容 |
| CopyObject （目标文件和源文件相同） | 修改文件属性 |
| CopyObject（目标文件和源文件不同） | 复制文件 |
| CopyObject+DeleteObject | 重命名文件 |

该文章对您有帮助吗？
反馈
