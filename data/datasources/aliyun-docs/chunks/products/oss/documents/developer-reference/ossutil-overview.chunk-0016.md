ssing style。 | 支持内联写法。 |

说明
可以使用config命令查看和设置配置内容。更多信息，请参见[config（管理配置文件）](config-create-configuration-file.md)。
节类型：profile
用于配置访问凭证和全局配置参数，支持的参数名如下：
访问凭证相关参数

| 参数名 | 别名 | 含义 |
| --- | --- | --- |
| mode | / | 鉴权模式。 取值：AK、StsToken、RamRoleArn、EcsRamRole、Anonymous。 |
| access-key-id | accessKeyId access_key_id | 访问 OSS 使用的 AccessKey ID。 |
| access-key-secret | accessKeySecret access_key_secret | 访问 OSS 使用的 AccessKey Secret。 |
| sts-token | stsToken sts_token | 访问 OSS 使用的 STS Token。 |
| role-arn | roleArn role_arn | RAM 角色的 ARN，主要用于 RamRoleArn 模式。 |
| role-session-name | roleSessionName role_session_name | 会话名字，主要用于 RamRoleArn 模式。 |
| ecs-role-name | ecsRoleName ecs_role_name | 角色名，主要用于 EcsRamRole 模式。 |
| credential-process | credentialProcess credential_process | 指定一个外部命令。 |
| credential-uri | credentialUri credential_uri | 指定一个获取访问凭证的 URI 地址。 |
| oidc-provider-arn | oidcProviderArn oidc_provider_arn | 指定 OIDC 提供者的 ARN（Aliyun Resource Name），格式为 acs:ram::account-id:oidc-provider/provider-name 。 |
| oidc-token-file-path | oidcTokenFilePath oidc_token_file_path | 指定 OIDC 令牌的文件路径，用于存储 OIDC 令牌。 |
| credential-process-timeout | credentialProcessTimeout credential_process_timeout | 用于指定外部凭证请求的超时时间，单位为秒。默认值为 15 即指定 15 秒；最大值为 600 即指定 10 分钟； credential-process-timeout = 60 即指定 60 秒的超时时间。自 2.0.3 版本起支持。 |
