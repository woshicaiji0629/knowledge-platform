### 通配符

| 通配符号 | 含义 | 路径匹配示例 |
| --- | --- | --- |
| ? | 表示匹配任意 1 个字符。 | /img/?.png 匹配 /img/a.png 、 /img/b.png 等单字符文件名的资源。 |
| * | 表示匹配任意多个字符。 | /api/* 匹配 /api/ 下的所有路径（如 /api/v1/users 、 /api/v2/products ）； /static/*.css 匹配 /static/ 目录下所有 CSS 文件。 |
