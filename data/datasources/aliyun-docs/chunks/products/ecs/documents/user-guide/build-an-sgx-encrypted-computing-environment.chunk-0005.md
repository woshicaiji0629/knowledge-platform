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
检
