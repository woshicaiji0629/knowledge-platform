## 常见问题
CDN访问OSS资源提示This request is forbidden by kms.错误如何解决？
如果您的OSS Bucket中使用了密钥管理服务KMS（Key Management Service）进行加密，您需要为CDN的回源角色额外授予使用KMS密钥的权限，否则CDN将无法解密和访问这些文件，出现This request is forbidden by kms.报错。
登录[RAM](https://ram.console.aliyun.com/)[控制台](https://ram.console.aliyun.com/)。
在左侧导航栏，选择
在角色名称列表下，找到AliyunCDNAccessingPrivateOSSRole角色。
单击新增授权，授权主体会自动填入。
在权限策略下选择系统策略，搜索AliyunKMSCryptoUserAccess，并单击AliyunKMSCryptoUserAccess，将其添加到已选择权限策略区域框中。
单击确认新增授权，显示已完成。
单击关闭。
使用[刷新和预热资源](refresh-and-prefetch-resources.md)功能，待刷新任务完成后，重新访问资源。
