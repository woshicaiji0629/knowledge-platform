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
对Quote
