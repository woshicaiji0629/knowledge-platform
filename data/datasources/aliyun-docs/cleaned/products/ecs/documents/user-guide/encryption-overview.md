# 通过加密云盘保护存储在云盘中的数据安全-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/encryption-overview

# 加密云盘
为满足数据合规性要求，并应对物理盗窃、未授权访问等安全威胁，可利用密钥管理服务 (KMS) 对ECS云盘加密，保障数据机密性与完整性。
## 云盘加解密工作原理
加密云盘通过两层密钥保障数据安全：
数据密钥：用于加密和解密云盘数据。
KMS密钥：由KMS服务保管，用于加密和解密数据密钥。
创建加密云盘时，由KMS密钥加密的数据密钥会被存储在云盘中。实例启动阶段，云服务器ECS会向KMS服务请求解密数据密钥，解密后的数据密钥明文将被加载到内存中，用于加解密数据。
## 创建加密云盘
创建加密云盘。
重要
加密操作不可逆，云盘一旦被加密，无法再转为非加密状态。
控制台
创建云盘分为以下场景。
云盘通过非共享而来的加密快照创建：默认使用该快照所使用的加密密钥进行加密，可下拉列表更换KMS密钥。
云盘通过共享而来的加密快照创建：默认使用服务密钥进行加密，可下拉列表更换KMS密钥。
在已开启块存储账号级默认加密的地域创建：默认使用指定的账号级密钥进行加密，可下拉列表更换KMS密钥。
其他情况：可在设置中勾选加密后，下拉列表选择KMS密钥。默认使用服务密钥进行加密。
KMS密钥分为以下两种类型。
服务密钥：由云产品为 ECS 服务自动创建和管理的密钥，别名为alias/acs/ecs。满足基本的数据加密需求，操作简便，无需管理密钥生命周期。
主密钥：在 KMS 中自行导入/创建的拥有完全控制权的密钥。适用于对数据安全有更高要求，需要自行管理密钥的轮转、禁用、删除等生命周期。
首次选择主密钥加密时，需要依照界面提示为ECS授权AliyunECSDiskEncryptDefaultRole角色，以允许访问KMS资源。
API
创建ECS实例时加密系统盘及数据盘。
调用API接口[RunInstances](../developer-reference/api-ecs-2014-05-26-runinstances.md)创建ECS实例时，通过设置系统盘或数据盘的Encrypted值和KMSKeyId值实现加密。
单独创建加密数据盘。
调用API接口[CreateDisk](../developer-reference/api-ecs-2014-05-26-createdisk.md)创建数据盘时，通过设置Encrypted值和KMSKeyId值实现加密。
后续步骤。
系统盘：创建后即可使用，无需额外操作。
数据盘：
随实例创建：
Windows：创建后即可使用，无需额外操作。
Linux：需要完成[初始化](initialize-a-data-disk.md)后才可使用。
单独创建：需要将其[挂载至](attach-a-data-disk.md)[ECS](attach-a-data-disk.md)[实例](attach-a-data-disk.md)并完成[初始化](initialize-a-data-disk.md)后才可使用。
## 将非加密云盘转换为加密云盘
已有的非加密云盘无法直接加密，需要利用加密自定义镜像或加密快照，通过更换操作系统或新建云盘间接实现。
系统盘
[为目标实例创建自定义镜像](create-a-custom-image-from-an-instance.md)。
[复制自定义镜像](copy-an-image.md)时选择加密复制，将非加密镜像复制为加密镜像。
选择任一方式，间接实现加密系统盘。
使用加密镜像[更换原](replace-the-operating-system-of-an-instance-1.md)[ECS](replace-the-operating-system-of-an-instance-1.md)[实例的操作系统](replace-the-operating-system-of-an-instance-1.md)。
[使用加密镜像创建新实例](create-an-ecs-instance-by-using-a-custom-image.md)。
数据盘
为数据盘[手动创建单个快照](create-a-snapshot.md)。
将快照[复制为加密快照](copy-a-snapshot.md)。
[使用加密快照创建数据盘](create-a-disk-from-a-snapshot.md)。
将创建的加密云盘[挂载](attach-a-data-disk.md)至原ECS实例。
## 应用于生产环境
禁止随意删除或禁用密钥。
一旦删除或禁用密钥，所有依赖该密钥的加密资源（如云盘、快照、镜像）将无法解密，可能导致数据不可恢复。请在操作前进行[密钥关联检测](../../../kms/documents/key-management-service/user-guide/manage-keys-2.md)。
重要
因用户主动操作导致密钥失效而引起的数据不可恢复损失，由用户自行承担。
限制RAM用户仅能创建加密云盘。
为满足特定的安全合规要求，防止因云盘未加密而导致数据泄露，可为账号下的所有RAM用户配置自定义权限策略，[限制其只能创建加密云盘](custom-policies-for-ecs.md)，保护数据的机密性。
禁止RAM用户管理密钥。
为防止密钥被误删除或禁用，可仅授予RAM用户只读访问密钥管理服务（KMS）的权限：AliyunKMSReadOnlyAccess。
批量加密已有系统盘
可使用OOS公共模板[ACS-ECS-BulkyEncryptSystemDisk](https://oos.console.aliyun.com/cn-hangzhou/template/public/detail/ACS-ECS-BulkyEncryptSystemDisk)，通过更换操作系统方式，[加密多台](https://help.aliyun.com/zh/oos/use-cases/automatically-encrypt-the-system-disk-through-oos)[ECS](https://help.aliyun.com/zh/oos/use-cases/automatically-encrypt-the-system-disk-through-oos)[实例的系统盘](https://help.aliyun.com/zh/oos/use-cases/automatically-encrypt-the-system-disk-through-oos)。
## 费用说明
云盘费用：加密云盘与非加密云盘的计费规则相同，加密功能本身不收取额外费用。详细内容，可参考[块存储计费](../block-storage-devices.md)。
密钥费用：使用密钥过程中不会产生密钥费用。
## 配额与限制
实例规格
加密系统盘或通过快照创建加密数据盘时，不支持挂载至ecs.ebmg5、ecs.ebmgn5t、ecs.ebmi3、ecs.sccg5、ecs.scch5、ecs.ebmc4和ecs.ebmhfg5。
云盘类型
加密系统盘或通过快照创建加密数据盘时，仅支持加密ESSD系列云盘（ESSD云盘、ESSD Entry云盘、ESSD AutoPL云盘和ESSD同城冗余云盘）。
地域
不支持创建加密云盘的地域：华东5（南京-本地地域-关停中）、韩国（首尔）。
不支持使用主密钥的地域：华东6（福州-本地地域-关停中）、泰国（曼谷）。
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
## 相关文档
关于KMS密钥的详细介绍，可参考[支持云产品加密的密钥类型](../../../kms/documents/key-management-service/user-guide/integration-with-kms.md)。
加密的详细原理，请参见[云产品集成](../../../kms/documents/key-management-service/user-guide/integration-with-kms.md)[KMS](../../../kms/documents/key-management-service/user-guide/integration-with-kms.md)[加密概述](../../../kms/documents/key-management-service/user-guide/integration-with-kms.md)。
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
