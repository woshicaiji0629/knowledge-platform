## 操作步骤
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，找到目标域名，单击操作列的管理。
在指定域名的左侧导航栏，单击回源配置。
在高级回源区域，单击添加。
在高级回源对话框中，选择使用条件并填写源站域名。
说明
任意选择Request Header、Query String Parameter、Path、Request Cookie配置不同源站。CDN节点在接收到客户端请求后将读取请求中对应的字段进行判断并回源到不同源站。
使用条件需配置字段名、匹配方式（如等于）及对应值。源站域名格式示例：img.yourdomain.com，源站域名不能与加速域名相同。
单击确定。
