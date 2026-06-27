### 配置命令行选项
ossutil提供了多个命令行选项，支持配置[全局命令行选项](ossutil-overview.md)。命令行选项的优先级最高，可以覆盖配置文件设置或环境变量设置的参数。
重要
通过命令行选项需要传入访问密钥，可能会被日志系统记录，存在密钥泄露的风险，请谨慎使用。
ossutil ls oss://examplebucket -i "your-access-key-id" -k "your-access-key-secret" --region cn-hangzhou
