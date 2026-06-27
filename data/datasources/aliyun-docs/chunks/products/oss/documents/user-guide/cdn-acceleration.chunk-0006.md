### 步骤四：验证加速效果
配置完成后，通过对比测试验证CDN加速域名的性能提升效果。
获取文件访问URL：

| URL 类型 | 获取方式 |
| --- | --- |
| OSS 默认访问 URL | 前往 [Bucket](https://oss.console.aliyun.com/bucket) [列表](https://oss.console.aliyun.com/bucket) ，单击目标 Bucket，在目标文件操作列单击 详情 ，然后单击 复制文件 URL 。 |
| CDN 加速访问 URL | 使用 CDN 加速域名和文件名构造 URL，如 http://example.com/example.jpg （ 不包含签名信息 ）。 |

验证加速效果：使用专业的测速平台或工具（如[云监控一次性拨测工具](https://cloudmonitornext.console.aliyun.com/disposableTest)），对比两个URL访问同一文件的加载时间。
说明
首次检测时，因CDN节点无缓存需回源获取资源，加速效果可能不明显。请于首次检测后，待CDN缓存生效后再次测试。
检查缓存命中状态：通过浏览器的开发者工具（F12），查看资源请求的响应头中X-Cache字段的值：

| 字段值 | 含义 |
| --- | --- |
| 以 HIT 开头 | 成功命中 CDN 缓存，实现了加速效果。 |
| 以 MISS 开头 | 未命中 CDN 缓存，请求已回源至 OSS 获取资源。 |
