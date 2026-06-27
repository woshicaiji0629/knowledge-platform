## 配置示例
配置示例一：忽略所有参数。

| 配置项 | 填写示例 |
| --- | --- |
| 忽略参数 | 开启 |
| 添加参数 | 无 |
| 删除参数 | 无 |
| 仅保留 | 无 |
| 修改参数 | 无 |
| 规则条件 | 不使用 |
| 结果说明 | 原始请求： http://example.com/index.html?code1=1&code2=2&code3=3 重写后的回源请求： http://example.com/index.html |

配置示例二：保留指定参数。

| 配置项 | 填写示例 |
| --- | --- |
| 忽略参数 | 关闭 |
| 添加参数 | 无 |
| 删除参数 | 无 |
| 仅保留 | code2 |
| 修改参数 | 无 |
| 规则条件 | 不使用 |
| 结果说明 | 原始请求： http://example.com/index.html?code1=1&code2=2&code3=3 重写后的回源请求： http://example.com/index.html?code2=2 |

配置示例三：添加参数+删除参数+修改参数。

| 配置项 | 填写示例 |
| --- | --- |
| 忽略参数 | 关闭 |
| 添加参数 | code4=4 |
| 删除参数 | code2 |
| 仅保留 | 无 |
| 修改参数 | code3=0 |
| 规则条件 | 不使用 |
| 结果说明 | 原始请求： http://example.com/index.html?code1=1&code2=2&code3=3 重写后的回源请求： http://example.com/index.html?code1=1&code3=0&code4=4 |
