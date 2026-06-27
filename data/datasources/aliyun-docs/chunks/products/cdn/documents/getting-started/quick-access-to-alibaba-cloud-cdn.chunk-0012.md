## # Host Database # # localhost is used to configure the loopback interface # when the system is booting. Do not change this entry. ## 127.0.0.1 localhost 255.255.255.255 broadcasthost ::1 localhost
在文件末尾添加获取到的IP地址和加速域名，例如：
192.168.0.1 www.example.com
保存更改并退出。
按Esc键退出插入模式，然后输入:wq按回车，保存文件并退出vim。
（可选）刷新DNS缓存是为了确保DNS解析的更改立即生效。
在终端中输入以下命令并按回车：
sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder
测试加速域名是否访问正常。
成功绑定hosts文件后，您可以打开浏览器，在本地访问加速域名进行连通性测试，测试结果可通过浏览器自带的开发者工具查看。
如果Remote Address的IP和您在hosts文件中绑定的IP一致，表示配置正确，您可以在域名解析服务商处配置CNAME。打开浏览器开发者工具的Network面板，选中加速域名对应的请求条目，在右侧Headers面板的 General 区域中，确认Status Code为200 OK表示连通正常，同时查看Remote Address中显示的 IP 地址。
如果Remote Address的IP和您在hosts文件中绑定的IP不一致，表示配置不正确，您需要检查hosts文件中绑定的IP地址是否正确，确保该IP地址是CNAME地址的IP。
成功访问加速域名后，如果您需要验证其他功能，可在电脑本地进行相应的验证。
