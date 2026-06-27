### 收集前端日志
日志服务提供webTracking功能，用以收集小程序/客户端（iOS/Android/APP）/浏览器上的日志数据。
该功能有两种使用方式：
通过[使用](use-the-web-tracking-feature-to-collect-logs.md)[STS](use-the-web-tracking-feature-to-collect-logs.md)[鉴权方式](use-the-web-tracking-feature-to-collect-logs.md)进行传输，适用于生产场景。该方式无需修改LogStore配置。
通过OpenAPI等进行[匿名传输](use-the-web-tracking-feature-to-collect-logs.md)数据，仅适用于测试场景。需要在LogStore中打开开关，参考下文进行配置。
