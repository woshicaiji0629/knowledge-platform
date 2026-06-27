rant-permissions-to-the-ram-user.md)[用户的权限](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
获取可用的地域ID，以便后续配置身份凭证使用。阿里云CLI将使用您指定的地域发起OpenAPI调用，推荐您选择集群所在地域对应的地域ID。ACK的可用地域请参见[服务接入点](../../ack-managed-and-ack-dedicated/developer-reference/api-cs-2015-12-15-endpoint.md)。
说明
使用阿里云CLI过程中，您可以使用--region选项指定地域发起命令调用，该选项在使用时将忽略默认身份凭证配置及环境变量设置中的地域信息。更多信息，请参见[命令行选项](https://help.aliyun.com/zh/cli/command-line-options)。
使用RAM用户的AccessKey信息配置AK类型凭证，配置文件命名为AkProfile。具体操作，请参见[配置示例](https://help.aliyun.com/zh/cli/configure-credentials/#237984d36ci83)。
