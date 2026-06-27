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
