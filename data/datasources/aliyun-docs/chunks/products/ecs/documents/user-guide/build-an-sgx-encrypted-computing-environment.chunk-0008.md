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
cat <<'EOF' > install_sgx_repo.sh ID=$(grep -w '^ID' /etc/os-release | awk -F= '{print $2}' | tr -d '"') VERSION_ID=$(grep -w '^VERSION_ID' /etc/os-release | awk -F= '{print $2}' | tr -d '"') # 查看实例所在Region token=$(curl -s -X PUT -H "X-aliyun-ecs-metadata-token-ttl-seconds: 5" "http://100.100.100.200/latest/api/token") region_id=$(curl -s -H "X-aliyun-ecs-metadata-token: $token" http://100.100.100.200/latest/meta-data/region-id) # 针对Alibaba Cloud Linux 2需要启用阿里云exp源 if [ "$ID" = "alinux" -a "$VERSION_ID" = "2.1903" ]; then sudo rpmkeys --import http://mirrors.cloud.aliyuncs.com/epel/RPM-GPG-KEY-EPEL-7 sudo yum install -y alinux-release-experimentals fi yum install -y yum-utils && \ yum-config-manager --add-repo \ https://enclave-${region_id}.oss-${region_id}-internal.
