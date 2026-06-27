置中新增条件源站，按路径规则匹配源站。

| 规则条件 | 源站地址 |
| --- | --- |
| bucket1 | cdn-bucket1.oss-<region-id>.aliyuncs.com |
| bucket2 | cdn-bucket2.oss-<region-id>.aliyuncs.com |

指定源站回源HOST：在加速域名的回源配置中添加指定源站回源HOST，确保回源请求正确到达目标Bucket。

| 源站类型 | 源站地址 | 回源 HOST 类型 | 回源 HOST | 规则条件 |
| --- | --- | --- | --- | --- |
| 基础源站地址 | cdn-bucket1.oss-<region-id>.aliyuncs.com | 基础源站域名 | cdn-bucket1.oss-<region-id>.aliyuncs.com | bucket1 |
| 基础源站地址 | cdn-bucket2.oss-<region-id>.aliyuncs.com | 基础源站域名 | cdn-bucket2.oss-<region-id>.aliyuncs.com | bucket2 |

重写回源URL：在加速域名的回源配置中添加重写回源路径，在回源时自动剥离虚拟路径（如/bucket1），使回源请求路径与Bucket内对象的实际存储路径一致。

| 待重写的 Path | 目标 Path | 执行规则 |
| --- | --- | --- |
| ^/bucket1/(.*)$ | /$1 | break |
| ^/bucket2/(.*)$ | /$1 | break |

效果验证：配置完成后，即可使用单一CDN加速域名根据不同路径访问不同的OSS Bucket资源。如访问http://oss.example.com/bucket1/example.jpg，将回源到cdn-bucket1根目录下的example.jpg文件。
