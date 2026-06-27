# 配置监听转发规则-负载均衡(SLB)-阿里云帮助中心

Source: https://help.aliyun.com/zh/slb/application-load-balancer/user-guide/manage-forwarding-rules-for-a-listener

# 配置监听转发规则
如果您需要将客户端请求按指定条件路由到不同的后端服务器组，并对后端响应结果进行处理后返回给客户端，可参考本文配置ALB监听的转发规则。
## 转发规则概述
您可以为ALB实例的一个监听添加多条转发规则。一条转发规则由转发条件（condition）和转发动作（action）两部分组成：转发条件用于匹配请求或响应数据，转发动作按照匹配结果执行对应的处理。一条转发规则中可以定义一个或多个转发条件以及一个或多个转发动作。
按数据链路方向，转发规则分为请求方向转发规则和响应方向转发规则。基础版实例仅支持请求方向转发规则；标准版和WAF增强版实例同时支持请求方向和响应方向转发规则。
对于标准版和WAF增强版的ALB实例，客户端发起请求至ALB，ALB将请求数据通过请求方向转发规则处理后发送至对应的后端服务器，后端服务器的响应数据再经过ALB的响应方向转发规则处理后，返回给客户端。
请求方向转发规则：只能设置请求方向的条件和动作。
响应方向转发规则：可以设置响应方向的条件和动作，同时也可以附加请求方向的条件。
每条转发规则必须包含一条转发至、重定向至或返回固定响应类型的转发动作，以保证客户端请求不会中断。
表 1.基础版实例支持的转发规则
| 分类 | 转发条件 | 转发动作 |
| --- | --- | --- |
| 请求方向 | 域名 、 路径 、 HTTP 标头 | 转发至 、 重定向至 |
表 2.标准版和WAF增强版实例支持的转发规则
| 分类 | 转发条件 | 转发动作 |
| --- | --- | --- |
| 请求方向 | 域名 、 路径 、 HTTP 标头 、 查询字符串 、 HTTP 请求方法 、 Cookie 和 SourceIp 。 | 转发至 、 重定向至 、 返回固定响应 、 重写 、 写入 Header 、 删除 Header 、 限速 、 流量镜像至 和 跨域 。 |
| 响应方向 | 请求方向条件（选填）： 域名 、 路径 、 HTTP 标头 、 查询字符串 、 HTTP 请求方法 、 Cookie 和 SourceIp 。 响应方向条件： 响应中的状态码 和 响应中的标头 。 | 返回固定响应 、 写入 Header 和 删除 Header |
## 匹配原理
匹配策略：每个客户端请求会按照转发规则的优先级顺序（转发规则编号的数值越小，优先级越高）逐条匹配，一旦能够匹配到一条转发规则，立即按照当前转发规则转发流量。
如果在请求方向未匹配到其他转发规则，客户端请求将会按照默认转发规则转发。
如果在响应方向未匹配到转发规则，ALB会直接将响应返回给客户端。
ALB按转发规则编号的优先级顺序逐条匹配，不会自动按域名或路径的精确程度排序。如需精确域名优先匹配，请手动将精确域名的规则调整到通配符或正则规则之前（即编号更小的位置）。此匹配方式与Nginx的最长前缀匹配和CLB的自动域名精度排序不同。
默认转发规则：创建监听后，系统会在请求方向自动创建一条默认转发规则，该转发规则转发条件为-，表示匹配所有客户端请求；转发动作为转发至监听配置的服务器组。
默认转发规则不支持删除，但支持更改转发动作的服务器组。
默认转发规则的优先级最低且不支持调整优先级。
如果您需要一条更灵活的兜底转发规则用于处理非预期请求，可配置一条转发条件中路径为/*（表示匹配所有路径）的转发规则，转发动作配置为返回固定响应，状态码设置为404或403，配置完成后将该转发规则拖拽至倒数第二位置即可。
转发条件间的逻辑关系：一条转发规则中可以配置多个转发条件，不同类型的转发条件之间为"与"（AND）关系，同一类型转发条件的多个值之间为"或"（OR）关系。
不同条件之间为"与"：例如一条规则同时配置了域名条件*.example.com和路径条件/api/*，则请求必须同时满足域名和路径两个条件才会匹配该规则。仅满足域名或仅满足路径均不会匹配。
同条件多值之间为"或"：例如域名条件添加了www.example.com和www.test.com两个值，则请求域名匹配其中任意一个即满足该域名条件。
以下示例说明多条转发规则的匹配过程：
| 优先级 | 转发条件 | 转发动作 | 说明 |
| --- | --- | --- | --- |
| 1 | 域名： api.example.com ，路径： /v2/* | 转发至服务器组 A | 精确域名 + 路径通配，优先级最高 |
| 2 | 域名： api.example.com ，路径： /* | 转发至服务器组 B | 精确域名 + 所有路径，优先级次之 |
| 3 | 域名： *.example.com | 转发至服务器组 C | 通配域名，优先级再次之 |
| 默认 | -（匹配所有请求） | 转发至服务器组 D | 兜底规则，优先级最低 |
请求api.example.com/v2/users匹配规则 1，转发至服务器组 A。
请求api.example.com/v1/users不匹配规则 1（路径不满足/v2/*），匹配规则 2，转发至服务器组 B。
请求web.example.com/index不匹配规则 1、2（域名不满足），匹配规则 3，转发至服务器组 C。
请求other.com/page不匹配任何规则，按默认规则转发至服务器组 D。
## 前提条件
已[创建](create-and-manage-alb-instances.md)[ALB](create-and-manage-alb-instances.md)[实例](create-and-manage-alb-instances.md)和[服务器组](create-and-manage-a-server-group.md)，并向服务器组中添加了后端服务器。
已为ALB实例[创建和管理监听](create-and-manage-listeners.md)并关联了已创建的服务器组。
## 添加转发规则
您已在创建监听时定义了默认转发规则。此外，您可以在创建监听后添加转发规则。
前往ALB控制台的[实例](https://slb.console.aliyun.com/alb/cn-hangzhou/albs)页面，单击目标实例ID。
单击监听页签，找到目标监听，在操作列单击查看/编辑转发规则。
在转发规则页签，选择请求方向转发规则或响应方向转发规则，单击插入新规则，配置以下参数后单击保存。
### 请求方向转发规则
规则名称
可选，不输入时系统自动生成。
转发条件
选择条件类型添加以下条件，您也可以单击添加转发条件添加多个。
域名：添加一个或多个域名。域名匹配规则长度限制为3~256个字符，支持星号（*）和半角问号（?）作为通配符使用（其中*可以代表任何字符串，?仅代表单个字符串），包括精准域名、通配符域名、正则表达式域名。域名配置规则详见[转发规则配置示例与域名路径匹配规则](forwarding-rule-configuration-example-and-domain-name-path-matching-rule.md)。
精准匹配：请求域名与配置域名完全一致，如www.example.com。
通配符匹配：使用*匹配任意长度字符串（包含.），?匹配单个字符，如*.example.com可匹配api.example.com、www.example.com等。
正则表达式匹配：使用正则表达式进行域名匹配，域名匹配不区分大小写。如^www\.example\.(com|cn)$可同时匹配.com和.cn结尾的域名。
路径：添加一条或多条路径。包括正则表达式类型的路径和非正则表达式类型的路径。路径配置规则详见[转发规则配置示例与域名路径匹配规则](forwarding-rule-configuration-example-and-domain-name-path-matching-rule.md)。
精准匹配：如/api/v1/users仅匹配完全一致的路径。
通配符匹配：如/api/*匹配所有以/api/开头的路径（包含多级子路径），/*匹配所有路径。路径匹配区分大小写。
正则表达式匹配：如^/api/(.*)/list$匹配以/api/开头且以/list结尾的路径，正则路径匹配时可选择区分或不区分大小写。
HTTP标头：在键是字段输入HTTP标头的名称，值是字段输入HTTP标头的内容，可添加多条标头内容。HTTP标头的键长度限制为1~40个字符，只允许包含大小写英文字母、数字、下划线（_）和中划线（-），匹配不区分大小写。标头的值长度限制为1~128个字符，支持可打印字符，开头和结尾不能为空格，支持星号（*）和半角问号（?）作为通配符。
示例：键user-agent，值*Mozilla/4.0*（表示匹配值中包含Mozilla/4.0的所有请求）。
查询字符串：添加一个或多个查询字符串的键值对。键的长度为1~100个字符，值的长度为1~128个字符，支持小写字母（输入仅支持小写字母，但实际匹配时不区分大小写）、通配符星号（*）和半角问号（?）等可见字符，不支持空格和#[]{}\|<>&等特殊字符。
示例：URL为www.example.com/test/test1?x=1&y=2时可配置为x：1或y：2。
HTTP 请求方法：添加一个或多个HTTP请求方法。包括：HEAD、GET、POST、OPTIONS、PUT、PATCH、DELETE。
Cookie：添加一个或多个Cookie。键的长度为1~100个字符，值长度为1~128个字符，支持小写字母（输入仅支持小写字母，但实际匹配时不区分大小写）、通配符星号（*）和半角问号（?）等可见字符，不支持空格和[]{}<>\#|&等特殊字符。
示例：键key，值value。
SourceIp：添加一个或多个IP地址或者IP地址段，不支持0.0.0.0/x类型的地址段，x为任意数字。
示例：192.168.1.1/32
转发动作
选择动作类型添加以下动作，您也可以单击添加动作添加多个。
转发至：在服务器组列表中选择目标服务器组。目前支持的服务器组类型包括服务器类型、IP类型和函数计算类型。您可以添加多个服务器组，通过设置各服务器组间的权重来控制流量分发比例，单个服务器组权重取值范围为0~100。添加多个服务器组时，还可以开启服务器组间会话保持（该功能需确保所有添加的服务器组开启了会话保持功能）。
在添加多个服务器组时，支持选择HTTP和HTTPS两种不同后端协议的服务器组。单个服务器组的权重上限支持提升至10000，如有需要请联系商务经理申请。
重定向至：在协议和状态码列表选择一个协议和一个状态码，以及分别输入跳转的目的域名、端口、路径和查询字符串。该转发动作中协议、域名、端口、路径、查询值不能全部为默认值或为空。
重定向至中关于路径的增强配置规则，请参见[重写和重定向中路径的增强配置规则](forwarding-rule-configuration-example-and-domain-name-path-matching-rule.md)。各字段的默认值（如${host}、${path}、${port}、${protocol}、${query}）表示引用请求中的相应值。路径字段仅支持引用${host}、${path}、${port}、${protocol}以及正则捕获组变量（如${1}、${2}、${3}等），不支持引用其他$变量。关于状态码的更多信息，请参见[HTTP](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/error-codes-and-status-codes#title-fxj-9jb-wk0)[协议常用标准状态码说明](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/error-codes-and-status-codes#title-fxj-9jb-wk0)。
返回固定响应：输入响应状态码，然后选择填写响应正文类型（可选）和响应正文（可选）。响应状态码必须是2xx、4xx、5xx的数字型字符串，x为任意数字。
重写：在ALB内部将请求的域名、路径或查询修改为指定值后再转发至后端服务器，客户端浏览器地址栏中的 URL 不会发生变化。
重写动作必须与转发至动作配合使用才能生效。重写与重定向至的区别：重写是ALB内部处理，改变后端接收到的路径，客户端 URL 不变；重定向返回 3xx 状态码，客户端浏览器跳转到新 URL。简单示例：将/app/page重写为/v2/page，可设置转发条件路径为/app/page（精准匹配），重写路径为/v2/page。如需匹配/app/下所有子路径并重写，请使用正则表达式方式，参见[重写和重定向中路径的增强配置规则](forwarding-rule-configuration-example-and-domain-name-path-matching-rule.md)。重写路径中，$仅允许用于引用以下变量：${host}、${path}、${port}、${protocol}以及正则捕获组变量（如${1}、${2}、${3}等），不支持引用其他变量。
写入Header：输入头字段名称和头字段内容，将覆盖请求中已有的头变量。其中标头键长度为1~40字符，支持大小写英文字母、数字、下划线（_）和中划线（-），标头的值长度限制为1~128个字符，支持英文字母、数字及常见标点符号，开头和结尾不能为空格。
删除Header：输入头字段名称，将删除请求Header中的该键值对内容。
请求方向写入Header和删除Header不允许将头字段名称设置为以下字段（不区分大小写）：slb-id、slb-ip、x-forwarded-for、x-forwarded-proto、x-forwarded-eip、x-forwarded-port、x-forwarded-client-srcport、x-forwarded-host、connection、upgrade、content-length、transfer-encoding、keep-alive、te、host、cookie、remoteip、authority。这些字段为ALB系统保留字段或HTTP协议关键字段，修改可能导致请求转发异常或连接中断。
限速：请根据需要配置以下参数。
QPS(总限速)：输入每秒请求数，取值范围：1~1000000。
QPS(基于客户端源IP限速)：输入基于客户端源IP限速，取值范围：1~1000000。同时配置QPS(总限速)和QPS(基于客户端源IP限速)时，基于客户端源IP限速值要小于总限速值。
限速动作必须与转发至动作配合使用。限速值以内的请求转发至目标服务器组；超出限速值时，默认返回503状态码，也可附加重定向至或返回固定响应动作处理超出限速值的请求。开启QPS(基于客户端源IP限速)后，ALB从X-Forwarded-For头字段中获取源IP。如果请求经过多层代理，需要在监听中打开查找真实客户端源IP开关，确保获取到正确的客户端源IP。更多信息，请参见[创建和管理监听](create-and-manage-listeners.md)。
流量镜像至：在服务器组列表中选择目标服务器组。支持选择服务器类型和IP类型的后端服务器组。
跨域：配置CORS跨域访问策略，ALB自动处理OPTIONS预检请求并返回CORS响应头，无需后端服务器处理。相比通过写入Header动作手动设置Access-Control-Allow-Origin等响应头，跨域动作配置更简单。
什么是跨域
客户端发送的请求URL的协议、域名或者端口三者之间任意一个与当前返回的页面URL不同即为跨域。请求包括简单请求和预检请求。跨域动作适用于前后端分离架构等场景，例如前端部署在www.example.com，API服务部署在api.example.com，前端通过浏览器调用API时会触发跨域限制。
允许的访问来源：设置允许通过浏览器访问服务资源的站点。
允许的方法：选择跨域访问时允许的HTTP方法。包括：GET，POST、PUT、DELETE、HEAD、OPTIONS、PATCH。
允许的请求头部：除了浏览器内置的基础Header，设置跨域访问时允许的Header。
允许的响应头部：允许浏览器、JavaScript脚本访问的响应头部。
允许的携带凭证：跨域访问时是否允许携带凭证信息，默认允许。
浏览器缓存时间：对于预检请求，设置OPTIONS预检请求在浏览器的最大缓存时间。单位：秒。取值范围：-1~172800。
### 响应方向转发规则
规则名称
可选，不输入时系统自动生成。
如果满足以下请求方向条件（选填）：
选择请求方向的转发条件，也可以单击添加请求方向转发条件添加多个。各条件的配置说明请参见请求方向转发规则标签页。
如果请求方向转发规则中配置了重写动作，则响应方向转发规则中附加的请求方向条件（域名、路径、查询字符串）需要匹配重写后的值，而非客户端原始请求中的值。例如请求方向将路径从/app/page重写为/v2/page，则响应方向的路径条件应配置为/v2/page。
且满足以下响应方向条件
选择响应方向的转发条件，您也可以单击添加响应方向转发条件添加多个。
响应中的状态码：返回给客户端响应中的状态码，取值100~599。支持输入范围，多个状态码用半角逗号（,）分隔，例如：200-233,301。
响应中的标头：响应中的HTTP标头。在键是字段输入HTTP标头的名称，值是字段输入HTTP标头的内容，可添加多条标头内容。
转发动作
选择响应方向的动作类型，您也可以单击添加动作添加多个。
返回固定响应：输入响应状态码，然后选择填写响应正文类型（可选）和响应正文（可选）。响应状态码必须是2xx、4xx、5xx的数字型字符串，x为任意数字。
写入Header：输入响应方向头字段名称和头字段内容，将覆盖响应报文中已有的头变量。
删除Header：输入响应方向头字段名称，将删除响应报文中对应的键值对内容。
响应方向写入Header和删除Header不允许将头字段名称设置为以下字段（不区分大小写）：connection、upgrade、content-length、transfer-encoding。这些字段为HTTP协议关键字段，修改可能导致响应传输异常。
### 添加AScript可编程脚本
您可以单击在规则执行前添加可编程脚本或在规则执行后添加可编程脚本来[添加](add-and-manage-scripts.md)[AScript](add-and-manage-scripts.md)[可编程脚本转发规则](add-and-manage-scripts.md)。仅标准版和WAF增强版的ALB实例支持AScript，基础版不支持。
## API
调用[CreateRule](../developer-reference/api-alb-2020-06-16-createrule.md)创建转发规则。
调用[CreateRules](../developer-reference/api-alb-2020-06-16-createrules.md)批量创建转发规则。
## 编辑/删除转发规则与调整优先级
警告
编辑、删除转发规则或调整转发规则优先级可能影响现有业务流量的转发路径。建议在业务低峰期进行操作，并确保已对所需更改进行充分评估和测试。
### 控制台
前往ALB控制台的[实例](https://slb.console.aliyun.com/alb/cn-hangzhou/albs)页面，单击目标实例ID。
单击监听页签，找到目标监听，在操作列单击查看/编辑转发规则。
在转发规则页签，选择请求方向转发规则或响应方向转发规则，按需执行以下操作：
编辑转发规则：找到要编辑的规则，单击右上角编辑，修改完成后单击保存。
删除转发规则：找到要删除的规则，单击删除，在弹出的对话框中单击确定删除。默认转发规则不支持删除。删除监听时会同时删除其所有转发规则。
调整转发规则优先级：将目标转发规则拖拽至目标位置，然后单击保存优先级。请求按优先级数字从小到大依次匹配转发规则。默认规则的优先级不可调整。
### API
调用[ListRules](../developer-reference/api-alb-2020-06-16-listrules.md)查询转发规则。
调用[UpdateRuleAttribute](../developer-reference/api-alb-2020-06-16-updateruleattribute.md)更新转发规则属性。
调用[UpdateRulesAttribute](../developer-reference/api-alb-2020-06-16-updaterulesattribute.md)批量更新转发规则属性。
调用[DeleteRule](../developer-reference/api-alb-2020-06-16-deleterule.md)删除转发规则。
调用[DeleteRules](../developer-reference/api-alb-2020-06-16-deleterules.md)批量删除转发规则。
## 计费
转发规则本身不收费，转发规则数量会影响ALB实例LCU费用中的规则评估数指标，详见[ALB](../product-overview/alb-billing-rules.md)[计费规则](../product-overview/alb-billing-rules.md)。
## 配额
### 可申请提升的配额
一个ALB实例可添加的转发规则数（不计入默认规则）配额如下：
| 配额名称 | 描述 | 默认值 | 最大支持提升至 | 是否支持申请 |
| --- | --- | --- | --- | --- |
| alb_quota_loadbalancer_rules_num_basic_edition | 一个基础版 ALB 实例可添加的转发规则数（不计入默认规则） | 40 个 | 100 个 | [是](https://quotas.console.aliyun.com/products/alb/quotas?query=alb_quota_loadbalancer_rules_num_basic_edition) |
| alb_quota_loadbalancer_rules_num_standard_edition | 一个标准版 ALB 实例可添加的转发规则数（不计入默认规则） | 100 个 | 200 个 | [是](https://quotas.console.aliyun.com/products/alb/quotas?query=alb_quota_loadbalancer_rules_num_standard_edition) |
| alb_quota_loadbalancer_rules_num_standardwithwaf_edition | 一个 WAF 增强版 ALB 实例可添加的转发规则数（不计入默认规则） | 100 个 | 200 个 | [是](https://quotas.console.aliyun.com/products/alb/quotas?query=alb_quota_loadbalancer_rules_num_standardwithwaf_edition) |
当转发规则数接近或达到上限时，您可以：
在配额中心申请提升转发规则数配额。
合并条件相似的转发规则，利用同一条件多值的"或"关系减少规则数量。
基础版实例可[升级](modify-the-configurations-of-alb-instances.md)至标准版或WAF增强版以获得更高的配额上限。
### 硬限制（不可提升）
单条转发规则可添加的条目数限制如下，此类配额不可提升。
| 资源 | 功能版本 | 默认限制 |
| --- | --- | --- |
| 一条转发规则可添加的动作条目数 | 基础版 | 3 个 |
| 标准版/WAF 增强版 | 5 个 |  |
| 一条转发规则可添加的匹配条件条目数 | 基础版 | 5 个 |
| 标准版/WAF 增强版 | 10 个 |  |
| 一条转发规则可添加的包含通配符的条目数 | 基础版 | 5 个 |
| 标准版/WAF 增强版 | 10 个 |  |
## 相关文档
[转发规则配置示例与域名路径匹配规则](forwarding-rule-configuration-example-and-domain-name-path-matching-rule.md)：自定义域名和路径的匹配与转发规则。
[使用](../use-cases/redirect-http-requests-to-an-https-listener.md)[ALB](../use-cases/redirect-http-requests-to-an-https-listener.md)[将](../use-cases/redirect-http-requests-to-an-https-listener.md)[HTTP](../use-cases/redirect-http-requests-to-an-https-listener.md)[访问重定向至](../use-cases/redirect-http-requests-to-an-https-listener.md)[HTTPS](../use-cases/redirect-http-requests-to-an-https-listener.md)：通过监听转发规则将HTTP请求重定向到HTTPS，确保数据传输加密。
[使用](../use-cases/use-the-traffic-mirroring-feature-to-mirror-production-traffic-to-a-staging-environment.md)[ALB](../use-cases/use-the-traffic-mirroring-feature-to-mirror-production-traffic-to-a-staging-environment.md)[流量镜像功能实现仿真压测](../use-cases/use-the-traffic-mirroring-feature-to-mirror-production-traffic-to-a-staging-environment.md)：将在线流量镜像到测试环境，验证测试业务而不影响线上业务。
[使用](../use-cases/use-alb-to-implement-canary-releases.md)[ALB](../use-cases/use-alb-to-implement-canary-releases.md)[实现灰度发布](../use-cases/use-alb-to-implement-canary-releases.md)：通过条件或权重转发规则，将部分请求转发至新版本应用，逐步验证稳定性。
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
