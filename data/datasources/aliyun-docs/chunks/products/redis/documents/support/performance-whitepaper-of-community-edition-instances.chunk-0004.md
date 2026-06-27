## 测试工具
建议优先使用Tair团队开源的[resp-benchmark](https://github.com/tair-opensource/resp-benchmark)工具：
SET、GET等常规测试项与redis-benchmark保持一致，在复杂测试项中采用更贴近真实业务场景的测试模式。
默认启用了多线程能力，最大程度向服务端发送请求增压，避免压测客户端成为性能瓶颈。
若使用redis-benchmark，建议Redis 7.0及以上版本（该版本优化了基准测试工具的多线程支持）。
