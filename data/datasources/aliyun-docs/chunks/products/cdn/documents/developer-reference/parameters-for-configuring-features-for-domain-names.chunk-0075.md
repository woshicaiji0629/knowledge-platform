ip 作为判断依据。 all：同时使用 x-forwarded-for 和 真实连接 ip 作为判断依据。 | all |
| ip_list_notes | String | 否 | 备注信息，用于记录 IP 列表的备注说明信息。 | 192.x.x.1（恶意 IP 地址） 192.x.x.2（灰产 IP 地址） |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "ip_list", "argValue": "192.168.0.1/24" }], "functionName": "ip_allow_list_set" }], "DomainNames": "example.com" }
ip_black_list_set
功能说明：配置IP黑名单，该功能详细介绍请参见控制台配置说明[配置](../user-guide/configure-an-ip-blacklist-or-whitelist.md)[IP](../user-guide/configure-an-ip-blacklist-or-whitelist.md)[黑/白名单](../user-guide/configure-an-ip-blacklist-or-whitelist.md)。
功能冲突说明：IP黑名单功能与IP白名单功能（功能函数：ip_allow_list_set，功能ID：69）存在冲突，只能二选其一。如果已经配置了其中一个功能（注意：如果功能函数存在功能开关配置参数，在参数被置为off的情况下，也属于已存在配置），则必须删除已经添加的功能配置（您可以通过调用[DeleteSpecificConfig](api-cdn-2018-05-10-deletespecificconfig.md)接口来删除域名的指定配置），然后才能给另一个功能添加配置。
功能ID（FunctionID/FuncId）：13。
参数说明：
