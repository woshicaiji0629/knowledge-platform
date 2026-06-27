### 示例二：执行break规则。

| 待重写的 Path | ^/hello.jpg$ |
| --- | --- |
| 目标 Path | /image/hello.jpg |
| 执行规则 | break |
| 结果说明 | 原始请求： http://example.com/hello.jpg 重写后的回源请求： http://example.com/image/hello.jpg 该请求将不再继续匹配 重写回源路径 规则列表中其余的规则。 |
