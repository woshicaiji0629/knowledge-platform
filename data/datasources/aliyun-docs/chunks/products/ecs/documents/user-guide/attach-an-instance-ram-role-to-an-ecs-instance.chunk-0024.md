nstall-cli-on-macos)
配置身份凭据。
aliyun configure --profile EcsProfile --mode EcsRamRole
该命令为交互式命令，需要根据提示输入相应信息。更多信息请参见[配置凭证](https://help.aliyun.com/zh/cli/configure-credentials/#4d37882a4dx9h)。交互过程示例：
Configuring profile 'EcsProfile' in 'EcsRamRole' authenticate mode... Ecs Ram Role []:YOUR_ROLE_NAMEDefault Region Id []:YOUR_REGIONDefault Output Format [json]: json (Only support json) Default Language [zh|en] en: en Saving profile[EcsProfile] ...Done.
调用API。例如，使用CLI查询ECS实例列表。
aliyun ecs DescribeInstances
更多关于CLI命令的说明，请参见[命令结构](https://help.aliyun.com/zh/cli/understanding-command-structure)。
