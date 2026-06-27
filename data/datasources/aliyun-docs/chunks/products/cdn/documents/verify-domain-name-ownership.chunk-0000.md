## 方法一：DNS解析验证（推荐）
本文以加速域名image.example.com为例，为您介绍如何通过DNS解析验证来验证域名归属权。
在验证页面，单击方法1：DNS解析验证，获取主机记录、记录值。
重要
在验证完成前请不要关闭验证页面。DNS解析验证偶尔会出现验证失败的情况，您还可以尝试使用方法二：文件验证。
在您的域名解析服务商，添加TXT记录。
下文以阿里云的云解析为例介绍如何添加TXT记录，在其他域名解析服务商（例如：腾讯云、新网等）的配置方法类似。
登录[云解析](https://dns.console.aliyun.com)[DNS](https://dns.console.aliyun.com)[控制台](https://dns.console.aliyun.com)。
在公网权威解析页面，找到加速域名的根域名example.com，并单击右侧的解析设置。
单击添加记录，记录类型选择为TXT，填写步骤1中阿里云CDN提供的主机记录、记录值，其余参数保持默认即可。
单击确定，完成添加。
等待TXT解析生效，返回CDN控制台，单击点击验证，完成验证。
如果系统提示“验证失败”，请检查TXT记录是否正确填写，并等待DNS记录生效后重新验证。
以加速域名image.example.com为例，检查TXT记录是否正确方法：
说明
域名首次配置TXT解析记录后将会实时生效，修改TXT解析记录通常会在10分钟后生效（具体生效时间长短取决于域名DNS解析配置的TTL时长，默认为10分钟）。
如果Linux系统没有安装nslookup命令程序，centos系：yum install bind-utilsUbuntu系：apt-get install dnsutils执行命令自动安装。
