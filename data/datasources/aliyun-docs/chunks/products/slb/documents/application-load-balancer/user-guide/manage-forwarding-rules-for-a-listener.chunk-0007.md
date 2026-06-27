其他$变量。关于状态码的更多信息，请参见[HTTP](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/error-codes-and-status-codes#title-fxj-9jb-wk0)[协议常用标准状态码说明](https://help.aliyun.com/zh/cms/cloudmonitor-1-0/user-guide/error-codes-and-status-codes#title-fxj-9jb-wk0)。
返回固定响应：输入响应状态码，然后选择填写响应正文类型（可选）和响应正文（可选）。响应状态码必须是2xx、4xx、5xx的数字型字符串，x为任意数字。
重写：在ALB内部将请求的域名、路径或查询修改为指定值后再转发至后端服务器，客户端浏览器地址栏中的 URL 不会发生变化。
重写动作必须与转发至动作配合使用才能生效。重写与重定向至的区别：重写是ALB内部处理，改变后端接收到的路径，客户端 URL 不变；重定向返回 3xx 状态码，客户端浏览器跳转到新 URL。简单示例：将/app/page重写为/v2/page，可设置转发条件路径为/app/page（精准匹配），重写路径为/v2/page。如需匹配/app/下所有子路径并重写，请使用正则表达式方式，参见[重写和重定向中路径的增强配置规则](forwarding-rule-configuration-example-and-domain-name-path-matching-rule.md)。重写路径中，$仅允许用于引用以下变量：${host}、${path}、${port}、${protocol}以及正则捕获组变量（如${1}、${2}、${3}等），不支持引用其他变量。
写入Header：输入头字段名称和头字段内容，将覆盖请求中已有的头变量。其中标头键长度为1~40字符，支持大小写英文字母、数字、下划线（_）和中划线（-），标头的值长度限制为1~128个字符，支持英文字母、数字及常见标点符号，开头和结尾不能为空格。
删除Header：输入头字段名称，将删除请求Header中的该键值对内容。
请求方向写入Header和删除Header不允许将头字段名称设置为以下字段（不区分大小写）：slb-id、slb-ip、x-forwarded-for、x-forwarded-proto、x-forwarded-eip、x-forwarded-port、x-forwarded-client-srcport、x-forwarded-host、connection、upgrade、content-length、transfer-encoding、keep-alive、te、host、cookie、remoteip、auth
