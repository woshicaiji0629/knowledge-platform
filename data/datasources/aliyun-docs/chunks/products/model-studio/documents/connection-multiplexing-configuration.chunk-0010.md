## 最佳实践
Java SDK：根据业务并发量合理配置connectionPoolSize、maximumAsyncRequests等参数，避免连接数过高或过低。
Python SDK：推荐使用with语句自动管理 Session 的生命周期，确保资源正确释放。
选择合适的调用方式：如果您的应用是异步架构（如使用 asyncio、FastAPI 等），建议使用异步调用方式；如果是传统同步架构，使用同步调用方式即可。
