## 常见问题
如何证明数据落盘已加密？
重要
该方法通过禁用密钥进行加密验证，会导致系统盘出现读写异常，建议[购买测试实例](create-an-instance-by-using-the-wizard.md)进行测试。
购买测试实例时，创建使用主密钥加密的系统盘。
禁用主密钥。
登录[密钥管理服务控制台](https://yundun.console.aliyun.com/?p=kms#/keyList/base)，在顶部菜单栏选择地域后，在左侧导航栏单击资源>密钥管理。
在用户主密钥或默认密钥页签，定位目标密钥，单击操作列的禁用。
在禁用密钥对话框，确认无误后，单击确定。
重要
在禁用KMS主密钥时，请自行排查该密钥是否存在关联使用的云资源，避免禁用密钥后对使用该密钥的服务产生影响。
验证是否加密。
连接ECS实例后，执行sudo reboot，重启操作系统，由于加密系统盘关联的KMS加密密钥已被禁用，系统无法解密数据，会出现IO hang。此时[通过](log-on-to-an-instance-by-using-vnc.md)[VNC](log-on-to-an-instance-by-using-vnc.md)[连接](log-on-to-an-instance-by-using-vnc.md)[ECS](log-on-to-an-instance-by-using-vnc.md)[实例](log-on-to-an-instance-by-using-vnc.md)，显示为黑屏，证明数据已被加密。
启用KMS主密钥并[释放测试实例](release-an-instance.md)。
