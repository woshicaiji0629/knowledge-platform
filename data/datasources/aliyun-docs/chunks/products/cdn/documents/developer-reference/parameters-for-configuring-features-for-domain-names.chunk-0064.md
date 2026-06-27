HTTP 或 HTTPS 协议头部，则依然视为有效 referer 进行处理。示例： 取值为 on 时，referer 格式如下： referer: www.example.com 取值为 off（默认值）时，referer 格式如下： referer: https://www.example.com | off |

配置示例：
{ "Functions": [{ "functionArgs": [{ "argName": "allow_empty", "argValue": "off" }, { "argName": "refer_domain_allow_list", "argValue": "example.aliyundoc.com,demo.aliyundoc.com" }], "functionName": "referer_white_list_set" }], "DomainNames": "example.com" }
referer_black_list_set
功能说明：配置Referer黑名单，该功能详细介绍请参见控制台配置说明[配置](../user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)[Referer](../user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)[黑/白名单](../user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)。
功能冲突说明：Referer黑名单功能与Referer白名单功能（功能函数：referer_white_list_set，功能ID：1）存在冲突，只能二选其一。如果已经配置了其中一个功能（注意：如果功能函数存在功能开关配置参数，在参数被置为off的情况下，也属于已存在配置），则必须删除已经添加的功能配置（您可以通过调用[DeleteSpecificConfig](api-cdn-2018-05-10-deletespecificconfig.md)接口来删除域名的指定配置），然后才能给另一个功能添加配置。
功能ID（FunctionID/FuncId）：5。
参数说明：
