## Ubuntu
sudo apt install -y unzip
根据操作系统与架构选择对应安装包（[Linux x86 32bit](https://gosspublic.alicdn.com/ossutil/v2/2.3.0/ossutil-2.3.0-linux-386.zip)、[Linux x86 64bit](https://gosspublic.alicdn.com/ossutil/v2/2.3.0/ossutil-2.3.0-linux-amd64.zip)、[Linux ARM 32bit](https://gosspublic.alicdn.com/ossutil/v2/2.3.0/ossutil-2.3.0-linux-arm.zip)、[Linux ARM 64bit](https://gosspublic.alicdn.com/ossutil/v2/2.3.0/ossutil-2.3.0-linux-arm64.zip)），也可通过 curl 下载。以下以在 Linux x86_64 上使用 curl 获取为例：
curl -o ossutil-2.3.0-linux-amd64.zip https://gosspublic.alicdn.com/ossutil/v2/2.3.0/ossutil-2.3.0-linux-amd64.zip
在下载压缩包的所在目录执行以下解压命令。
unzip ossutil-2.3.0-linux-amd64.zip
进入ossutil-2.3.0-linux-amd64目录。
cd ossutil-2.3.0-linux-amd64
在当前目录执行以下命令。
chmod 755 ossutil
执行以下命令，实现ossutil的全局调用。
sudo mv ossutil /usr/local/bin/ && sudo ln -s /usr/local/bin/ossutil /usr/bin/ossutil
验证是否成功安装ossutil，执行ossutil命令。
ossutil
返回ossutil的帮助信息即表示安装成功。
