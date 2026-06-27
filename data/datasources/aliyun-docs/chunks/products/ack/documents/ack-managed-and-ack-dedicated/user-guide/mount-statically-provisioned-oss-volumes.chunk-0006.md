s-1.md) [ARNs](faq-about-oss-volumes-1.md) [或](faq-about-oss-volumes-1.md) [ServiceAccount？](faq-about-oss-volumes-1.md) 。 |
| 角色名称 | 本示例为 demo-role-for-rrsa。 |

创建权限策略。
本示例遵循最小权限原则，[创建一个自定义权限策略](../../../../ram/documents/create-a-custom-policy.md)，授予访问目标OSS Bucket的权限（OSS只读权限或OSS读写权限）。
访问[RAM](https://ram.console.aliyun.com/policies/create)[控制台-创建权限策略](https://ram.console.aliyun.com/policies/create)页面，切换为脚本编辑，按照页面提示配置策略脚本。
若已有授权OSS权限的RAM角色，修改其信任策略即可复用，请参见[使用已存在的](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[RAM](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)[角色并授权](use-rrsa-to-authorize-pods-to-access-different-cloud-services.md)。
