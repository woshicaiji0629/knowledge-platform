### ERR command 'xxx' not support for your account
可能原因：阿里云禁止用户执行某些Tair命令，或您手动在#no_loose_disabled-commands参数中配置了禁止执行的命令。更多信息请参见[Redis](../developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)[开源版命令支持](../developer-reference/commands-supported-by-apsaradb-for-redis-community-edition.md)和[禁用高风险命令](../user-guide/disable-high-risk-commands.md)。
解决方法：若需执行您禁用的命令，您可以在#no_loose_disabled-commands参数中删除对应命令。
