## 加速原理
CDN接管域名解析，将用户请求智能地引导至最近的CDN节点，如果该最佳节点已[缓存](https://www.aliyun.com/getting-started/what-is/what-is-cache)该资源，当终端用户请求访问和获取源站资源时无需回源，从而实现加速。
假设您的加速域名为www.aliyundoc.com，接入CDN开始加速服务后，当终端用户在北京发起HTTP请求时，处理流程如下图所示。
用户发起请求：当终端用户向www.aliyundoc.com下的指定资源发起请求时，首先向Local DNS（本地DNS）发起请求域名www.aliyundoc.com对应的IP。
解析请求转发：Local DNS检查缓存中是否有www.aliyundoc.com的IP地址记录。如果有，则直接返回给终端用户；如果没有，则向网站授权DNS请求域名www.aliyundoc.com的解析记录。
CNAME配置生效：当网站授权DNS解析www.aliyundoc.com后，返回域名的CNAMEwww.aliyundoc.com.example.com。
智能调度：Local DNS向阿里云CDN的DNS调度系统请求域名www.aliyundoc.com.example.com的解析记录，阿里云CDN的DNS调度系统将为其分配最佳节点IP地址。
返回最佳节点IP：Local DNS获取阿里云CDN的DNS调度系统返回的最佳节点IP地址。
用户访问节点：Local DNS将最佳节点IP地址返回给用户，用户获取到最佳节点IP地址，向最佳节点IP地址发起对该资源的访问请求。
节点响应：
缓存命中：如果该最佳节点已缓存该资源，则会将请求的资源直接返回给用户（步骤8），此时请求结束。
缓存未命中：如果该最佳节点未缓存该资源或者缓存的资源已经失效，则节点将会向源站发起对该资源的请求。获取源站资源后结合用户自定义配置的缓存策略，将资源缓存到CDN节点并返回给用户（步骤8），此时请求结束。配置缓存策略的操作方法，请参见[配置缓存过期时间](../user-guide/configure-the-cdn-cache-expiration-time.md)。
