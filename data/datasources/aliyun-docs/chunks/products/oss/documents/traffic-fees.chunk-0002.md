### 流出流量

| 计费项 | 计费项 Code | 计费规则 | 是否计费 |
| --- | --- | --- | --- |
| 外网流出流量 | NetworkOut | 通过外网 Endpoint（示例值 oss-cn-hangzhou.aliyuncs.com）或者传输加速 Endpoint（示例值 oss-accelerate.aliyuncs.com）调用 GetObject 接口访问、下载、预览文件或者进行图片处理操作产生的流量。 说明 使用传输加速 Endpoint 请求 OSS 资源时，还会产生 [传输加速费用](transfer-acceleration-fees.md) 。 外网流出流量费用=外网流出流量（GB）×每 GB 单价 | 是 |
| 内网流出流量 | 不涉及 | 通过内网 Endpoint（示例值 oss-cn-hangzhou-internal.aliyuncs.com）调用 GetObject 接口访问、下载、预览文件或者进行图片处理操作产生的流量。 | 否 |
