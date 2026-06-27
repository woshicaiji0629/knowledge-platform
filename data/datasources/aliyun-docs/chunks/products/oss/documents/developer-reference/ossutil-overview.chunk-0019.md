访问点的映射关系。支持嵌套写法，即buckets节按bucket-name = 行分成多个小节。格式如下：
[buckets name] bucket-name = key=value
其中，name为该buckets节的名字，bucket-name为具体的Bucket名字，key=value配置参数，支持的参数如下：

| 参数名 | 别名 | 含义 |
| --- | --- | --- |
| region | / | 数据中心所在的地域。 当不设置时，使用引入该参数的 profile 里的 region 值。 |
| endpoint | / | 对外服务的访问域名，可不设置。 |
| addressing-style | addressingStyle addressing_style | 请求地址的格式。取值： virtual（默认值）：使用 Bucket 虚拟域名请求地址格式。 path：使用 path style 请求地址格式。 cname：使用 cname 请求地址格式。 |

节类型buckets示例如下：
[buckets dev-bucket] bucket-hz-01 = region=cn-hangzhou bucket-hz-02 = region=cn-hangzhou endpoint=test.com addressing-style=cname bucket-bj-01 = region=cn-beijing
