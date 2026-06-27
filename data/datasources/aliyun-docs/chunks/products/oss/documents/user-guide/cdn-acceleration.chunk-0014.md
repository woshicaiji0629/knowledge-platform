-- | --- |
| Access-Control-Allow-Origin | * | 开启 |
| Access-Control-Allow-Methods | POST,GET, HEAD, PUT, DELETE | 不涉及 |
| Access-Control-Max-Age | 3600 | 不涉及 |

说明
参数设置仅供参考，请结合实际业务场景进行调整。
性能优化：提升大文件与数据传输效率
开启Range回源：对于音视频点播、大文件分发等场景，[配置](../../../cdn/documents/user-guide/object-chunking.md)[Range](../../../cdn/documents/user-guide/object-chunking.md)[回源](../../../cdn/documents/user-guide/object-chunking.md)功能至关重要。它允许CDN节点按需分片请求大文件，可实现视频拖动播放等高级功能，并显著减少回源流量和首屏等待时间。
优化数据传输：为减小JS、CSS、HTML等文本文件的传输体积，可在CDN控制台开启[Gzip](../../../cdn/documents/user-guide/use-the-gzip-compression-feature.md)[压缩](../../../cdn/documents/user-guide/use-the-gzip-compression-feature.md)或[页面优化](../../../cdn/documents/user-guide/enable-html-optimization.md)功能。
说明
开启页面优化或Gzip压缩功能会改变文件的Content-Length和Content-MD5值。如果业务逻辑依赖这些值进行校验，请谨慎开启。
若同时开启页面优化和Gzip压缩功能，页面优化功能将失效，CDN只会对文件进行Gzip压缩。
平滑上线：零停机域名切换
在将现有业务从OSS Bucket域名切换至CDN加速域名时，应采用分阶段切换策略：
准备阶段：完成CDN加速域名的所有配置，并在测试环境中充分验证其功能和性能表现。
灰度发布阶段（建议在业务低峰期）：采用灰度发布的方式将部分业务流量切换至CDN加速域名，通过逐步放量降低切换风险。
验证阶段：密切监控业务访问日志和错误率，分析响应时间、成功率等关键指标，确保服务正常。
全量发布阶段：经过充分验证后，将全量业务流量切换至CDN加速域名。
回滚预案：如遇问题，立即回滚至Bucket域名，并详细分析问题根因后重新部署。
