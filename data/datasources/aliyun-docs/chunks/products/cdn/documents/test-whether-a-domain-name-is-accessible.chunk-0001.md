## 操作步骤
获取加速域名的CNAME地址。
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，复制加速域名对应的CNAME地址。
说明
请复制状态为正常运行的CNAME地址。
获取CNAME对应的IP地址。在命令行（CMD，PowerShell或终端）中使用nslookup命令查询CNAME地址，得到IP地址。
说明
以下通过nslookup命令得到的IP地址仅作为参考，实际以nslookup您的真实CNAME地址得到的IP地址为准。
nslookup xxx xxx w.kunlunle.com Server: 100 Address: 100.xxx.xxx.53 Non-authoritative answer: Name: xxx.p.kunlunle.com Address: 117.xxx.214 Name: flaskzx.zhang-xin.top.w.kunlunle.com Address: xxx:e:1:3::3fa
在本地电脑绑定hosts文件。
您需要将步骤2得到的IP地址和加速域名绑定到电脑本地hosts文件中，绑定顺序为IP地址在前，加速域名在后，顺序不能颠倒。
本文以加速域名为example.aliyundoc.com，生成的CNAME地址为example.aliyundoc.com.w.kunlunle.com，nslookup example.aliyundoc.com.w.kunlunle.com得到IP地址为192.168.0.1为例，为您介绍绑定方法。
