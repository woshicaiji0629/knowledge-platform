## 解决方案
在使用alicloud_cdn_domain_new新建CDN域名且添加HTTPS证书的时候，当cert_type设置为"cas"时：
若当前账号是阿里云国际站账号，cert_region必填，且cert_region="ap-southeast-1"。
若当前账号不是阿里云国际账号，cert_region非必填，cert_region="cn-hangzhou"。
例如：
