## API
[创建自定义域名](developer-reference/api-sls-2020-12-30-createdomain.md)。
自定义域名绑定 SSL 证书
现状说明：日志服务控制台目前不支持直接上传或绑定 SSL 证书到自定义域名。
解决方案：
方案一（推荐方案）：通过 CDN/SLB 间接实现。使用阿里云 CDN 加速 SLS 域名，在 CDN 控制台绑定 SSL 证书，通过 CDN 访问；或使用 SLB 负载均衡配置 HTTPS 监听并绑定证书，后端指向 SLS 公网地址。
方案二（默认方案）：使用 SLS 默认域名。SLS 内置的默认域名已默认支持 HTTPS 及内置 SSL 证书，无需额外配置。如无特殊需求，可直接使用默认域名。
