## macOS/Linux系统
在命令界面内，输入nslookup -type=TXT verification.example.com，根据当前的TXT结果，可以查看解析记录是否生效或正确。
[root@xxx ~]# nslookup -type=TXT verification.xxx Server: xxx Address: xxx Non-authoritative answer: verification.xxx text = "verify_xxx981c5ebff22" Authoritative answers can be found from:
说明
在nslookup命令中，类型是TXT，验证的域名则是将原域名的主机名替换为verification。例如，如果您的加速域名是www.example.com，那么您需要验证的域名则是verification.example.com。
域名首次配置TXT解析记录后将会实时生效，修改TXT解析记录通常会在10分钟后生效（具体生效时间长短取决于域名DNS解析配置的TTL时长，默认为10分钟）。
如果Linux系统没有安装nslookup命令程序，centos系：yum install bind-utils；Ubuntu系：apt-get install dnsutils执行命令自动安装。
文件验证
在验证页面，单击方法2: 文件验证。
按照页面提示完成文件验证：下载验证文件verification.html，将该文件上传至加速域名的站点根目录（确保通过http://example.com/verification.html可正常访问），然后单击点击验证完成域名归属权验证。
单击verification.html，下载验证文件。
手动将验证文件上传到您主域名服务器（例如您的ECS、OSS、CVM、COS、EC2等）的根目录。例如：当前加速域名为www.example.com，您需要将该文件上传至example.com的根目录下。
确保可通过http://example.com/verification.html访问到该文件后，即可点击验证进行验证.
阿里云CDN后台将访问您服务器中http://example.com/verification.html文件链接进行验证。
如果文件内的记录值与验证文件记录值一致，则通过验证。
如果验证失败，请确保上述文件链接可访问，并且您上传的文件正确。
- 配置源站信息
源站是指您运行业务的网站服务器。CDN 缓存未命中时从源站获取资源。
配置源站信息
完成域名业务信息配置后，在源站信息区域单击新增源站信息。
在对话框中，选择源站的类型，并填写源站地址。
根据您源站的实际情况填写端口，默认使用HTTP协议的80端口。
在新增源站信息对话框中，源站信息支持OSS域
