| 参数 | 类型 | 说明 |
| --- | --- | --- |
| -i, --access-key-id | string | 访问 OSS 使用的 AccessKey ID。 |
| -k, --access-key-secret | string | 访问 OSS 使用的 AccessKey Secret。 |
| --addressing-style | string | 请求地址的格式。取值范围如下： virtual（默认值），表示虚拟托管模式 。 path，表示路径模式。 cname，表示自定义域名模式。 |
| -c, --config-file | string | 配置文件的路径。 默认值为 ~\\.ossutilconfig 。 |
| --connect-timeout | int | 客户端连接超时的时间。单位为秒，默认值为 10。 |
| -n, --dry-run | / | 在不进行任何更改的情况下执行试运行。 |
| -e, --endpoint | string | 对外服务的访问域名。 |
| -h, --help | / | 显示帮助信息。 |
| --language | string | 显示的语言。 |
| --loglevel | string | 日志级别。取值范围如下： off（默认值） info debug |
| --mode | string | 鉴权模式。取值： AK，表示访问密钥。 StsToken，表示临时安全凭证。 EcsRamRole，表示使用 ECS 实例角色（RAM Role）进行鉴权。 Anonymous，表示匿名访问。 |
| --output-format | string | 输出格式，默认值为 raw。 |
| --output-query | string | JMESPath 查询条件。 |
| --profile | string | 指定配置文件里的 profile。 |
| -q, --quiet | / | 安静模式，打印尽可能少的信息。 |
| --read-timeout | int | 客户端读写请求超时时间。单位为秒，默认值为 20。 |
| --region | string | 数据中心所在的地域，配置值可设置为 cn-hangzhou。 |
| --retry-times | int | 当错误发生时的重试次数。默认值为 10。 |
| --sign-version | string | 请求使用的签名算法版本。取值： v1 v4（默认值） |
| --skip-verify-cert | / | 表示不校验服务端的数字证书。 |
| -t, --sts-token | string | 访问 OSS 使用的 STS Token。 |
| --
