# 构建并验证SGX机密计算环境-云服务器 ECS-阿里云

Source: https://help.aliyun.com/zh/ecs/user-guide/build-an-sgx-encrypted-computing-environment

# 构建SGX机密计算环境
本文介绍如何在基于Intel®Software Guard Extensions（Intel®SGX）技术的ECS实例（下文简称为vSGX实例）中构建SGX机密计算环境，并演示如何运行示例代码以验证SGX功能。
## 前提条件
已创建并登录vSGX实例。
说明
目前仅g7t、c7t或r7t实例规格族支持SGX功能。更多信息，请参见[实例规格族](overview-of-instance-families.md)。
## 背景信息
Intel®SGX以硬件安全保障信息安全，不依赖固件和软件的安全状态，为用户提供物理级的机密计算环境。Intel®SGX通过新的指令集扩展与访问控制机制实现SGX程序的隔离运行，保障关键代码和数据的机密性与完整性不受恶意软件的破坏。不同于其他安全技术，Intel®SGX的可信根仅包括硬件，避免了基于软件的可信根可能自身存在安全漏洞的缺陷，极大地提升了系统安全保障。
阿里云安全增强型实例规格族g7t、c7t、r7t基于Intel®SGX技术提供机密内存，并支持虚拟机形态的SGX技术，您可以在vSGX实例中开发并运行SGX程序。
重要
如果您在Intel SGX Enclave中使用了与硬件相绑定的密钥加密数据（例如基于SGX Sealing），实例所在的宿主机发生变化后将导致无法解密对应数据。建议您在应用层做好数据冗余和备份，以保证应用的可靠性。
## 操作步骤
### 步骤一：检查SGX的启用状态
构建SGX机密计算环境之前，您可以通过cpuid检查SGX的启用状态。本文以Alibaba Cloud Linux 2/3 UEFI镜像和Ubuntu 22.04 UEFI镜像为例，演示如何进行SGX状态的检查过程。
## Alibaba Cloud Linux 2/3 UEFI镜像
安装cpuid。
sudo yum install -y cpuid
检查SGX的启用状态。
cpuid -1 -l 0x7 |grep SGX
下图所示表示SGX已经被正确启用。
说明
SGX被正确启用后，运行SGX程序还需要SGX驱动。阿里云提供的专用镜像已经内置了SGX驱动，如果您没有使用专用镜像，请自行安装SGX驱动。
检查SGX驱动安装情况。
ls -l /dev/{sgx_enclave,sgx_provision}
下图所示表示已经安装SGX驱动。
## Ubuntu 22.04 UEFI镜像
安装cpuid。
sudo apt-get update && sudo apt-get install -y --no-install-recommends cpuid
检查SGX的启用状态。
cpuid -1 -l 0x7 |grep SGX
下图所示表示SGX已经被正确启用。
说明
SGX被正确启用后，运行SGX程序还需要SGX驱动。阿里云提供的专用镜像已经内置了SGX驱动，如果您没有使用专用镜像，请自行安装SGX驱动。
执行以下操作安装SGX驱动。
执行以下命令，创建install_sgx_dcap.sh脚本文件。
cat <<'EOF' > install_sgx_dcap.sh #!/bin/bash version_id=$(cat /etc/os-release|grep "VERSION_ID"|cut -d"=" -f2|tr -d "\"") version_codename=$(cat /etc/os-release|grep "VERSION_CODENAME"|cut -d"=" -f2) apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential dkms curl wget if [ ! -e /dev/sgx/enclave -a ! -e /dev/sgx_enclave ]; then dcap_version=$(curl -s https://download.01.org/intel-sgx/latest/version.xml |grep dcap| sed -r 's/.*>(.*)<.*/\1/') dcap_files=$(curl -s https://download.01.org/intel-sgx/latest/dcap-latest/linux/SHA256SUM_dcap_${dcap_version}.cfg) echo "${dcap_files}" | grep "ubuntu${version_id}-server" |grep "sgx_linux_x64_driver" | awk '{print $2}' | xargs -I{} curl -O -J https://download.01.org/intel-sgx/latest/dcap-latest/linux/{} bash sgx_linux_x64_driver*.bin else echo "driver already installed" fi EOF
执行以下命令，运行脚本文件安装SGX驱动。
sudo bash ./install_sgx_dcap.sh
检查SGX驱动安装情况。
ls -l /dev/{sgx_enclave,sgx_provision}
下图所示表示已经安装SGX驱动。
### 步骤二：构建SGX机密计算环境
为开发SGX程序，您需要在vSGX实例上安装运行时（runtime）、SDK，并配置远程证明服务，建议您使用阿里云提供的专用镜像获得更好的使用体验。这些镜像已搭载SGX驱动，并提供完全兼容Intel®SGX SDK的阿里云TEE SDK。本文以Alibaba Cloud Linux 2/3和Ubuntu 22.04 UEFI镜像为例演示构建过程，如果您使用CentOS等Linux镜像，请参考Intel官方提供的[Intel](https://download.01.org/intel-sgx/latest/linux-latest/docs/Intel_SGX_SW_Installation_Guide_for_Linux.pdf)[®](https://download.01.org/intel-sgx/latest/linux-latest/docs/Intel_SGX_SW_Installation_Guide_for_Linux.pdf)[SGX](https://download.01.org/intel-sgx/latest/linux-latest/docs/Intel_SGX_SW_Installation_Guide_for_Linux.pdf)[软件安装指南](https://download.01.org/intel-sgx/latest/linux-latest/docs/Intel_SGX_SW_Installation_Guide_for_Linux.pdf)安装所需的驱动、PSW等。
安装构建SGX机密计算环境所需模块。
## Alibaba Cloud Linux 2/3 UEFI镜像
（条件必选）安装阿里云SGX运行时。
说明
如果您通过ECS管理控制台创建vSGX实例，会自动安装阿里云SGX运行时。您可以跳过本步骤，直接开始安装阿里云TEE SDK。
导入阿里云机密计算yum软件源。
说明
下述地址中的[Region-ID]应为vSGX实例所在地域的ID。
公网地址格式：https://enclave-[Region-ID].oss-[Region-ID].aliyuncs.com/repo/alinux/enclave-expr.repo。
VPC内网地址格式：https://enclave-[Region-ID].oss-[Region-ID]-internal.aliyuncs.com/repo/alinux/enclave-expr.repo。
自动化安装脚本如下所示：
执行以下命令，创建install_sgx_repo.sh脚本文件。
cat <<'EOF' > install_sgx_repo.sh ID=$(grep -w '^ID' /etc/os-release | awk -F= '{print $2}' | tr -d '"') VERSION_ID=$(grep -w '^VERSION_ID' /etc/os-release | awk -F= '{print $2}' | tr -d '"') # 查看实例所在Region token=$(curl -s -X PUT -H "X-aliyun-ecs-metadata-token-ttl-seconds: 5" "http://100.100.100.200/latest/api/token") region_id=$(curl -s -H "X-aliyun-ecs-metadata-token: $token" http://100.100.100.200/latest/meta-data/region-id) # 针对Alibaba Cloud Linux 2需要启用阿里云exp源 if [ "$ID" = "alinux" -a "$VERSION_ID" = "2.1903" ]; then sudo rpmkeys --import http://mirrors.cloud.aliyuncs.com/epel/RPM-GPG-KEY-EPEL-7 sudo yum install -y alinux-release-experimentals fi yum install -y yum-utils && \ yum-config-manager --add-repo \ https://enclave-${region_id}.oss-${region_id}-internal.aliyuncs.com/repo/alinux/enclave-expr.repo EOF
执行以下命令，导入阿里云机密计算yum软件源。
sudo bash ./install_sgx_repo.sh
安装阿里云SGX运行时。
sudo yum install -y libsgx-ae-le libsgx-ae-pce libsgx-ae-qe3 libsgx-ae-qve \ libsgx-aesm-ecdsa-plugin libsgx-aesm-launch-plugin libsgx-aesm-pce-plugin \ libsgx-aesm-quote-ex-plugin libsgx-dcap-default-qpl libsgx-dcap-ql \ libsgx-dcap-quote-verify libsgx-enclave-common libsgx-launch libsgx-pce-logic \ libsgx-qe3-logic libsgx-quote-ex libsgx-ra-network libsgx-ra-uefi \ libsgx-uae-service libsgx-urts sgx-ra-service sgx-aesm-service
说明
SGX AESM（Architectural Enclave Service Manager）负责管理启动Enclave、密钥配置、远程认证等服务，默认安装路径为/opt/intel/sgx-aesm-service。
安装阿里云TEE SDK。
sudo yum install -y sgxsdk
阿里云TEE SDK完全兼容Intel®SGX SDK，安装阿里云TEE SDK后，您可以使用Intel®SGX Developer Reference开发SGX程序。更多信息，请参见[Intel](https://download.01.org/intel-sgx/sgx-linux/2.13/docs/Intel_SGX_Developer_Reference_Linux_2.13_Open_Source.pdf)[®](https://download.01.org/intel-sgx/sgx-linux/2.13/docs/Intel_SGX_Developer_Reference_Linux_2.13_Open_Source.pdf)[SGX Developer Reference](https://download.01.org/intel-sgx/sgx-linux/2.13/docs/Intel_SGX_Developer_Reference_Linux_2.13_Open_Source.pdf)。
说明
阿里云TEE SDK中包含的Intel®SGX SDK的默认安装目录为/opt/alibaba/teesdk/intel/sgxsdk/。
## Ubuntu 22.04 UEFI镜像
执行以下命令，创建install_sgx_sdk.sh脚本文件。
cat <<'EOF' > install_sgx_sdk.sh #!/bin/bash version_id=$(cat /etc/os-release|grep "VERSION_ID"|cut -d"=" -f2|tr -d "\"") version_codename=$(cat /etc/os-release|grep "VERSION_CODENAME"|cut -d"=" -f2) apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential dkms curl wget dcap_version=$(curl -s https://download.01.org/intel-sgx/latest/version.xml |grep dcap| sed -r 's/.*>(.*)<.*/\1/') linux_version=$(curl -s https://download.01.org/intel-sgx/latest/version.xml |grep linux| sed -r 's/.*>(.*)<.*/\1/') dcap_files=$(curl -s https://download.01.org/intel-sgx/latest/dcap-latest/linux/SHA256SUM_dcap_${dcap_version}.cfg) echo "${dcap_files}" | grep "ubuntu${version_id}-server" | awk '{print $2}' | xargs -I{} curl -O -J https://download.01.org/intel-sgx/latest/dcap-latest/linux/{} # install sgx_sdk bash sgx_linux_x64_sdk*.bin --prefix /opt/intel source /opt/intel/sgxsdk/environment # install psw echo "deb [arch=amd64] https://download.01.org/intel-sgx/sgx_repo/ubuntu ${version_codename} main" | tee /etc/apt/sources.list.d/intelsgx.list wget -qO - https://download.01.org/intel-sgx/sgx_repo/ubuntu/intel-sgx-deb.key | apt-key add - apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y libsgx-launch libsgx-urts libsgx-epid libsgx-quote-ex libsgx-dcap-ql libsgx-dcap-ql-dev systemctl enable --now aesmd.service EOF
执行以下命令，运行脚本文件安装Intel®SGX SDK和PSW。
sudo bash ./install_sgx_sdk.sh
配置阿里云SGX远程证明服务。
阿里云SGX远程证明服务完全兼容Intel®SGX ECDSA远程证明服务和Intel®SGX SDK，因此阿里云vSGX实例能够通过远程证明来获得远程提供商或生产者的信任。更多信息，请参见[Attestation & Provisioning Services](https://software.intel.com/content/www/us/en/develop/topics/software-guard-extensions/attestation-services.html)。
阿里云SGX远程证明服务为SGX SDK提供下列信息：
SGX certificates：SGX证书。
Revocation lists：已被撤销的SGX证书列表。
Trusted computing base information：可信根信息。
说明
Intel Ice Lake仅支持基于Intel SGX DCAP的远程证明方式，不支持基于Intel EPID的远程证明方式，您可能需要适配程序后才能正常使用远程证明功能。更多远程证明的信息，请参见[attestation-service](https://software.intel.com/content/www/us/en/develop/topics/software-guard-extensions/attestation-services.html)。
阿里云SGX远程证明服务采用区域化部署，您可以访问vSGX实例所在地域的阿里云SGX远程证明服务来获得最佳的稳定性。安装阿里云TEE SDK后会自动生成远程证明服务的默认配置文件/etc/sgx_default_qcnl.conf，您需要修改该配置文件以适配vSGX实例所在地域的阿里云SGX远程证明服务，方法如下：
说明
目前阿里云SGX远程证明服务仅支持如下地域和可用区。
| 支持的地域 | Region ID |
| --- | --- |
| 华北 1（青岛） | cn-qingdao |
| 华北 2（北京） | cn-beijing |
| 华北 3（张家口） | cn-zhangjiakou |
| 华北 6（乌兰察布） | cn-wulanchabu |
| 华东 1（杭州） | cn-hangzhou |
| 华东 2（上海） | cn-shanghai |
| 华南 1（深圳） | cn-shenzhen |
| 华南 2（河源） | cn-heyuan |
| 华南 3（广州） | cn-guangzhou |
| 西南 1（成都） | cn-chengdu |
| 中国（香港） | cn-hongkong |
| 新加坡 | ap-southeast-1 |
| 印度尼西亚（雅加达） | ap-southeast-5 |
（推荐）方法一：自动化完成/etc/sgx_default_qcnl.conf文件的配置。
执行如下命令，自动化完成/etc/sgx_default_qcnl.conf文件的配置。更多命令信息，请参见[实例元数据](view-instance-metadata.md)。
# 查看实例所在Region token=$(curl -s -X PUT -H "X-aliyun-ecs-metadata-token-ttl-seconds: 5" "http://100.100.100.200/latest/api/token") region_id=$(curl -s -H "X-aliyun-ecs-metadata-token: $token" http://100.100.100.200/latest/meta-data/region-id) # 配置PCCS_URL指向实例所在Region的PCCS PCCS_URL=https://sgx-dcap-server-vpc.${region_id}.aliyuncs.com/sgx/certification/v4/ sudo bash -c 'cat > /etc/sgx_default_qcnl.conf' << EOF # PCCS server address PCCS_URL=${PCCS_URL} # To accept insecure HTTPS cert, set this option to FALSE USE_SECURE_CERT=TRUE EOF
方法二：手动修改/etc/sgx_default_qcnl.conf配置文件。
如果vSGX实例已分配公网IP，/etc/sgx_default_qcnl.conf文件的内容修改如下。其中，[Region-ID]需替换为vSGX实例所在地域的ID。
# PCCS server address PCCS_URL=https://sgx-dcap-server.[Region-ID].aliyuncs.com/sgx/certification/v4/ # To accept insecure HTTPS cert, set this option to FALSE USE_SECURE_CERT=TRUE
如果vSGX实例只有VPC内网IP，/etc/sgx_default_qcnl.conf文件的内容修改如下。其中，[Region-ID]需替换为vSGX实例所在地域的ID。
# PCCS server address PCCS_URL=https://sgx-dcap-server-vpc.[Region-ID].aliyuncs.com/sgx/certification/v4/ # To accept insecure HTTPS cert, set this option to FALSE USE_SECURE_CERT=TRUE
## 验证SGX功能示例
本节演示其中的启动Enclave示例（SampleEnclave），效果为启动一个Enclave，以验证是否可以正常使用安装的SGX SDK。
### 示例一：启动Enclave
## Alibaba Cloud Linux 2/3 UEFI镜像
阿里云TEE SDK中提供了SGX示例代码用于验证SGX功能，默认位于/opt/alibaba/teesdk/intel/sgxsdk/SampleCode目录下。
安装编译工具。
ID=$(grep -w '^ID' /etc/os-release | awk -F= '{print $2}' | tr -d '"') VERSION_ID=$(grep -w '^VERSION_ID' /etc/os-release | awk -F= '{print $2}' | tr -d '"') if [ "$ID" = "alinux" ]; then case "$VERSION_ID" in "2.1903" ) sudo yum install -y devtoolset-9 ;; "3" ) sudo yum groupinstall -y "Development Tools" ;; esac fi
设置SGX SDK相关的环境变量。
if [ "$ID" = "alinux" -a "$VERSION_ID" = "2.1903" ]; then source /opt/rh/devtoolset-9/enable fi source /opt/alibaba/teesdk/intel/sgxsdk/environment
编译示例代码SampleEnclave。
执行以下命令，进入SampleEnclave目录。
cd /opt/alibaba/teesdk/intel/sgxsdk/SampleCode/SampleEnclave
执行以下命令，编译SampleEnclave。
sudo -E make
运行编译出的可执行文件。
sudo ./app
出现类似如下信息时，表示SGX功能运行正常。
## Ubuntu 22.04 UEFI镜像
执行以下命令，更新包列表。
sudo apt update
执行以下命令，安装build-essential编译工具。
sudo apt install -y build-essential
编译示例代码SampleEnclave。
执行以下命令，进入SampleEnclave目录。
cd /opt/intel/sgxsdk/SampleCode/SampleEnclave/
执行以下命令，编译SampleEnclave。
sudo make SGX_DEBUG=1
运行编译出的可执行文件。
sudo ./app
出现类似如下信息时，表示SGX功能运行正常。
### 示例二：SGX远程证明
本示例以Alibaba Cloud Linux 2/3 UEFI镜像为例演示SGX远程证明过程，阿里云TEE SDK中提供了SGX示例代码用于验证SGX功能，默认位于/opt/alibaba/teesdk/intel/sgxsdk/SampleCode目录下。
本节演示其中的SGX远程证明示例（QuoteGenerationSample、QuoteVerificationSample），效果为生成和验证Quote。该示例涉及被挑战方（在vSGX实例中运行的SGX程序）和挑战方（希望验证SGX程序是否可信的一方），其中QuoteGenerationSample为被挑战方生成Quote的示例代码，QuoteVerificationSample为挑战方验证Quote的示例代码。
安装编译工具。
如果为Alibaba Cloud Linux 2 UEFI镜像，安装devtoolset。
安装devtoolset。
sudo yum install -y devtoolset-9
设置devtoolset相关的环境变量。
source /opt/rh/devtoolset-9/enable
如果为Alibaba Cloud Linux 3 UEFI镜像，安装Development Tools。
sudo yum groupinstall -y "Development Tools"
设置SGX SDK相关的环境变量。
source /opt/alibaba/teesdk/intel/sgxsdk/environment
安装SGX远程证明依赖的包。
sudo yum install -y libsgx-dcap-ql-devel libsgx-dcap-quote-verify-devel libsgx-dcap-default-qpl-devel
编译被挑战方示例代码QuoteGenerationSample。
进入QuoteGenerationSample目录。
cd /opt/alibaba/teesdk/intel/sgxsdk/SampleCode/QuoteGenerationSample
编译QuoteGenerationSample。
sudo -E make
运行编译出的可执行文件生成Quote。
sudo ./app
出现类似如下信息时，表示Quote验证成功。
编译挑战方示例代码QuoteVerificationSample。
进入QuoteVerificationSample目录。
cd /opt/alibaba/teesdk/intel/sgxsdk/SampleCode/QuoteVerificationSample
编译QuoteVerificationSample。
sudo -E make
对QuoteVerificationSample Enclave进行签名。
发布对外的正式版Enclave时，您需要提供签名密钥进行签名操作。
sudo sgx_sign sign -key Enclave/Enclave_private_sample.pem -enclave enclave.so -out enclave.signed.so -config Enclave/Enclave.config.xml
说明
如果执行该命令提示报错Failed to open file "Enclave/Enclave_private_sample.pem"，您可以执行如下命令重新进行签名：
sudo sgx_sign sign -key ../QuoteGenerationSample/Enclave/Enclave_private_sample.pem -enclave enclave.so -out enclave.signed.so -config Enclave/Enclave.config.xml
运行编译出的可执行文件验证Quote。
sudo ./app
出现类似如下信息时，表示Quote验证成功。
## 更新SGX SDK、PSW及DCAP软件包
Intel®SGX的软件栈主要包括[SGX SDK](https://github.com/intel/linux-sgx#install-the-intelr-sgx-sdk)、[SGX PSW](https://github.com/intel/linux-sgx#install-the-intelr-sgx-psw-1)和[SGX DCAP](https://github.com/intel/SGXDataCenterAttestationPrimitives#intelr-software-guard-extensions-data-center-attestation-primitives)，阿里云建议您定期更新软件版本以提供最佳的安全性。本节以Alibaba Cloud Linux 3 UEFI镜像为例演示更新SGX SDK、PSW及DCAP软件包的过程。
执行如下命令，升级SGX SDK、SGX PSW和SGX DCAP相关软件包。
sudo rpm -qa --qf "%{NAME}\n"|grep -E "sgxsdk|libsgx-|libtdx-|^sgx-|^tdx-"|sudo xargs bash -c '</dev/tty yum update "$@"' _
查看SGX SDK、SGX PSW和SGX DCAP软件版本。
查看SGX SDK、SGX PSW软件版本。
sudo rpm -qa|grep -E "sgxsdk|sgx-aesm-service|libsgx-(ae-epid|ae-le|ae-pce|aesm|enclave|epid|headers|launch|quote-ex|uae-service|urts)"
系统显示类似如下回显信息。
查看SGX DCAP软件版本。
sudo rpm -qa|grep -E "sgx-(dcap-pccs|pck|ra-service)|libsgx-(ae-id-enclave|ae-qe3|ae-qve|ae-tdqe|dcap|pce-logic|qe3-logic|ra-|tdx-)|libtdx-|^tdx-"
系统显示类似如下回显信息。
## 已知问题
Alibaba Cloud Linux 2在内核版本4.19.91-23.al7.x86_64中所包含的SGX驱动在特定情况下存在内存泄漏问题，该问题已在最新版本中修复，建议您更新到最新内核版本解决该问题。如果您需要继续使用该内核版本，建议安装补丁规避此问题，安装命令如下。
sudo yum install -y alinux-release-experimentals && \ sudo yum install -y kernel-hotfix-5577959-23.al7.x86_64
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
