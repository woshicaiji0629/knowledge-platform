CORS相关响应头：
在[CDN](https://cdnnext.console.aliyun.com/domain/list)[控制台](https://cdnnext.console.aliyun.com/domain/list)单击加速域名或操作列的管理。
在缓存配置>修改出站响应头中配置响应头参数和响应头值。

| 自定义响应头参数 | 响应头值 | 跨域验证 |
| --- | --- | --- |
| Access-Control-Allow-Origin | * | 开启 |
| Access-Control-Allow-Methods | POST,GET, HEAD, PUT, DELETE | 不涉及 |
| Access-Control-Max-Age | 3600 | 不涉及 |
