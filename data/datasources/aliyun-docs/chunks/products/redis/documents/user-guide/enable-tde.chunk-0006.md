## 操作步骤
访问[实例列表](https://kvstore.console.aliyun.com/Redis/instance/cn-hangzhou)，在上方选择地域，然后单击目标实例ID。
在左侧导航栏，单击TDE设置。
打开TDE状态右侧的开关。
说明
如果小版本过低，该开关将处于不可单击状态，查看及升级小版本的方法，请参见[升级小版本与代理版本](update-the-minor-version.md)。
在弹出的对话框中，选择使用自动生成密钥或使用自定义密钥，然后单击确定。
说明
首次开启TDE时，需要您授权AliyunRdsInstanceEncryptionDefaultRole角色。
自定义密钥的创建方法，请参见[密钥管理服务](../../../kms/documents/key-management-service/support/what-is-key-management-service.md)[KMS](../../../kms/documents/key-management-service/support/what-is-key-management-service.md)。
设置完成后，实例状态改为TDE更变中，当实例状态转变为运行中表示操作完成。
