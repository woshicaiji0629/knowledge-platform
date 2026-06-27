| 1200 万 | 是 | 120 万 | 32 | 8 | 30 | 30 | 30 万/无 | 16/无 |
| ecs.g7t.32xlarge | 128 | 512 | 256 | 64/无 | 2400 万 | 是 | 240 万 | 32 | 15 | 30 | 30 | 60 万/无 | 32/无 |

说明
Intel Ice Lake仅支持基于Intel SGX DCAP的远程证明方式，不支持基于Intel EPID的远程证明方式，您可能需要适配程序后才能正常使用远程证明功能。更多远程证明的信息，请参见[attestation-service](https://software.intel.com/content/www/us/en/develop/topics/software-guard-extensions/attestation-services.html)。
Intel SGX特性与宿主机的硬件绑定，本实例规格族不支持热迁移。
实例变配规格、触发节省停机等操作均可能造成实例所在的宿主机发生变化，请注意本规格族实例的宿主机变化带来的无法解密数据风险。
实例默认未开启宕机自动迁移，您可以自行修改。具体操作，请参见[修改实例维护属性](modify-instance-maintenance-attributes.md)。宕机自动迁移会造成实例所在的宿主机发生变化，请注意本规格族实例的宿主机变化带来的无法解密数据风险。
在创建安全增强型实例时，需要选择专用的镜像才可以使用相关安全特性，更多信息，请参见[创建可信实例](create-a-security-enhanced-instance.md)。
如需使用ecs.g7t.32xlarge，请[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)申请。
