### macOS
在终端中执行以下命令，查看默认Shell类型。
echo $SHELL
根据默认Shell类型进行操作。
Zsh
执行以下命令来将环境变量设置追加到~/.zshrc文件中。
echo "export OSS_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.zshrc echo "export OSS_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.zshrc
执行以下命令使变更生效。
source ~/.zshrc
执行以下命令检查环境变量是否生效。
echo $OSS_ACCESS_KEY_ID echo $OSS_ACCESS_KEY_SECRET
Bash
执行以下命令来将环境变量设置追加到~/.bash_profile文件中。
echo "export OSS_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bash_profile echo "export OSS_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bash_profile
执行以下命令使变更生效。
source ~/.bash_profile
执行以下命令检查环境变量是否生效。
echo $OSS_ACCESS_KEY_ID echo $OSS_ACCESS_KEY_SECRET
