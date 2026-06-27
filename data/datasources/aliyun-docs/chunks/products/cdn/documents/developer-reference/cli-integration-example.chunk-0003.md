## 配置阿里云CLI
重要
阿里云账号（主账号）拥有所有产品API的管理和访问权限，风险很高。强烈建议您创建并使用RAM用户进行API访问或日常运维。
使用阿里云CLI之前，您需要在阿里云CLI中配置身份凭证、地域ID等信息。阿里云CLI支持多种身份凭证，详情请参见[配置与管理身份凭证](https://help.aliyun.com/zh/cli/configure-credentials/#30ab0f9c3eovm)。本文操作以AK类型凭证为例，具体操作步骤如下：
您需要创建一个RAM用户并授予相应操作权限。具体操作，请参见[创建](../../../ram/documents/create-a-ram-user-1.md)[RAM](../../../ram/documents/create-a-ram-user-1.md)[用户](../../../ram/documents/create-a-ram-user-1.md)及[管理](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户的权限](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)。
重要
本示例需要您为RAM用户授予AliyunCDNReadOnlyAccess权限策略。您也可以按需选择AliyunCDNFullAccess权限（具有查询、修改CDN域名的完全控制权限）或进行自定义策略，更多信息请参见[CDN](../security-and-compliance/custom-policies-for-dcdn.md)[自定义权限策略参考](../security-and-compliance/custom-policies-for-dcdn.md)。
创建RAM用户并授权后，您需要创建RAM用户对应的AccessKey，并记录AccessKey ID和AccessKey Secret，以便后续配置身份凭证使用。具体操作，请参见[创建](../../../ram/documents/user-guide/create-an-accesskey-pair.md)[AccessKey](../../../ram/documents/user-guide/create-an-accesskey-pair.md)。
您需要获取并记录可用的地域ID，以便后续配置身份凭证使用。阿里云CLI将使用您指定的地域发起API调用，可用地域请参见[请求结构](htt
