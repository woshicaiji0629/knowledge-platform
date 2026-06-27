### 示例五：在文件名是变量的情况下对指定目录添加URL前缀。
例如：将包含/live/xxx的URL（xxx代表任意文件名称，例如：/live/hello.jpg、/live/hello.html 等等）重写为/image/live/xxx，即对目录/live下的任意文件的URL都插入路径/image。

| 待重写的 Path | ^/live/(.*)$ |
| --- | --- |
| 目标 Path | /image/live/$1 |
| 执行规则 | break |
| 结果说明 | 原始请求： http://example.com/live/hello.jpg 重写后的回源请求： http://example.com/image/live/hello.jpg 原始请求： http://example.com/live/hello.html 重写后的回源请求： http://example.com/image/live/hello.html 该请求将不再继续匹配 回源 URL 重写 规则列表中其余的规则。 |
