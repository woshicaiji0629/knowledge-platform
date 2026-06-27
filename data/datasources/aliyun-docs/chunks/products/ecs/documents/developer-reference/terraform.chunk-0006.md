## 使用源
如果您期望从源代码编译二进制文件，可以克隆[HashiCorp Terraform](https://github.com/hashicorp/terraform)[代码库](https://github.com/hashicorp/terraform)
git clone https://github.com/hashicorp/terraform.git
您将会看到如下进度提示信息，并等待其执行完成。
执行完成后，您执行命令的目录下会新增一个terraform名称的目录。通过cd指令进入该目录。
cd terraform
然后，执行install 指令，这将会编译目录并将编译后的包移动到$GOPATH/bin/terraform目录中
go install
当您看到如下提示信息，则说明正在编译中。等待完成后即可进行下一步操作。
注意：如果提示zsh: command not found: go，则您需要先[安装](https://go.dev/doc/install)[go](https://go.dev/doc/install)[的环境](https://go.dev/doc/install)。
最终，确保terraform目录在PATH中定义并可用。 PATH定义取决于您所使用的操作系统。
