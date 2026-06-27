## 私有Bucket
访问私有读写权限的Bucket需要在文件URL中包含签名信息。以下操作演示如何通过控制台获取文件的签名URL，关于签名的详细信息和生成方式请参见[签名版本](../developer-reference/add-signatures-to-urls.md)[4（推荐）](../developer-reference/add-signatures-to-urls.md)。
前往[Bucket](https://oss.console.aliyun.com/bucket)[列表](https://oss.console.aliyun.com/bucket)，单击目标Bucket。
单击需要访问的目标文件右侧操作列的详情。
单击复制文件 URL，并将URL中的外网访问域名（如oss-cn-hangzhou.aliyuncs.com）替换为传输加速访问域名（oss-accelerate.aliyuncs.com）。
在浏览器中访问修改后的URL。
重要
使用SDK、ossutil、ossbrowser等访问OSS时，Endpoint应配置为oss-accelerate.aliyuncs.com，不要包含Bucket名称。如果误将Endpoint配置为<BucketName>.oss-accelerate.aliyuncs.com，会导致域名解析失败。
