## 前提条件
在初次使用CDN之前，您需要先开通CDN服务，请参见[开通](../activate-alibaba-cloud-cdn.md)[CDN](../activate-alibaba-cloud-cdn.md)[服务](../activate-alibaba-cloud-cdn.md)。
为了降低信息安全风险，建议使用最小权限的RAM用户完成此教程的操作。请参见[创建](../../../ram/documents/user-guide/create-a-ram-user.md)[RAM](../../../ram/documents/user-guide/create-a-ram-user.md)[用户](../../../ram/documents/user-guide/create-a-ram-user.md)与[管理](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[RAM](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)[用户的权限](../../../ram/documents/user-guide/grant-permissions-to-the-ram-user.md)，完成此教程所需最小权限的权限策略如下：
{ "Version": "1", "Statement": [ { "Effect": "Allow", "Action": [ "cdn:AddCdnDomain", "cdn:DescribeCdnDomainDetail", "cdn:DescribeDomainCertificateInfo", "cdn:ListTagResources", "cdn:DeleteCdnDomain", "cdn:BatchSetCdnDomainConfig", "cdn:DescribeCdnDomainConfigs", "cdn:DeleteSpecificConfig" ], "Resource": "*" } ] }
准备Terraform运行环境，您可以选择以下任一方式来使用Terraform。
[Explorer](https://help.aliyun.com/zh/terraform/using-terraform-in-terraform-explorer)：阿里云提供了Terraform的在线运行环境，您无需安装Terraform，登录后即可在线使用和体验Terraform。适用于零成本、快速、便捷地体验和调试Terraform的场景。
[使用](https://help.aliyun.com/zh/terraform
