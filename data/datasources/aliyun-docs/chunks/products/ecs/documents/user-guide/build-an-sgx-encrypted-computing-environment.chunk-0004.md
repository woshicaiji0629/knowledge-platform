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
