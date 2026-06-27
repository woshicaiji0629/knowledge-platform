### 示例三：源站类型为OSS域名
当源站信息为 OSS 域名时，将会同步开启默认回源HOST功能，并且设置域名类型为源站域名。

| 域名 | 说明 |
| --- | --- |
| 加速域名： example.com 源站地址： example.oss-cn-hangzhou.aliyuncs.com | 回源域名类型说明： • 加速域名 ：当回源时，会到 example.oss-cn-hangzhou.aliyuncs.com OSS 域名上的 example.com 站点获取资源。 • 源站域名 ：当回源时，会到 OSS 域名 example.oss-cn-hangzhou.aliyuncs.com 获取资源。 • 自定义域名 ：当回源时，会到 example.oss-cn-hangzhou.aliyuncs.com 站点上自定义域名的虚拟站点获取资源。 |
