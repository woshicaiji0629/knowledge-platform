## Windows系统
在CMD中运行以下命令。
setx OSS_ACCESS_KEY_ID "your-access-key-id" setx OSS_ACCESS_KEY_SECRET "your-access-key-secret"
打开一个新的CMD窗口。
在新的CMD窗口运行以下命令，检查环境变量是否生效。
echo %OSS_ACCESS_KEY_ID% echo %OSS_ACCESS_KEY_SECRET%
当前支持配置的环境变量如下：

| 环境变量名 | 对应的参数名 |
| --- | --- |
| OSS_ACCESS_KEY_ID | access-key-id |
| OSS_ACCESS_KEY_SECRET | access-key-secret |
| OSS_SESSION_TOKEN | sts-token |
| OSS_ROLE_ARN | ram-role-arn |
| OSS_ROLE_SESSION_NAME | role-session-name |
| OSS_REGION | region |
| OSS_ENDPOINT | endpoint |
| OSSUTIL_CONFIG_FILE | config-file |
| OSSUTIL_PROFILE | profile |
