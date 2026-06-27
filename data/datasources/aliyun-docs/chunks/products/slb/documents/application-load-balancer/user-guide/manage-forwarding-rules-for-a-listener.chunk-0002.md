| 域名： api.example.com ，路径： /* | 转发至服务器组 B | 精确域名 + 所有路径，优先级次之 |
| 3 | 域名： *.example.com | 转发至服务器组 C | 通配域名，优先级再次之 |
| 默认 | -（匹配所有请求） | 转发至服务器组 D | 兜底规则，优先级最低 |

请求api.example.com/v2/users匹配规则 1，转发至服务器组 A。
请求api.example.com/v1/users不匹配规则 1（路径不满足/v2/*），匹配规则 2，转发至服务器组 B。
请求web.example.com/index不匹配规则 1、2（域名不满足），匹配规则 3，转发至服务器组 C。
请求other.com/page不匹配任何规则，按默认规则转发至服务器组 D。
