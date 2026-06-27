### Linux
在命令行界面执行以下命令来将环境变量设置追加到~/.bashrc文件中。
echo "export OSS_ACCESS_KEY_ID='YOUR_ACCESS_KEY_ID'" >> ~/.bashrc echo "export OSS_ACCESS_KEY_SECRET='YOUR_ACCESS_KEY_SECRET'" >> ~/.bashrc
执行以下命令使变更生效。
source ~/.bashrc
执行以下命令检查环境变量是否生效。
echo $OSS_ACCESS_KEY_ID echo $OSS_ACCESS_KEY_SECRET
