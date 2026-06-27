## 步骤二：配置阿里云CLI
重要
阿里云账号（主账号）拥有所有产品OpenAPI的管理和访问权限，风险很高。强烈建议您创建RAM用户（子账号），并依据最小化权限原则授予权限，使用RAM用户身份访问OpenAPI。关于ACK支持的系统权限策略，请参见[AliyunCSFullAccess](../../../../ram/documents/developer-reference/aliyuncsfullaccess.md)及[AliyunCSReadOnlyAccess](../../../../ram/documents/developer-reference/aliyuncsreadonlyaccess.md)。
使用阿里云CLI之前，您需要在阿里云CLI中配置身份凭证、地域ID等信息。阿里云CLI支持多种身份凭证，详情请参见[身份凭证类型](https://help.aliyun.com/zh/cli/configure-credentials/#30ab0f9c3eovm)。阿里云CLI支持使用RAM用户的AccessKey信息配置AK类型身份凭证，具体操作流程如下。
创建一个RAM用户，并创建AccessKey，以便后续配置身份凭证使用。具体操作，请参见[创建](../../../../ram/documents/create-a-ram-user-1.md)[RAM](../../../../ram/documents/create-a-ram-user-1.md)[用户](../../../../ram/documents/create-a-ram-user-1.md)及[创建](../../../../ram/documents/user-guide/create-an-accesskey-pair.md)[AccessKey](../../../../ram/documents/user-guide/create-an-accesskey-pair.md)。
为RAM用户授权。本文示例需授予RAM用户只读访问ACK的权限AliyunCSReadOnlyAccess。具体操作，请参见[管理](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户的权限](../../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
获取可用的地域ID，以便后续配置身份凭证使用。阿里云CLI将使用您指定的地域发起
