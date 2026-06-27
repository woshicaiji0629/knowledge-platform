### 结合阿里云CDN实现静态资源的加速和分发，提高资源访问速度
阿里云内容分发网络CDN（Content Delivery Network）是建立并覆盖在承载网之上，由遍布全球的边缘节点服务器群组成的分布式网络。阿里云CDN能分担源站压力，避免网络拥塞，确保在不同区域、不同场景下加速网站内容的分发，提高资源访问速度。详情参考[什么是阿里云](product-overview/what-is-alibaba-cloud-cdn.md)[CDN](product-overview/what-is-alibaba-cloud-cdn.md)。
在第三步中，云解析DNS返回的CNAME记录值即为CDN为该域名分配的CNAME域名，通过"www.example.com.cname.com"可以访问CDN的调度中心，CDN的调度中心会根据请求用户的信息为其分配最优的CDN节点，用户访问该节点从而达到加速访问的效果。
该文章对您有帮助吗？
反馈
