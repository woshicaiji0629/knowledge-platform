cationSample。
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
