essTimeout credential_process_timeout | 用于指定外部凭证请求的超时时间，单位为秒。默认值为 15 即指定 15 秒；最大值为 600 即指定 10 分钟； credential-process-timeout = 60 即指定 60 秒的超时时间。自 2.0.3 版本起支持。 |

全局参数

| 参数名 | 别名 | 含义 |
| --- | --- | --- |
| region | / | 地域 ID，必须设置。 |
| loglevel | / | 日志级别 。取值： off（默认值） info debug |
| read-timeout | readTimeout read_timeout | 客户端读写请求超时时间。单位为秒，默认值 20。 |
| connect-timeout | connectTimeout connect_timeout | 客户端连接超时的时间。单位为秒，默认值 10。 |
| retry-times | retryTimes retry_times | 当错误发生时的重试次数。默认值 10。 |
| skip-verify-cert | skipVerifyCert skip_verify_cert | 不校验服务端的数字证书。 |
| sign-version | signVersion sign_version | 请求使用的签名算法版本。取值： v1 v4（默认值） |
| output-format | outputFormat output_format | 输出格式。取值： raw（默认值） json xml yaml |
| addressing-style | addressingStyle addressing_style | 请求地址的格式 。取值： virtual（默认值） path cname |
| language | / | 显示的语言。 |
| endpoint | / | 对外服务的访问域名，可不设置。 |

其它参数
