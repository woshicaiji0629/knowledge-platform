## 前提条件
[创建](../../ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[ACK](../../ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)[托管集群](../../ack-managed-and-ack-dedicated/user-guide/create-an-ack-managed-cluster-2.md)。
创建集群的服务器证书，包括公钥证书和私钥。
您可以通过执行以下命令填写证书信息，快速创建集群的服务器证书。
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt
输出：
Generating a 2048 bit RSA private key .......+++ .......+++ writing new private key to 'tls.key' ----- You are about to be asked to enter information that will be incorporated into your certificate request. What you are about to enter is what is called a Distinguished Name or a DN. There are quite a few fields but you can leave some blank For some fields there will be a default value, If you enter '.', the field will be left blank. ----- Country Name (2 letter code) []:CN State or Province Name (full name) []:zhejiang Locality Name (eg, city) []:hangzhou Organization Name (eg, company) []:alibaba Organizational Unit Name (eg, section) []:test Common Name (eg, fully qualified host name) []:foo.bar.com # 注意，您需要正确配置域名 Email Address []:te**@alibaba.com
创建的证书以及私钥文件会保存在当前目录下的tls.crt
