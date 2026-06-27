## macOS Homebrew
[Homebrew](https://brew.sh/)是一款在Mac系统上经常使用的包安装工具。借助Homebrew可以通过简单的指令安装Terraform。
第一步，安装HashiCorp的tap，用来定义包在Homebrew的位置。
brew tap hashicorp/tap
第二步，执行安装指令，安装Terraform
brew install hashicorp/tap/terraform
重要
安装指令将索引最新的版本并进行安装，如果在安装一段时间后希望更新到最新版本。可以通过重新执行upgrade指令进行。
更新最新版本的Terraform，首先需要更新Homebrew。
brew update
然后，运行upgrade指令更新到最新版本。
brew upgrade hashicorp/tap/terraform
