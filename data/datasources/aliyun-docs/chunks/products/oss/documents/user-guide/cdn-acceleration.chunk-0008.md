### 多Bucket回源配置
当业务架构依赖于多个OSS Bucket存储不同类型或归属的资源时，可通过以下两种方案配置多源回源。
方式一：独立子域名架构
为不同功能或资源类型的Bucket分配独立的、语义化的子域名，并为每个子域名配置单独的CDN加速。

| 资源类型 | 子域名示例 | 配置建议 |
| --- | --- | --- |
| 图片资源 | img.example.com | 配置长期缓存策略以提升访问速度 |
| 音视频资源 | video.example.com | 启用 Range 回源支持断点续传 |
| 敏感文档 | docs.example.com | 单独启用 URL 鉴权保障安全 |

使用独立子域名架构具备以下优势：
语义化子域名便于开发团队识别和维护。
在DNS层面实现流量分流，避免单一域名的并发连接限制。
各Bucket的缓存策略、安全配置、监控告警可独立设置。
独立的监控体系能够精确定位性能瓶颈和异常流量。
方式二：统一域名路径路由
当多个Bucket分属不同业务或应用，却希望对外提供统一访问入口时，可配置单一CDN加速域名，利用[规则引擎](../../../cdn/documents/user-guide/rules-engine.md)将不同访问路径的请求回源至指定Bucket。以加速域名oss.example.com回源两个Bucket（cdn-bucket1、cdn-bucket2）为例：
添加源站信息：将cdn-bucket1和cdn-bucket2添加到加速域名的源站信息中，并为域名[配置](cdn-acceleration.md)[CNAME](cdn-acceleration.md)[解析规则](cdn-acceleration.md)。
添加路径规则：在加速域名的添加规则中，添加两条URL路径规则，分别匹配http://oss.example.com/bucket1/*和http://oss.example.com/bucket2/*。

| 规则名称 | 类型 | 匹配运算符 | 匹配值 |
| --- | --- | --- | --- |
| bucket1（可自定义） | URI | 包含其中任意一个 | /bucket1/* |
| bucket2（可自定义） | URI | 包含其中任意一个 | /bucket2/* |

添加条件源站：在加速域名的基本配置中新增条件源站，按路径规则匹配源站。

| 规则条件 | 源站地址 |
| --- | --- |
| bucket1 | cdn-bucket1.oss-<region-id>.aliyuncs.com |
| bucket2 | cdn-bucket2.oss-<region-id>.aliyuncs.com |
