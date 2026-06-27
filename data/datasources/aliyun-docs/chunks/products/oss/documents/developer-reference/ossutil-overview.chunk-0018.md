addressing-style | addressingStyle addressing_style | 请求地址的格式 。取值： virtual（默认值） path cname |
| language | / | 显示的语言。 |
| endpoint | / | 对外服务的访问域名，可不设置。 |

其它参数

| 参数名 | 别名 | 含义 |
| --- | --- | --- |
| source-profile | sourceProfile source_profile | 引用指定 profile 里的参数，例如： [profile cred] access-key-id=ak access-key-secret=sk [profile dev] region=cn-hangzhou source-profile=cred |
| buckets | / | 引用指定 buckets 里的参数。 [profile dev] region=cn-hangzhou access-key-id=ak access-key-secret=sk buckets=dev-bucket [buckets dev-bucket] bucket-name-hz = endpoint=oss-cn-hangzhou-internal.aliyuncs.com bucket-name-bj = region=cn-beijing |
| endpoint-suffix-list-path-style | / | 指定自动使用 path-style 请求模式的 Endpoint 后缀列表，多个后缀以英文逗号（ , ）分隔。自 2.2.0 版本起支持。 示例 1： endpoint-suffix-list-path-style=DEFAULT 示例 2： endpoint-suffix-list-path-style=DEFAULT,.path-style.com DEFAULT：表示内置的缺省列表，当前为 .privatelink.aliyuncs.com |

节类型：buckets
用于配置特定Bucket和访问点的映射关系。支持嵌套写法，即buckets节按bucket-name = 行分成多个小节。格式如下：
[buckets name] bucket-name = key=value
其中，name为该buckets节的名字，bucket-name为具体的Bucket名字，key=value配置参数，支持的参数如下：
