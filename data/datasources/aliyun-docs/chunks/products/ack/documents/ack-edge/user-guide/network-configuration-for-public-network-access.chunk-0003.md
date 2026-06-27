.com | TCP 443 | 系统组件镜像需要使用的地址。 |
| 系统工具 | 系统工具在线安装（无需额外域名） net-tools、iproute、chrony（或者 ntpdate）、crontabs、pciutils、socat、ebtables、iptables、conntrack-tools | 不涉及 | 检测待添加节点是否已安装系统工具，如果没有，则会在线安装，具体的访问地址由节点 yum/apt 源配置决定。 如果是 Ubuntu 系统，则采用 apt-get 安装。 如果是 CentOS 系统，则采用 yum 安装。 |
