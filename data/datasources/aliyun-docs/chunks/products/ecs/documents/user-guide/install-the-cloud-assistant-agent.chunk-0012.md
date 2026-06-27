else PACKAGE="aliyun-assist_${VERSION}-1_arm64.deb" fi PKG_URI="https://$DOMAIN/arm/$PACKAGE" ;; esac echo "[main] package = ${PACKAGE}" echo "[main] pkg_uri = ${PKG_URI}" if command -v wget; then sudo wget -O "${PACKAGE}" "${PKG_URI}" elif command -v curl; then sudo curl -o "${PACKAGE}" "${PKG_URI}" else echo "[WARN] command wget/curl not found, exit" exit 1 fi if command -v rpm && ! command -v dpkg; then sudo rpm -ivh --force "${PACKAGE}" elif command -v dpkg; then sudo dpkg -i "${PACKAGE}" else echo "[WARN] command rpm/dpkg not found, exit" exit 2 fi if [[ -e /etc/redhat-release ]]; then if sudo systemctl status qemu-guest-agent; then sudo systemctl stop qemu-guest-agent sudo systemctl disable qemu-guest-agent sudo systemctl restart aliyun.service fi fi
Windows方法一：通过浏览器打开网址下载云助手Agent。
在浏览器中打开网址下载云助手Agent。
https://aliyun-client-assist.oss-accelerate.aliyuncs.com/windows/aliyun_agent_latest_setup.exe
安装云助手Agent。
双击云助手Agent文件，根据安装向导完成安装。默认安装路径为C:\ProgramData\aliyun\assist\。
方法二：通过PowerShell安装并启动云助手Agentcurl -UseBasicParsing -Uri https://aliyun-client-assist.oss-accelerate.aliyuncs.com/windows/aliyun_agent_latest_setup.exe -OutFile 'C:\\aliyun_agent_latest_setup.exe' ;"C:\\aliyun_a
