FreeBSD操作系统如何安装云助手Agent？
适用于阿里云ECS实例
#!/bin/sh VERSION=latest use_curl=0 which curl >/dev/null 2>&1 && use_curl=1 if [ $use_curl -eq 1 ];then REGION=$(curl http://100.100.100.200/latest/meta-data/region-id) else REGION=$(wget -O - http://100.100.100.200/latest/meta-data/region-id) fi DOMAIN=aliyun-client-assist-${REGION}.oss-${REGION}-internal.aliyuncs.com PACKAGE=aliyun_assist_${VERSION}.txz PKG_URI="https://$DOMAIN/freebsd/$PACKAGE" if [ $use_curl -eq 1 ];then curl -o $PACKAGE $PKG_URI else wget -O $PACKAGE $PKG_URI fi pkg install -U -y $PACKAGE service aliyun start
适用于托管实例（非阿里云服务器）
#!/bin/sh VERSION=latest DOMAIN=aliyun-client-assist.oss-accelerate.aliyuncs.com PACKAGE=aliyun_assist_${VERSION}.txz PKG_URI="https://$DOMAIN/freebsd/$PACKAGE" use_curl=0 which curl >/dev/null 2>&1 && use_curl=1 if [ $use_curl -eq 1 ];then curl -o $PACKAGE $PKG_URI else wget -O $PACKAGE $PKG_URI fi pkg install -U -y $PACKAGE service aliyun start
托管实例（非阿里云服务器）如何安装云助手Agent？
Linux脚本默认安装最新版本的Agent，安装指定版本请修改VERSION=latest。#!/bin/bash VERSION=latest PACKAGE= PKG_URI= DOMAIN=aliyun-client-assist.oss-accelerate.aliyuncs.com arch=$(uname -m) echo "[main] arch = ${arch}" # 检测是否为 openSUSE 或 SLES 系统 is_suse_like
