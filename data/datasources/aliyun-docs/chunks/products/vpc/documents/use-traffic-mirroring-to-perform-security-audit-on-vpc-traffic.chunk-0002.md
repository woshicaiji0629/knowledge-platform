### 步骤一：配置Suricata
您需要在ECS2服务器中部署Suricata，接收网络流量并进行安全审查。
登录ECS2服务器，执行如下命令，安装Suricata。
#安装依赖 sudo dnf install -y gcc libpcap-devel pcre-devel libyaml-devel file-devel \ zlib-devel jansson-devel nss-devel libcap-ng-devel libnet-devel #安装suricata sudo dnf install suricata -y #确保suricata自动启动 sudo systemctl enable suricata sudo systemctl start suricata
配置Suricata。
Suricata的配置存放在/etc/suricata/suricata.yaml，使用默认配置即可。
更新安全规则。
执行suricata-update更新规则文件，默认保存在/var/lib/suricata/rules/suricata.rules。
执行sudo service suricata restart重启Suricata。
