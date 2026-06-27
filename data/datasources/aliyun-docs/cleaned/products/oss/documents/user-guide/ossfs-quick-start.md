# 使用ossfs将OSS的Bucket挂载到Linux系统中-对象存储(OSS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/oss/user-guide/ossfs-quick-start?spm=a2c4g.11186623.help-menu-31815.d_1_4.50dd7166B93Yte

# 使用ossfs将OSS的Bucket挂载到Linux系统中
ossfs是一款能够将对象存储OSS中的Bucket挂载到本地Linux系统的工具。您的应用程序可以通过文件系统操作（例如open和read）访问存储在OSS中的对象。ossfs会自动将这些操作转换为OSS的API调用。
说明
ossfs分为1.0和2.0两个版本。2.0版本是面向新形态计算密集型应用进行了全面重构的版本，实现了性能的全面升级，但对POSIX语义进行了部分限制，是未来的主线演进版本。如果您正在开展AI训练、推理、自动驾驶仿真等新型应用，且不方便使用OSS SDK和[使用](../developer-reference/oss-connector-overview.md)[OSS Connector for AI/ML](../developer-reference/oss-connector-overview.md)[加速模型训练](../developer-reference/oss-connector-overview.md)，强烈建议使用[ossfs 2.0](../developer-reference/ossfs-2-0.md)。相较之下，[ossfs 1.0](../developer-reference/ossfs-overview.md)对POSIX语义支持更为全面，适合对性能无特殊需求的场景日常使用。
## 前提条件
已[注册阿里云账号](https://account.aliyun.com/register/qr_register.htm?oauth_callback=https%3A%2F%2Fbailian.console.aliyun.com%2F%3FapiKey%3D1)。
已[个人实名认证](https://help.aliyun.com/zh/document_detail/324614.html#task-2020003)或[企业实名认证](https://help.aliyun.com/zh/account/overview)。
已[开通](https://oss.console.aliyun.com/overview)[OSS](https://oss.console.aliyun.com/overview)[服务](https://oss.console.aliyun.com/overview)并[创建](create-a-bucket-4.md)[OSS Bucket](create-a-bucket-4.md)。
## 运行环境
ossfs 2.0基于FUSE（用户态文件系统，Filesystem in Userspace）开发。
| 系统架构 | 操作系统 | 系统版本 |
| --- | --- | --- |
| x86_64 | CentOS | CentOS 7、CentOS 8 |
| Rocky Linux | Rocky Linux 9.0 及以上版本 |  |
| Alibaba Cloud Linux | Alibaba Cloud Linux 2 及以上版本 |  |
| Ubuntu | Ubuntu 20.04 LTS 及后续 LTS 版本 |  |
| Debian | Debian 11 及以上版本 |  |
| aarch64 | Alibaba Cloud Linux | Alibaba Cloud Linux 3 |
## 安装ossfs 2.0
### Alibaba Cloud Linux
根据平台的系统架构执行相应命令，下载安装包。
x86_64架构：sudo wget https://gosspublic.alicdn.com/ossfs/ossfs2_2.0.7_linux_x86_64.rpm
aarch64架构：sudo wget https://gosspublic.alicdn.com/ossfs/ossfs2_2.0.7_linux_aarch64.rpm
根据平台的系统架构执行相应命令，安装ossfs 2.0。
x86_64架构：sudo yum install ossfs2_2.0.7_linux_x86_64.rpm -y
aarch64架构：sudo yum install ossfs2_2.0.7_linux_aarch64.rpm -y
执行以下命令，验证ossfs 2.0是否成功安装。
ossfs2 --version
说明
ossfs2的可执行文件安装在/usr/local/bin/ossfs2路径下，若您的环境变量PATH有特殊配置，可直接通过/usr/local/bin/ossfs2路径访问该程序。
### CentOS/Rocky Linux
执行以下命令，下载安装包。
sudo wget https://gosspublic.alicdn.com/ossfs/ossfs2_2.0.7_linux_x86_64.rpm
执行以下命令，安装ossfs 2.0。
sudo yum install ossfs2_2.0.7_linux_x86_64.rpm -y
执行以下命令，验证ossfs 2.0是否成功安装。
ossfs2 --version
说明
ossfs2的可执行文件安装在/usr/local/bin/ossfs2路径下，若您的环境变量PATH有特殊配置，可直接通过/usr/local/bin/ossfs2路径访问该程序。
### Ubuntu/Debian
执行以下命令，下载安装包。
sudo wget https://gosspublic.alicdn.com/ossfs/ossfs2_2.0.7_linux_x86_64.deb
执行以下命令，安装ossfs 2.0。
sudo dpkg -i ossfs2_2.0.7_linux_x86_64.deb
执行以下命令，验证ossfs 2.0是否成功安装。
ossfs2 --version
说明
ossfs2的可执行文件安装在/usr/local/bin/ossfs2路径下，若您的环境变量PATH有特殊配置，可直接通过/usr/local/bin/ossfs2路径访问该程序。
## 配置ossfs 2.0
在实际使用过程中，为满足不同场景下对存储空间（OSS Bucket）的挂载需求，需对ossfs 2.0配置文件进行针对性配置，然后在挂载存储空间（OSS Bucket）时，引用该配置文件即可完成挂载。
[创建拥有](../../../ram/documents/create-an-accesskey-pair-1.md)[OSS](../../../ram/documents/create-an-accesskey-pair-1.md)[管理权限的](../../../ram/documents/create-an-accesskey-pair-1.md)[RAM](../../../ram/documents/create-an-accesskey-pair-1.md)[用户](../../../ram/documents/create-an-accesskey-pair-1.md)[AccessKey](../../../ram/documents/create-an-accesskey-pair-1.md)。
通过ROS脚本快速创建具备OSS管理权限的RAM用户及其AccessKey
在资源编排ROS控制台的[创建资源栈](https://ros.console.aliyun.com/cn-hangzhou/stacks/create?templateUrl=https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20241114/itgrlo/createossadmin.yaml&step=1&hideTemplateSelector=false)页面的安全确认下，勾选确认，然后单击创建。
创建完成后，在输出中复制新创建的AccessKey。
输出关键字包括AccessKeyId和AccessKeySecret，分别复制对应的值。
配置用于访问对象存储OSS的凭证环境变量。
export OSS_ACCESS_KEY_ID=LTAI****************** export OSS_ACCESS_KEY_SECRET=8CE4**********************
您可按需自由设定ossfs 2.0配置文件的文件名与路径。例如，创建/etc/ossfs2.conf文件作为配置文件。
sudo touch /etc/ossfs2.conf
填写挂载信息。以只读方式挂载整个Bucket的配置为例。
说明
查看Bucket的Endpoint请进入[Bucket](https://oss.console.aliyun.com/bucket)[列表](https://oss.console.aliyun.com/bucket)页面，选择目标Bucket并进入，接着单击左侧导航栏的概览选项，在概览页的访问端口栏中即可查看目标Bucket所处的地域节点。以杭州地域Bucket为例。
杭州地域 Bucket 的 Endpoint 信息：外网访问对应oss-cn-hangzhou.aliyuncs.com，ECS 经典网络及 VPC 内网访问对应oss-cn-hangzhou-internal.aliyuncs.com，传输加速域名（全地域上传下载加速）对应oss-accelerate.aliyuncs.com，OSS 加速器对应cn-hangzhou-internal.oss-data-acc.aliyuncs.com，所有端口均支持 HTTPS。
打开已创建的ossfs 2.0配置文件，参照以下示例（以杭州地域内网Endpoint为例）配置并保存。内网和OSS加速器Endpoint仅支持同地域VPC内实例挂载，数据传输更快速、稳定；不建议使用外网Endpoint访问ossfs，受高延迟和不稳定的Internet网络连接影响，可能会出现各种卡顿问题。
# Bucket所处Endpoint（地域节点） --oss_endpoint=https://oss-cn-hangzhou-internal.aliyuncs.com # Bucket名称 --oss_bucket=bucketName # 以只读方式挂载 --ro=true
## 挂载访问
创建挂载目录。
您可按需自由设定挂载目录的文件名与路径。例如，创建/tmp/ossfs2-bucket目录作为挂载目录。
sudo mkdir /tmp/ossfs2-bucket
执行命令挂载。
执行命令将ossfs 2.0配置文件ossfs2.conf中所配置的Bucket只读挂载至本地/tmp/ossfs2-bucket/目录下。如果您需要采用读写挂载，请删除ossfs2.conf配置文件中的--ro=true选项。
sudo ossfs2 mount /tmp/ossfs2-bucket/ -c /etc/ossfs2.conf
操作已挂载的Bucket。
挂载完成后您就可以像访问本地文件系统一样操作Bucket中的对象。例如执行sudo ls -lh /tmp/ossfs2-bucket/命令，查看已挂载Bucket的文件列表。
[root@iZbp1hxeiqyf3kjqoxgrgqZ ossfs2-bucket]# sudo ls -lh /tmp/ossfs2-bucket/ total 36G drwxrwxrwx 1 root root 0 Mar 20 13:27 100G drwxrwxrwx 1 root root 0 Mar 20 13:27 100G -rwxrwxrwx 1 root root 36G Feb 21 10:48 xxx.bin drwxrwxrwx 1 root root 0 Mar 20 10:48 checkpoints -rwxrwxrwx 1 root root 0 Feb 10 18:25 filename.txt -rwxrwxrwx 1 root root 23K Mar 7 13:26 xxx.txt -rwxrwxrwx 1 root root 191 Feb 25 15:10 xxx.txt drwxrwxrwx 1 root root 0 Mar 20 10:48 img -rwxrwxrwx 1 root root 575 Mar 6 16:52 xxx.txt -rwxrwxrwx 1 root root 269 Jan 23 14:48 xxx.txt -rwxrwxrwx 1 root root 2.2M Feb 10 13:20 xxx.txt -rwxrwxrwx 1 root root 11 Jan 23 14:08 xxxon.txt -rwxrwxrwx 1 root root 2.1K Jan 24 14:16 xxx.txt -rwxrwxrwx 1 root root 2.1K Jan 24 14:17 xxx.txt -rwxrwxrwx 1 root root 4.8K Feb 10 13:36 xxx.txt -rwxrwxrwx 1 root root 2.1K Jan 23 17:52 xxx
卸载已挂载的Bucket。
如果您不希望继续挂载此Bucket，可以执行以下命令将其卸载。
sudo umount /tmp/ossfs2-bucket/
## 相关文档
[ossfs 2.0](../developer-reference/ossfs-2-0.md)[概述](../developer-reference/ossfs-2-0.md)。
[配置](../developer-reference/configure-ossfs-2-0.md)[ossfs 2.0](../developer-reference/configure-ossfs-2-0.md)。
[ossfs 2.0](../developer-reference/description-of-mount-options.md)[挂载选项说明](../developer-reference/description-of-mount-options.md)。
[ossfs 2.0](../developer-reference/mount-buckets-using-ossfs-2-0.md)[挂载](../developer-reference/mount-buckets-using-ossfs-2-0.md)[Bucket](../developer-reference/mount-buckets-using-ossfs-2-0.md)[到本地系统](../developer-reference/mount-buckets-using-ossfs-2-0.md)。
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
