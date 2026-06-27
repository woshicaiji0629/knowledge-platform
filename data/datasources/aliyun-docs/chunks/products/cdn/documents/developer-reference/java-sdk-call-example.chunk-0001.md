## 步骤二：创建RAM用户并完成授权
重要
阿里云账号拥有所有API的访问权限，建议您创建并使用RAM用户进行API访问或日常运维。
如您已创建RAM用户且已完成授权，可跳过此步骤。
使用阿里云账号登录[RAM](https://ram.console.aliyun.com)[控制台](https://ram.console.aliyun.com)。
创建RAM用户。
在左侧导航栏，选择身份管理>用户。
在用户页面，单击创建用户。
在创建用户页面，设置登录名称和显示名称，设置访问方式为控制台访问和使用永久 AccessKey 访问，单击确定。
重要
RAM用户的AccessKey Secret只在创建时显示，不支持查看，请下载CSV文件后妥善保管。
创建RAM用户成功后，请记录用户登录名称和密码。在调用OpenAPI时，需要使用该RAM用户登录阿里云OpenAPI开发者门户，并使用该RAM用户的AccessKey进行代码调试。
为RAM用户授权。
说明
创建RAM用户后，该RAM用户无任何操作CDN的权限。您需要为该RAM用户授予系统策略（AliyunCDNFullAccess、AliyunCDNReadOnlyAccess）或自定义策略。本案例以授予RAM用户AliyunCDNReadOnlyAccess策略为例，AliyunCDNReadOnlyAccess策略具备CDN资源的只读权限。
在用户页面，单击目标RAM用户对应的添加权限。
在新增授权面板，在系统策略中搜索选中AliyunCDNReadOnlyAccess，然后单击确认新增授权。
确认授权结果，单击关闭。
