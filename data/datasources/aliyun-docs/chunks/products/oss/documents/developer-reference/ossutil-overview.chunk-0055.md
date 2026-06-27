|
| --sign-version | string | 请求使用的签名算法版本。取值： v1 v4（默认值） |
| --skip-verify-cert | / | 表示不校验服务端的数字证书。 |
| -t, --sts-token | string | 访问 OSS 使用的 STS Token。 |
| --proxy | string | 指定代理服务器。自 2.0.1 版本起支持。 配置值可以为以下几种： 直接配置：可以直接指定代理服务器的详细信息，例如： http://proxy.example.com:8080 https://proxy.example.com:8443 env ：表示使用环境变量 HTTP_PROXY 和 HTTPS_PROXY 来获取代理服务器信息。用户需要在操作系统中配置这两个环境变量，例如： HTTP_PROXY=http://proxy.example.com:8080 HTTPS_PROXY=https://proxy.example.com:8443 配置这些环境变量后，将代理服务器选项的值设置为 env ，系统将自动使用这些环境变量中的代理设置。 |
| --log-file | string | 指定日志输出文件，自 2.0.1 版本起支持。配置值为： - ：表示将日志输出到标准输出（Stdout）。 文件路径 ：指定一个具体的文件路径，将日志输出到该文件。 如果未指定日志输出文件，输出到默认配置文件上。 |
| --cloudbox-id | string | 云盒 ID，应用于云盒场景。自 2.1.0 版本起支持。 |
| --ignore-env-var | / | 忽略所有以 OSS_ 为前缀的环境变量配置。自 2.2.0 版本起支持。 |
| --bind-address | string | 指定出站连接所绑定的本地 IP 地址（支持 IPv4、IPv6）。自 2.2.0 版本起支持。 |
| --account-id | string | 账号 ID，用于向量 Bucket 场景中的身份识别与资源归属判断。自 2.2.0 版本起支持。 |
| --user-agent | string | 在默认的 User-Agent 末尾追加指定的值。自 2.2.2 版本起支持。 |
