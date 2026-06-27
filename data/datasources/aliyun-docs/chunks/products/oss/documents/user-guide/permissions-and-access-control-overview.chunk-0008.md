### 接入点
[接入点](access-point.md)（Access Point）为Bucket提供独立的访问入口。当一个Bucket需要被多个应用或团队以不同权限访问时，可为每个访问方创建独立的接入点，通过接入点策略（AP Policy）分别管理各自的权限，避免在单一Bucket Policy中维护复杂的规则。
每个接入点拥有独立的访问域名、AP Policy和网络限制配置。用户通过接入点访问时，需要RAM Policy与Bucket Policy的合并结果为Allow，且AP Policy也为Allow，请求才通过。
