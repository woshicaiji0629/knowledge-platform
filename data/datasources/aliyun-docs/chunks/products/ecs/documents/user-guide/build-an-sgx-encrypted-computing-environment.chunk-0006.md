x/latest/dcap-latest/linux/{} bash sgx_linux_x64_driver*.bin else echo "driver already installed" fi EOF
执行以下命令，运行脚本文件安装SGX驱动。
sudo bash ./install_sgx_dcap.sh
检查SGX驱动安装情况。
ls -l /dev/{sgx_enclave,sgx_provision}
下图所示表示已经安装SGX驱动。
