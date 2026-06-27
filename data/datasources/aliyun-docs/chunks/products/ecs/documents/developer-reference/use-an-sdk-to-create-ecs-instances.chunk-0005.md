--- | --- |
| [CreateSecurityGroup](../api-createsecuritygroup.md) | RegionId | 地域： cn-hangzhou |
| VpcId | VPC ID： vpc-bp1aag0sb9s4i92i3 **** |  |

给安全组添加防护规则

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [AuthorizeSecurityGroup](../api-authorizesecuritygroup.md) | RegionId | 地域： cn-hangzhou |
| SecurityGroupId | 安全组 ID： sg-bp1esyhwfbqeyudt **** |  |
| IpProtocol | 协议： tcp |  |
| SourceCidrIp | 源 CIDR： 0.0.0.0/0 |  |
| PortRange | 端口范围： Linux 实例： 22/22 Windows 实例： 3389/3389 |  |

创建SSH密钥对
阿里云SSH密钥对是一种安全便捷的登录认证方式，用于在SSH协议中进行身份验证和加密通信。通过SSH密钥对，您可以实现免密码远程登录。

| API | 参数 | 示例取值 |
| --- | --- | --- |
| [CreateKeyPair](../api-createkeypair.md) | RegionId | 地域： cn-hangzhou |
| KeyPairName | 密钥对名称： sdk-key-pair |  |

创建ECS实例
使用ECS您可以快速部署和运行应用程序，灵活调整资源以应对业务变化，同时享受高性能、高安全性和低成本的计算能力，适用于网站托管、应用开发、数据处理等多种场景。
