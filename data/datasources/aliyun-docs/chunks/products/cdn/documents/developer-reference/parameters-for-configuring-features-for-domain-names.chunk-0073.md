an-ip-blacklist-or-whitelist.md)[IP](../user-guide/configure-an-ip-blacklist-or-whitelist.md)[黑/白名单](../user-guide/configure-an-ip-blacklist-or-whitelist.md)。
功能冲突说明：IP白名单功能与IP黑名单功能（功能函数：ip_black_list_set，功能ID：13）存在冲突，只能二选其一。如果已经配置了其中一个功能（注意：如果功能函数存在功能开关配置参数，在参数被置为off的情况下，也属于已存在配置），则必须删除已经添加的功能配置（您可以通过调用[DeleteSpecificConfig](api-cdn-2018-05-10-deletespecificconfig.md)接口来删除域名的指定配置），然后才能给另一个功能添加配置。
功能ID（FunctionID/FuncId）：69。
参数说明：
