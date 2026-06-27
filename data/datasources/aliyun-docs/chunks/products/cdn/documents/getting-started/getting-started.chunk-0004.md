### 阶段三：配置CNAME并切换流量
[验证加速域名是否可用](quick-access-to-alibaba-cloud-cdn.md)：成功添加加速域名后，为保证DNS解析可以顺利切换而不影响现有业务，建议您先在本地测试加速域名，验证加速域名访问正常后，再将加速域名的DNS解析记录指向CNAME域名。
[配置](quick-access-to-alibaba-cloud-cdn.md)[CNAME](quick-access-to-alibaba-cloud-cdn.md)：添加域名后，阿里云CDN会为您分配对应的CNAME域名，您需要在DNS服务商处将加速域名的DNS解析记录指向分配的CNAME域名，CDN服务才能生效。
