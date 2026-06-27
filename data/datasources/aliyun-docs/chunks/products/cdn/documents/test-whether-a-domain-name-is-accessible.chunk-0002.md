# localhost name resolution is handled within DNS itself. # 127.0.0.1 localhost # ::1 localhost
在文件末尾添加获取到的IP地址和加速域名，例如：
192.168.0.1 example.aliyundoc.com
保存更改。
编辑完成后，选择文件>保存或按Ctrl + S保存更改。
（可选）刷新DNS缓存是为了确保DNS解析的更改立即生效。
打开命令提示符（以管理员身份运行），输入以下命令并按回车：
ipconfig /flushdns
