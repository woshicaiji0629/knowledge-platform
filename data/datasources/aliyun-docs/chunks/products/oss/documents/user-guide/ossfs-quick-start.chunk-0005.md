### Ubuntu/Debian
执行以下命令，下载安装包。
sudo wget https://gosspublic.alicdn.com/ossfs/ossfs2_2.0.7_linux_x86_64.deb
执行以下命令，安装ossfs 2.0。
sudo dpkg -i ossfs2_2.0.7_linux_x86_64.deb
执行以下命令，验证ossfs 2.0是否成功安装。
ossfs2 --version
说明
ossfs2的可执行文件安装在/usr/local/bin/ossfs2路径下，若您的环境变量PATH有特殊配置，可直接通过/usr/local/bin/ossfs2路径访问该程序。
