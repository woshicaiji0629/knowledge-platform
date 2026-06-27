install -y alinux-release-experimentals fi yum install -y yum-utils && \ yum-config-manager --add-repo \ https://enclave-${region_id}.oss-${region_id}-internal.aliyuncs.com/repo/alinux/enclave-expr.repo EOF
执行以下命令，导入阿里云机密计算yum软件源。
sudo bash ./install_sgx_repo.sh
安装阿里云SGX运行时。
sudo yum install -y libsgx-ae-le libsgx-ae-pce libsgx-ae-qe3 libsgx-ae-qve \ libsgx-aesm-ecdsa-plugin libsgx-aesm-launch-plugin libsgx-aesm-pce-plugin \ libsgx-aesm-quote-ex-plugin libsgx-dcap-default-qpl libsgx-dcap-ql \ libsgx-dcap-quote-verify libsgx-enclave-common libsgx-launch libsgx-pce-logic \ libsgx-qe3-logic libsgx-quote-ex libsgx-ra-network libsgx-ra-uefi \ libsgx-uae-service libsgx-urts sgx-ra-service sgx-aesm-service
说明
SGX AESM（Architectural Enclave Service Manager）负责管理启动Enclave、密钥配置、远程认证等服务，默认安装路径为/opt/intel/sgx-aesm-service。
安装阿里云TEE SDK。
sudo yum install -y sgxsdk
阿里云TEE SDK完全兼容Intel®SGX SDK，安装阿里云TEE SDK后，您可以使用Intel®SGX Developer Reference开发SGX程序。更多信息，请参见[Intel](https://download.01.org/intel-sgx/sgx-linux/2.13/docs/Intel_SGX_Developer_Reference_Linux_2.13_Open_Source.pdf)[®](https://download.01.org/intel-sgx/sgx-linux/2.13/docs/Intel_SGX_Developer_Reference_Linux_2.13_Open_Source.pdf)[SGX Develo
