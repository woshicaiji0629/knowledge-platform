## 工作原理与优势
工作原理：功能开启后，CDN向您的私有OSS Bucket发起回源请求时，会自动在请求头（Header）中添加一个Authorization字段。该字段的值是根据您授权的身份信息（STS临时令牌或AccessKey）生成的有效签名，OSS服务会据此对请求进行鉴权。
安全访问：通过为CDN授予一个受限的只读权限，确保了回源请求的合法性，避免了将私有Bucket设置为公开所带来的安全风险。
成本优化：终端用户访问将命中CDN缓存，其流量费用远低于直接访问OSS产生的外网流出流量。同时，CDN回源到OSS的流量会计为CDN回源流量，其单价也低于OSS外网流出流量单价，有效降低总体成本。具体请参见[CDN](../product-overview/billing-of-oss-content-acceleration.md)[加速](../product-overview/billing-of-oss-content-acceleration.md)[OSS](../product-overview/billing-of-oss-content-acceleration.md)[计费说明](../product-overview/billing-of-oss-content-acceleration.md)
