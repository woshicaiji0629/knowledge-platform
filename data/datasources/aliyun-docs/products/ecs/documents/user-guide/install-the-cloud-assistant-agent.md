# 安装云助手Agent-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/install-the-cloud-assistant-agent

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [用户指南](products/ecs/documents/user-guide.md)

- [开发参考](products/ecs/documents/developer-reference.md)

- [产品计费](products/ecs/documents/billing-2.md)

- [常见问题](products/ecs/documents/faqs.md)

- [动态与公告](products/ecs/documents/announcements-and-updates.md)

[首页](https://help.aliyun.com/zh)

# 安装云助手Agent

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/ecs)

[我的收藏](https://help.aliyun.com/my_favorites.html)

需要通过控制台或API进行免登录管理、执行命令或者发送文件等操作时，必须在目标实例上安装并运行云助手Agent。

## 适用范围

以下操作系统支持安装云助手Agent：

- 

Linux：Alibaba Cloud Linux、AlmaLinux 8+、Anolis OS 7+、CentOS 5+、Debian 8+、Ubuntu 12+、RHEL 5+、SUSE 11+、Fedora 33+、CoreOS、OpenSUSE。

- 

FreeBSD：11+。

- 

Windows：Server 2012+。

自2017年12月1日起，通过公共镜像创建的ECS实例已预装云助手Agent。

## 操作步骤

### 控制台

- 

访问[ECS](https://ecs.console.aliyun.com/cloud-assistant/region)[控制台-云助手](https://ecs.console.aliyun.com/cloud-assistant/region)。

- 

在页面左侧顶部，选择目标资源所在的资源组和地域。

- 

单击ECS实例页签，查看当前地域ECS实例上的云助手状态。

- 

正常：已安装。

- 

未安装：单击一键安装，等待安装完成，需要重启实例之后查看状态是否变为正常。

- 

异常：请参见[云助手异常状态处理](products/ecs/documents/user-guide/check-the-status-of-cloud-assistant-and-handle-exceptions.md)。

### Linux实例

步骤一：检查是否已安装云助手Agent

- 

[使用](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[Workbench](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[登录](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[Linux](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)[实例](products/ecs/documents/user-guide/connect-to-a-linux-instance-by-using-a-password-or-key.md)。

- 

判断初始化系统类型。

初始化系统（init system）负责在系统启动时加载和管理服务进程，不同初始化系统对应的云助手Agent的命令不同。

- 

systemd：Alibaba Cloud Linux、CentOS 7+、RHEL 7+、Fedora 15+、Ubuntu 15.04+、Debian 8+等。

- 

Upstart：Ubuntu 6.10-14.10、RHEL 6、CentOS 6等。

- 

SysVinit：RHEL 5、CentOS 5、Debian 6等。

- 

验证是否安装云助手Agent。

systemdsystemctl status aliyun.service

若回执信息包含Unit aliyun.service could not be found提示，表示未安装。

upstart/sbin/initctl status aliyun-service

若回执信息包含initctl: Unknown job: aliyun-service提示，表示未安装。

sysvinit/etc/init.d/aliyun-service status

若回执信息为空，表示未安装。

步骤二：下载并安装云助手Agent

脚本适用于阿里云ECS实例，默认安装最新版本的Agent，安装指定版本请修改VERSION=latest。

#!/bin/bash VERSION=latest PACKAGE= PKG_URI= REGION=$(curl -s http://100.100.100.200/latest/meta-data/region-id) DOMAIN=aliyun-client-assist-${REGION}.oss-${REGION}-internal.aliyuncs.com arch=$(uname -m) echo "[main] arch = ${arch}" # 检测是否为 openSUSE 或 SLES 系统 is_suse_like() { if [[ -f /etc/os-release ]]; then local os_id os_id=$(grep -E "^ID=" /etc/os-release | tr -d '"' | cut -d= -f2) local os_version os_version=$(grep -E "^VERSION_ID=" /etc/os-release | tr -d '"' | cut -d= -f2 | cut -d. -f1) if ([[ "$os_id" == "opensuse"* ]] || [[ "$os_id" == "sles" ]]) && [[ "$os_version" == "16" ]]; then return 0 fi fi return 1 } case $arch in "i386"|"i686"|"x86_64"|"amd64") if command -v rpm && ! command -v dpkg; then if [[ "$arch" == "x86_64" ]] && is_suse_like; then PACKAGE="aliyun_assist_${VERSION}_x86_64.rpm" else PACKAGE="aliyun_assist_${VERSION}.rpm" fi else if [[ "$arch" == "x86_64" ]] && is_suse_like; then PACKAGE="aliyun_assist_${VERSION}_x86_64.deb" else PACKAGE="aliyun_assist_${VERSION}.deb" fi fi PKG_URI="https://$DOMAIN/linux/$PACKAGE" ;; *) if command -v rpm && ! command -v dpkg; then PACKAGE="aliyun-assist-${VERSION}-1.aarch64.rpm" else PACKAGE="aliyun-assist_${VERSION}-1_arm64.deb" fi PKG_URI="https://$DOMAIN/arm/$PACKAGE" ;; esac echo "[main] package = ${PACKAGE}" echo "[main] pkg_uri = ${PKG_URI}" if command -v wget; then sudo wget -O "${PACKAGE}" "${PKG_URI}" elif command -v curl; then sudo curl -o "${PACKAGE}" "${PKG_URI}" else echo "[WARN] command wget/curl not found, exit" exit 1 fi if command -v rpm && ! command -v dpkg; then sudo rpm -ivh --force "${PACKAGE}" elif command -v dpkg; then sudo dpkg -i "${PACKAGE}" else echo "[WARN] command rpm/dpkg not found, exit" exit 2 fi if [[ -e /etc/redhat-release ]]; then if sudo systemctl status qemu-guest-agent; then sudo systemctl stop qemu-guest-agent sudo systemctl disable qemu-guest-agent sudo systemctl restart aliyun.service fi fi

### Windows实例

步骤一：检查是否已安装云助手Agent

- 

[使用远程桌面/Windows App](products/ecs/documents/user-guide/connect-to-a-windows-instance-by-using-a-username-and-password.md)[远程连接](products/ecs/documents/user-guide/connect-to-a-windows-instance-by-using-a-username-and-password.md)[Windows](products/ecs/documents/user-guide/connect-to-a-windows-instance-by-using-a-username-and-password.md)[实例](products/ecs/documents/user-guide/connect-to-a-windows-instance-by-using-a-username-and-password.md)。

- 

查看云助手服务状态。

- 

单击开始菜单，搜索计算机管理。

- 

选择服务和应用程序>服务。

- 

查找Aliyun Assist Service，若不存在，表示未安装。

步骤二：下载并安装云助手Agent方法一：通过浏览器下载云助手Agent

- 

下载云助手Agent。

将地址中的{regionId}替换为实例所在[地域](products/ecs/documents/user-guide/regions-and-zones.md)[ID](products/ecs/documents/user-guide/regions-and-zones.md)后，在浏览器中打开。

https://aliyun-client-assist-{regionId}.oss-{regionId}-internal.aliyuncs.com/windows/aliyun_agent_latest_setup.exe # 示例：杭州（cn-hangzhou）下载地址 https://aliyun-client-assist-cn-hangzhou.oss-cn-hangzhou-internal.aliyuncs.com/windows/aliyun_agent_latest_setup.exe

- 

安装云助手Agent。

双击云助手Agent文件，根据安装向导完成安装。默认安装路径为C:\ProgramData\aliyun\assist\。

方法二：通过PowerShell安装并启动云助手Agent

将脚本中的{regionId}替换为实例所在[地域](products/ecs/documents/user-guide/regions-and-zones.md)[ID](products/ecs/documents/user-guide/regions-and-zones.md)后，在PowerShell中执行。

curl -UseBasicParsing -Uri https://aliyun-client-assist-{regionId}.oss-{regionId}-internal.aliyuncs.com/windows/aliyun_agent_latest_setup.exe -OutFile 'C:\aliyun_agent_latest_setup.exe' & "C:\aliyun_agent_latest_setup.exe" /S

## API

通过API安装云助手Agent不区分操作系统类型。

- 

调用[DescribeCloudAssistantStatus](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describecloudassistantstatus.md)查询目标ECS实例是否安装了云助手Agent。

CloudAssistantStatus返回false时，表示未安装。

- 

若实例未安装云助手Agent，则调用[InstallCloudAssistant](products/ecs/documents/developer-reference/api-ecs-2014-05-26-installcloudassistant.md)安装云助手Agent。

- 

安装完成之后，调用[RebootInstance](products/ecs/documents/api-rebootinstance.md)重启ECS实例使安装生效。

## CLI

通过[阿里云](https://help.aliyun.com/zh/cli/what-is-alibaba-cloud-cli)[CLI](https://help.aliyun.com/zh/cli/what-is-alibaba-cloud-cli)安装云助手Agent不区分操作系统类型。请替换命令中的<YOUR-REGION-ID>为ECS实例所在[地域](products/ecs/documents/user-guide/regions-and-zones.md)[ID](products/ecs/documents/user-guide/regions-and-zones.md)，<YOUR-INSTANCE-ID>为ECS实例ID。

Red Hat Enterprise Linux (RHEL) 不支持通过阿里云CLI安装。

- 

调用[DescribeCloudAssistantStatus](products/ecs/documents/developer-reference/api-ecs-2014-05-26-describecloudassistantstatus.md)查询目标ECS实例是否安装了云助手Agent。

aliyun ecs DescribeCloudAssistantStatus --RegionId <YOUR-REGION-ID> --InstanceId.1 <YOUR-INSTANCE-ID> --output cols=CloudAssistantStatus rows=InstanceCloudAssistantStatusSet.InstanceCloudAssistantStatus[]

返回CloudAssistantStatus=true时，表示ECS实例已安装云助手Agent。

- 

调用[InstallCloudAssistant](products/ecs/documents/developer-reference/api-ecs-2014-05-26-installcloudassistant.md)安装云助手Agent。

aliyun ecs InstallCloudAssistant --RegionId <YOUR-REGION-ID> --InstanceId.1 <YOUR-INSTANCE-ID>

- 

调用[RebootInstance](products/ecs/documents/api-rebootinstance.md)重启ECS实例。

aliyun ecs RebootInstance --InstanceId <YOUR-INSTANCE-ID>

## 常见问题

如果我的操作系统不支持安装云助手Agent，该怎么办？

- 

[迁移操作系统](products/ecs/documents/user-guide/migrate-the-operating-system-of-an-ecs-instance.md)：将当前系统升级或迁移到受支持的版本。

- 

[更换操作系统（更换系统盘）](products/ecs/documents/user-guide/replace-the-operating-system-of-an-instance.md)：通过更换系统盘功能，为实例安装一个受支持的操作系统。

为什么操作系统支持但无法安装最新版本的云助手Agent？

部分内核在安装云助手时存在最高可安装版本的限制。

执行uname -r查看内核版本。

- 

- 

| 实例的内核版本号 | 云助手 Agent 可升级的最高版本 |
| --- | --- |
| Linux 内核版本 < 2.6.32 | X86/X64 架构：2.2.3.398 ARM 架构：2.4.3.398 |
| FreeBSD 内核版本 < 12.x | 2.3.3.529 |


FreeBSD操作系统如何安装云助手Agent？

- 

适用于阿里云ECS实例

#!/bin/sh VERSION=latest use_curl=0 which curl >/dev/null 2>&1 && use_curl=1 if [ $use_curl -eq 1 ];then REGION=$(curl http://100.100.100.200/latest/meta-data/region-id) else REGION=$(wget -O - http://100.100.100.200/latest/meta-data/region-id) fi DOMAIN=aliyun-client-assist-${REGION}.oss-${REGION}-internal.aliyuncs.com PACKAGE=aliyun_assist_${VERSION}.txz PKG_URI="https://$DOMAIN/freebsd/$PACKAGE" if [ $use_curl -eq 1 ];then curl -o $PACKAGE $PKG_URI else wget -O $PACKAGE $PKG_URI fi pkg install -U -y $PACKAGE service aliyun start

- 

适用于托管实例（非阿里云服务器）

#!/bin/sh VERSION=latest DOMAIN=aliyun-client-assist.oss-accelerate.aliyuncs.com PACKAGE=aliyun_assist_${VERSION}.txz PKG_URI="https://$DOMAIN/freebsd/$PACKAGE" use_curl=0 which curl >/dev/null 2>&1 && use_curl=1 if [ $use_curl -eq 1 ];then curl -o $PACKAGE $PKG_URI else wget -O $PACKAGE $PKG_URI fi pkg install -U -y $PACKAGE service aliyun start

托管实例（非阿里云服务器）如何安装云助手Agent？

Linux脚本默认安装最新版本的Agent，安装指定版本请修改VERSION=latest。#!/bin/bash VERSION=latest PACKAGE= PKG_URI= DOMAIN=aliyun-client-assist.oss-accelerate.aliyuncs.com arch=$(uname -m) echo "[main] arch = ${arch}" # 检测是否为 openSUSE 或 SLES 系统 is_suse_like() { if [[ -f /etc/os-release ]]; then local os_id os_id=$(grep -E "^ID=" /etc/os-release | tr -d '"' | cut -d= -f2) local os_version os_version=$(grep -E "^VERSION_ID=" /etc/os-release | tr -d '"' | cut -d= -f2 | cut -d. -f1) if ([[ "$os_id" == "opensuse"* ]] || [[ "$os_id" == "sles" ]]) && [[ "$os_version" == "16" ]]; then return 0 fi fi return 1 } case $arch in "i386"|"i686"|"x86_64"|"amd64") if command -v rpm && ! command -v dpkg; then if [[ "$arch" == "x86_64" ]] && is_suse_like; then PACKAGE="aliyun_assist_${VERSION}_x86_64.rpm" else PACKAGE="aliyun_assist_${VERSION}.rpm" fi else if [[ "$arch" == "x86_64" ]] && is_suse_like; then PACKAGE="aliyun_assist_${VERSION}_x86_64.deb" else PACKAGE="aliyun_assist_${VERSION}.deb" fi fi PKG_URI="https://$DOMAIN/linux/$PACKAGE" ;; *) if command -v rpm && ! command -v dpkg; then PACKAGE="aliyun-assist-${VERSION}-1.aarch64.rpm" else PACKAGE="aliyun-assist_${VERSION}-1_arm64.deb" fi PKG_URI="https://$DOMAIN/arm/$PACKAGE" ;; esac echo "[main] package = ${PACKAGE}" echo "[main] pkg_uri = ${PKG_URI}" if command -v wget; then sudo wget -O "${PACKAGE}" "${PKG_URI}" elif command -v curl; then sudo curl -o "${PACKAGE}" "${PKG_URI}" else echo "[WARN] command wget/curl not found, exit" exit 1 fi if command -v rpm && ! command -v dpkg; then sudo rpm -ivh --force "${PACKAGE}" elif command -v dpkg; then sudo dpkg -i "${PACKAGE}" else echo "[WARN] command rpm/dpkg not found, exit" exit 2 fi if [[ -e /etc/redhat-release ]]; then if sudo systemctl status qemu-guest-agent; then sudo systemctl stop qemu-guest-agent sudo systemctl disable qemu-guest-agent sudo systemctl restart aliyun.service fi fi

Windows方法一：通过浏览器打开网址下载云助手Agent。

- 

在浏览器中打开网址下载云助手Agent。

https://aliyun-client-assist.oss-accelerate.aliyuncs.com/windows/aliyun_agent_latest_setup.exe

- 

安装云助手Agent。

双击云助手Agent文件，根据安装向导完成安装。默认安装路径为C:\ProgramData\aliyun\assist\。

方法二：通过PowerShell安装并启动云助手Agentcurl -UseBasicParsing -Uri https://aliyun-client-assist.oss-accelerate.aliyuncs.com/windows/aliyun_agent_latest_setup.exe -OutFile 'C:\\aliyun_agent_latest_setup.exe' ;"C:\\aliyun_agent_latest_setup.exe" '/S'

云助手Agent如何通过二进制包或者源码等方式安装？

## 二进制包（Binary）安装

- 

适用于阿里云ECS实例

脚本默认安装最新版本的Agent，安装指定版本请修改VERSION=latest。#!/bin/bash VERSION=latest PACKAGE= PKG_URI= REGION=$(curl -s http://100.100.100.200/latest/meta-data/region-id) DOMAIN=aliyun-client-assist-${REGION}.oss-${REGION}-internal.aliyuncs.com arch=$(uname -m) echo "[main] arch = ${arch}" # 检测是否为 openSUSE 或 SLES 系统 is_suse_like() { if [[ -f /etc/os-release ]]; then local os_id os_id=$(grep -E "^ID=" /etc/os-release | tr -d '"' | cut -d= -f2) local os_version os_version=$(grep -E "^VERSION_ID=" /etc/os-release | tr -d '"' | cut -d= -f2 | cut -d. -f1) if ([[ "$os_id" == "opensuse"* ]] || [[ "$os_id" == "sles" ]]) && [[ "$os_version" == "16" ]]; then return 0 fi fi return 1 } case $arch in "i386"|"i686"|"x86_64"|"amd64") if [[ "$arch" == "x86_64" ]] && is_suse_like; then PACKAGE="aliyun_assist_${VERSION}_update_x86_64.zip" else PACKAGE="aliyun_assist_${VERSION}_update.zip" fi PKG_URI="https://$DOMAIN/linux/$PACKAGE" ;; *) PACKAGE="aliyun_assist_${VERSION}_update_arm.zip" PKG_URI="https://$DOMAIN/arm/$PACKAGE" ;; esac echo "[main] package = ${PACKAGE}" echo "[main] pkg_uri = ${PKG_URI}" if command -v wget; then sudo wget -O "${PACKAGE}" "${PKG_URI}" elif command -v curl; then sudo curl -o "${PACKAGE}" "${PKG_URI}" else echo "[WARN] command wget/curl not found, exit" exit 1 fi TARGET_DIR=/usr/local/share/aliyun-assist sudo unzip -o "${PACKAGE}" -d $TARGET_DIR/ TRUE_VERSION=$(cat $TARGET_DIR/version) sudo chmod a+x $TARGET_DIR/$TRUE_VERSION/update_install sudo bash $TARGET_DIR/$TRUE_VERSION/update_install

- 

适用于托管实例（非阿里云服务器）

#!/bin/bash VERSION=latest PACKAGE= PKG_URI= DOMAIN=aliyun-client-assist.oss-accelerate.aliyuncs.com arch=$(uname -m) echo "[main] arch = ${arch}" # 检测是否为 openSUSE 或 SLES 系统 is_suse_like() { if [[ -f /etc/os-release ]]; then local os_id os_id=$(grep -E "^ID=" /etc/os-release | tr -d '"' | cut -d= -f2) local os_version os_version=$(grep -E "^VERSION_ID=" /etc/os-release | tr -d '"' | cut -d= -f2 | cut -d. -f1) if ([[ "$os_id" == "opensuse"* ]] || [[ "$os_id" == "sles" ]]) && [[ "$os_version" == "16" ]]; then return 0 fi fi return 1 } case $arch in "i386"|"i686"|"x86_64"|"amd64") if [[ "$arch" == "x86_64" ]] && is_suse_like; then PACKAGE="aliyun_assist_${VERSION}_update_x86_64.zip" else PACKAGE="aliyun_assist_${VERSION}_update.zip" fi PKG_URI="https://$DOMAIN/linux/$PACKAGE" ;; *) PACKAGE="aliyun_assist_${VERSION}_update_arm.zip" PKG_URI="https://$DOMAIN/arm/$PACKAGE" ;; esac echo "[main] package = ${PACKAGE}" echo "[main] pkg_uri = ${PKG_URI}" if command -v wget; then sudo wget -O "${PACKAGE}" "${PKG_URI}" elif command -v curl; then sudo curl -o "${PACKAGE}" "${PKG_URI}" else echo "[WARN] command wget/curl not found, exit" exit 1 fi TARGET_DIR=/usr/local/share/aliyun-assist sudo unzip -o "${PACKAGE}" -d $TARGET_DIR/ TRUE_VERSION=$(cat $TARGET_DIR/version) sudo chmod a+x $TARGET_DIR/$TRUE_VERSION/update_install sudo bash $TARGET_DIR/$TRUE_VERSION/update_install

## 源码安装

示例通过yum安装，如果使用其他Linux版本，请修改为对应的包管理工具。

- 

安装Git和Go等必要的软件。

# 安装Git sudo yum install git -y # 安装Go sudo yum install go -y

- 

下载云助手Agent源码。

sudo git clone https://github.com/aliyun/aliyun_assist_client

- 

进入源码存放目录，编译源码。

# 进入源码存放目录 cd ./aliyun_assist_client # 编译源码 sudo go build

如果返回结果无报错信息，表示安装成功。

[上一篇：配置云助手Agent](products/ecs/documents/user-guide/configure-the-cloud-assistant-agent.md)[下一篇：查看云助手状态及异常状态处理](products/ecs/documents/user-guide/check-the-status-of-cloud-assistant-and-handle-exceptions.md)

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
