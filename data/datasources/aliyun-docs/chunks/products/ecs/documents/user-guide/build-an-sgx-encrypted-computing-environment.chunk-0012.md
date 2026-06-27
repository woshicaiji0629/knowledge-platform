gx_repo/ubuntu ${version_codename} main" | tee /etc/apt/sources.list.d/intelsgx.list wget -qO - https://download.01.org/intel-sgx/sgx_repo/ubuntu/intel-sgx-deb.key | apt-key add - apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y libsgx-launch libsgx-urts libsgx-epid libsgx-quote-ex libsgx-dcap-ql libsgx-dcap-ql-dev systemctl enable --now aesmd.service EOF
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
阿里云SGX远程证明服务采用区域化部署，您可以访问vSGX实例所在地域的阿里云SGX远程证明服务来获得最佳的稳定性。安装阿里云TEE SDK后会自动生成远程证明服务的默认配置文件/etc/sgx_default_qcnl.conf，您需要修改该配置文件以适配vS
