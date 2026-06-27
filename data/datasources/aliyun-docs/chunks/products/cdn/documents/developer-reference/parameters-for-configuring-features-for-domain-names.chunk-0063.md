也属于已存在配置），则必须删除已经添加的功能配置（您可以通过调用[DeleteSpecificConfig](api-cdn-2018-05-10-deletespecificconfig.md)接口来删除域名的指定配置），然后才能给另一个功能添加配置。
功能ID（FunctionID/FuncId）：1。
参数说明：

| 参数 | 类型 | 是否必选 | 描述 | 示例值 |
| --- | --- | --- | --- | --- |
| refer_domain_allow_list | String | 是 | 白名单列表，多个用半角逗号（,）分隔。 | example.aliyundoc.com,demo.aliyundoc.com |
| allow_empty | String | 否 | 是否允许空 referer 字段访问 CDN 资源。取值： on：允许。 off（默认值）：禁止。 | off |
| redirect_url | String | 否 | 重定向 URL，即用户请求中的 referer 信息未匹配上白名单列表，被拦截后不会再返回 403，而是会返回 302 加 Location 头，该项为 Location 头的值，以 http:// 或者 https:// 开头。 | http://www.example.com |
| disable_ast | String | 否 | 使用精确匹配模式，控制“白名单列表”项中填写的域名是否为精确匹配。如果勾选（on）则精确匹配域名。 取值为 on 时： 支持精确匹配 白名单列表填写 example.com ，匹配 example.com 。 白名单列表填写 a*b.example.com ，匹配 a<任意字符>b.example.com 。 不支持后缀匹配 取值为 off（默认值）时： 不支持精确匹配 支持后缀匹配 白名单列表填写 example.com ，匹配 example.com 和 <任意字符>.example.com 。 白名单列表填写 a*b.example.com ，匹配 a<任意字符>b.example.com 和 <任意字符>.a<任意字符>b.example.com 。 | off |
| ignore_scheme | String | 否 | 开启忽略 scheme。开启后，如果用户请求中的 referer 没有带上 HTTP 或 HTTPS 协议头部，则依然视为有效 referer 进行处理。示例： 取值为 on 时，referer 格式如下： referer: www.example.com 取值为 off（默认值）时，referer 格式如下： referer: https://www.example.com | off |
