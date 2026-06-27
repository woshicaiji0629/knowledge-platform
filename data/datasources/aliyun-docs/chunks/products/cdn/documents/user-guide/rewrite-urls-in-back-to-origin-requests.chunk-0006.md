### 示例一：执行空规则。

| 待重写的 Path | ^/hello$ |
| --- | --- |
| 目标 Path | /index.html |
| 执行规则 | 空 |
| 结果说明 | 原始请求： http://example.com/hello 重写后的回源请求： http://example.com/index.html 该请求将会继续匹配 重写回源路径 规则列表中其余的规则。 |
