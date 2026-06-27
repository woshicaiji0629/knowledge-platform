## 问题原因
在使用alicloud_cdn_domain_new新建CDN域名并且添加HTTPS证书的时候，客户在传参里面设置了cert_type参数，并且设置值为cas（表示使用阿里云证书中心的证书）。
在cert_type="cas"的情况下，若为阿里云国际站账号，则必须同时设置cert_region="ap-southeast-1"（国际的阿里云证书中心）；而阿里云中国站账号，则可以不设置，因为cert_region的默认值是cn-hangzhou（中国内地的阿里云证书中心）。
更多关于alicloud_cdn_domain_new的参数信息，敬请参见[alicloud_cdn_domain_new](https://help.aliyun.com/zh/terraform/alicloud-cdn-domain-new)。
