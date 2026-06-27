# 快速接入阿里云CDN-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/getting-started/quick-access-to-alibaba-cloud-cdn

# 快速接入阿里云CDN
本文介绍如何快速接入阿里云CDN，包括添加域名、配置源站、配置CNAME以及推荐的性能优化和安全配置。
说明
本文以www.example.com作为示例中用户访问的域名，10.10.10.1作为示例中域名对应的服务器IP。
## 阿里云CDN是如何帮助加速的
如已了解 CDN 原理，可跳过本节直接开始配置。
阿里云CDN是如何帮助加速的
当我们通过浏览器输入一个URL时，最终会在屏幕上显示一个网页、一段视频、一首音乐或一张图片。这一过程背后涉及了多种软件和硬件的解析与转发操作，实际上相当复杂。接下来，本文将通过一个简单的请求示例，介绍阿里云CDN是如何在这个请求流程中起到加速作用的。
### 一、基本的请求过程
现在，我们希望通过访问www.example.com这一域名获取一张图片。然而，浏览器无法直接通过该域名定位到图片所在服务器的地址。在这种情况下，浏览器首先需要访问DNS服务器，以获取与该域名对应的IP地址10.10.10.1。接着，浏览器将通过该IP地址找到相应的服务器，最终从服务器中获取所需的图片。
说明
域名可以比作一个人的名字，而IP则可视为一个人的地址。当我们希望找到某个个体时，需通过其名字获取相应的地址，进而通过该地址找到此人。网络请求的过程与此场景高度相似。
DNS服务器可以理解为一个存储域名和IP映射关系的大型数据库。更多关于DNS服务器和域名的信息，敬请参考[DNS](https://help.aliyun.com/zh/dns/basic-concepts)[基本概念](https://help.aliyun.com/zh/dns/basic-concepts)。
### 二、引入阿里云CDN的请求过程
随着越来越多的用户通过www.example.com这一域名访问图片，访问请求的数据量不断增加。受服务器性能和网络条件限制，访问速度可能变慢。此时，阿里云CDN可以有效加速请求。
CDN 部署在服务器和用户之间。请求到达 CDN 节点时，优先返回缓存；如无缓存，从源站获取并缓存，加速后续请求。
说明
加速请求的访问速度只是阿里云CDN的基础功能，更多关于阿里云CDN的介绍和高阶功能，请见[什么是阿里云](../product-overview/what-is-alibaba-cloud-cdn.md)[CDN](../product-overview/what-is-alibaba-cloud-cdn.md)。
阿里云CDN在目标服务器的架构之外进行加速，对目标服务器不会产生任何侵入，也无需修改任何业务代码。
正常的请求流程远比上述流程复杂，此处为了方便用户理解阿里云CDN的工作原理，简化了大部分的细节。
## 快速接入阿里云CDN
只需完成以下配置即可实现内容加速。如果您更倾向于视频学习，也可以直接观看我们的[快速入门](../videos/quick-start.md)，跟随步骤一步步完成配置。
说明
在正式开始接入阿里云CDN之前，需要先完成以下两个步骤：
您需要拥有一个阿里云账号并完成[实名认证](https://account.console.aliyun.com/#/auth/home)，如果您尚未注册阿里云账号，可以通过[账号注册](https://account.aliyun.com/register/register.htm)页面完成注册。
在阿里云账号中[开通](../activate-alibaba-cloud-cdn.md)[CDN](../activate-alibaba-cloud-cdn.md)[服务](../activate-alibaba-cloud-cdn.md)。
### 一、添加域名和源站
- 配置域名
为了使您的域名享受到加速服务，需要将您的域名作为加速域名配置在阿里云CDN里。只有完成这一步骤，阿里云CDN才能识别并加速您配置的域名。
添加域名
[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)
在左侧导航栏，单击域名管理。
单击添加域名，配置加速区域、加速域名和业务类型，其他参数均可保持默认。
说明
加速域名是指接入阿里云CDN、用于加速的网站域名或资源域名，也是终端用户实际访问的域名。在上述示例的场景下，此处填写www.example.com。
www.example.com和example.com是两个不同的域名，CDN需要分别添加为加速域名。如果您同时需要加速这两个域名，需在CDN控制台中分别添加www.example.com和example.com，并分别完成CNAME配置。不能将裸域名的CNAME直接解析到带www域名的CDN CNAME地址。
加速区域请根据[加速区域](../user-guide/change-the-accelerated-region.md)的描述，选择合适自身业务的区域，本次演示选择仅中国内地作为加速区域。当加速区域包含中国内地时，域名必须进行[ICP](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/icp-filing-application-overview)[备案](https://help.aliyun.com/zh/icp-filing/basic-icp-service/user-guide/icp-filing-application-overview)，否则域名无法正常访问。
业务类型根据[应用场景](../product-overview/scenarios.md)的描述，选择适合您自身业务的场景，本次演示选择图片小文件。
当加速区域为全球（不包含中国内地）时，可以开启全球资源计划。开启后，您的域名可以享受更丰富的节点资源，但是支持的功能会受到限制，请查看[开启全球资源计划后支持的配置功能](../user-guide/configure-global-resource-planning.md)，谨慎评估之后使用。
- Q：配置CDN统一加速域名时有哪些注意事项？
配置统一加速域名时，请注意以下事项：
业务类型选择：建议选择「图片小文件」，以适配静态资源的加速场景。
共享缓存：若多个加速域名的源站内容完全一致，可开启共享缓存功能，提升缓存命中率。
HTTPS支持：如需支持HTTPS访问，需为每个加速域名单独配置SSL证书。
回源HOST设置：回源HOST建议设置为对应的实际源站域名，避免因HOST不匹配导致回源资源混淆。
域名添加规则：客户端访问几个网站域名，就需要在CDN中添加几个加速域名，无法通过单个加速域名代替多个网站域名，每个域名都需要单独添加。例如，www.example.com和example.com属于两个不同的域名，需分别在CDN控制台添加为加速域名并各自配置CNAME解析。
- 验证域名归属权
为了确保您添加的域名确实归您所有，阿里云CDN需要进行域名归属权验证。如果您之前已经完成过该验证或未收到验证提示，可以跳过此步骤。
验证域名归属权
重要
在验证完成之前请不要关闭验证页签。
DNS解析验证（推荐）
在添加域名页面的验证页签，单击方法1：DNS解析验证，获取主机值、记录值。
前往DNS服务商，添加一条TXT类型的解析记录，主机记录为verification，记录值为页面显示的验证值。配置完成后，选择已配置并单击点击验证完成域名归属权验证。
在您的域名解析服务商处，添加TXT记录。以下以阿里云的云解析为例介绍TXT记录的添加方法，其他域名解析服务商（例如：腾讯云、新网等）的配置方法类似。
配置TXT记录
登录[云解析](https://dnsnext.console.aliyun.com/authoritative)[DNS](https://dnsnext.console.aliyun.com/authoritative)[控制台](https://dnsnext.console.aliyun.com/authoritative)。
在公网权威解析页面，找到加速域名的主域名example.com，并单击右侧的解析设置。
单击添加记录，记录类型选择为TXT，填写步骤1中阿里云CDN提供的主机记录、记录值，其余参数保持为默认填写即可。
单击确定，完成添加。
说明
您可以参考[域名基本概念](https://help.aliyun.com/zh/dns/basic-concepts)，快速了解主域名和子域名的相关定义与区别。
等待TXT解析生效，返回CDN控制台的验证页签，单击点击验证，完成验证。
如果系统提示“验证失败”，请检查TXT记录的填写是否正确，并在DNS记录生效后重新进行验证。
检查TXT记录是否生效
以加速域名www.example.com为例，检查TXT记录是否生效或正确的方法如下：
## Windows系统
在系统内打开cmd命令界面，输入nslookup -type=TXT verification.example.com，根据当前的TXT结果，可以查看解析记录是否生效或正确。
命令执行后，返回示例如以下所示。
C:\Users\xxx> nslookup -type=TXT verification.xxx 服务器: UnKnown Address: fd00:1::1 DNS request timed out. timeout was 2 seconds. 非权威应答: verification.xxx text = "verify_0xxx...xxxff22"
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
在新增源站信息对话框中，源站信息支持OSS域名、IP、源站域名、函数计算域名四种类型。优先级取值范围0~127，主源站优先级为20，备源站优先级为30。权重取值范围1~100。端口还支持HTTPS默认443端口及自定义端口（范围1~65535），填写完成后单击确定。
说明
本示例以10.10.10.1作为源站服务器的IP来[配置源站](../user-guide/configure-an-origin-server.md)。
如果您要加速OSS的资源，源站信息请选择OSS域名；
如果您要加速的资源部署在ECS，源站信息请选择IP，IP请填写ECS服务器的公网IP。
如果您要加速的资源在服务器上并且不能使用IP访问，源站信息请选择源站域名，域名填写源站服务器的域名。但请注意，源站域名不能和加速域名相同，否则会造成循环解析。
如果您要加速的资源是阿里云的函数计算，源站信息请选函数计算域名，区域和域名根据您账号的函数计算资源进行选择。
如果您的源站上托管了多个网站，还需要配置[指定源站回源](../user-guide/specify-an-origin-host-for-each-origin.md)[HOST](../user-guide/specify-an-origin-host-for-each-origin.md)。
更多关于源站配置项的说明，请见[配置源站](../user-guide/configure-an-origin-server.md)。
关于CDN与OSS的最佳实践，请见[CDN 加速 OSS 资源](../use-cases/accelerate-the-retrieval-of-resources-from-an-oss-bucket-in-the-alibaba-cloud-cdn-console.md)。
- 验证加速域名
成功添加加速域名后，为保证DNS解析可以顺利切换而不影响现有业务，建议您先在本地测试加速域名，验证加速域名访问正常后，再将加速域名的DNS解析记录指向CNAME域名。
说明
模拟访问会产生正常的CDN费用。详细信息，请参见[计费组成](../product-overview/billing-overview.md)。
验证加速域名
获取加速域名的CNAME地址。
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，复制加速域名对应的CNAME地址。
说明
请复制状态为正常运行的CNAME地址。
在域名管理页面的域名列表中，CNAME列显示了对应的 CNAME 地址（格式类似xxx.alikunlun.com）。
获取CNAME对应的IP地址。在命令行（CMD，PowerShell或终端）中使用nslookup命令查询CNAME地址，得到IP地址。例如：
nslookup www.example.com.w.kunlunle.comnslookup xxx w.kunlunle.com Server: 100 Address: 100.xxx.xxx53 Non-authoritative answer: Name: xxx.p.kunlunle.com Address: 117.xxx.214 Name: flaskzx.zhang-xin.top.w.kunlunle.com Address: xxx:e:1:3::3fa
在本地电脑绑定hosts文件。
您需要将步骤2得到的IP地址和加速域名绑定到电脑本地hosts文件中，绑定顺序为IP地址在前，加速域名在后，顺序不能颠倒。接下来将以IP地址为192.168.0.1为例，为您介绍绑定方法。
## Windows系统
进入路径C:\Windows\System32\drivers\etc，使用记事本以管理员身份打开hosts文件。
编辑hosts文件。文件内容可能类似如下：
# localhost name resolution is handled within DNS itself. # 127.0.0.1 localhost # ::1 localhost
在文件末尾添加获取到的IP地址和加速域名，例如：
192.168.0.1 www.example.com
保存更改。编辑完成后，选择文件>保存或按Ctrl + S保存更改。
（可选）刷新DNS缓存是为了确保DNS解析的更改立即生效。
打开命令提示符（以管理员身份运行），输入以下命令并按回车：
ipconfig /flushdns
## macOS系统
打开Terminal终端，使用以下命令以管理员权限打开hosts文件。
sudo vim /etc/hosts
编辑hosts文件。文件内容可能类似如下：
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
### 二、推荐配置
完成域名和源站的配置之后，点击下一步即可进入推荐配置页面。
推荐配置中提供了提升缓存命中率、提升访问性能、防止费用超额、提升访问安全四种配置，快速提升CDN的缓存命中率、访问性能以及安全性。
您可以根据自身业务配置合适的功能，或者跳过，后续在域名管理页的操作栏点击快捷配置再次进入。
提升缓存命中率
缓存过期时间
配置缓存规则，减少回源请求。规则按顺序匹配，首个命中的规则生效。请根据资源的特性[配置合理的缓存过期时间](../user-guide/configure-the-cdn-cache-expiration-time.md)。以添加文件后缀名类型为例，参考推荐配置：
| 文件类型 | 文件后缀名 | 过期时间 | 说明 |
| --- | --- | --- | --- |
| 图片/音视频 | jpg,png,gif,mp3,mp4 | 30 天 | 资源内容不经常变更 |
| 静态脚本 | js,css | 1 小时 | 可能随版本发布而频繁变更 |
| 网站首页 | html | 不缓存（0 秒） | 确保用户始终获取最新页面结构 |
忽略参数
开启[忽略参数](../user-guide/ignore-parameters.md)功能后，CDN节点在生成缓存hashkey时会去除URL中?之后的参数，这样客户端在携带不同的参数访问同一个资源文件时，能够命中同一个缓存文件，有助于提高缓存命中率，减少回源流量。
在忽略参数配置弹窗中，选择模式为保留指定参数或删除指定参数，将忽略参数设置为是，在保留指定参数输入框中输入需要保留的参数（最多10个，使用半角逗号分隔）。开启保留回源参数后回源保留所有参数，未开启时回源携带的参数与缓存hashkey的参数一致。单击确定完成配置。
提升访问性能
Range回源
[Range](../user-guide/object-chunking.md)[回源](../user-guide/object-chunking.md)可针对大文件仅回源未缓存的字节范围，避免重复传输完整文件。
如果客户端配置了Range回源参数，选择跟随客户端Range请求，图片推荐 512KB 分片，视频或大文件根据大小选择 1MB、2MB 或 4MB 分片。
如果加速的资源为视频或大文件，选择开启Range回源（大文件场景推荐配置），根据文件大小选择 1MB、2MB 或 4MB 分片。CDN 节点所有回源请求均按指定分片大小发起。
Gzip压缩
加速文件大小在1 KB~10 MB及之间时，可以使用Gzip压缩来降低传输数据量。
该功能不压缩1 KB以下和10 MB以上大小的文件。常见的图片类型文件和视频类型文件已自带压缩，开启 Gzip 无效。开启该功能之前，请仔细阅读[Gzip](../user-guide/use-the-gzip-compression-feature.md)[压缩](../user-guide/use-the-gzip-compression-feature.md)的注意事项。
打开Gzip压缩开关。若源站文件自身有md5值校验机制，请勿开启此功能。
防止费用超额
为防止域名被攻击或盗刷产生突发高带宽，导致产生高额账单，可通过配置用量封顶，控制用户访问该域名的带宽、流量、HTTPS请求数上限值。详细信息可以参考[配置用量封顶](../user-guide/configure-usage-cap.md)。
重要
触发规则之后，加速域名将会被暂时下线，下线期间域名将无法访问。如果您希望在用量超过阈值以后只发送告警通知，可以[设置流量监控告警](../user-guide/set-an-alert-rule.md)。
请根据网站的历史流量、历史带宽和历史HTTPS请求数来设置阈值。如果不清楚网站的流量、带宽和HTTPS请求数信息，您可以先行跳过该配置，待系统稳定运行之后，使用CDN的[用量查询](../user-guide/query-resource-usage-1.md)查看加速域名的用量信息，然后再来[配置用量封顶](../user-guide/configure-usage-cap.md)。
流量封顶
如果计费方式是默认的按流量计费，推荐配置该功能。可以根据历史流量来设置阈值，系统会统计域名在指定周期内产生的总流量。当累计流量超过您设定的阈值时，将触发封顶规则，下线域名，当到达解封时间后，重新上线加速域名。
带宽封顶
如果计费方式是按带宽峰值计费，推荐配置该功能，能有效控制计费带宽的上限。当系统实时监控到的带宽值超过您设定的阈值时，将触发封顶规则，下线域名，当到达解封时间后，重新上线加速域名。
HTTPS请求数封顶
如果加速域名需要开启HTTPS访问，并且对HTTPS请求量有明确预算控制，推荐配置该功能。当加速累计请求数超过您设定的阈值时，将触发封顶规则，下线域名，当到达解封时间后，重新上线加速域名。
提升访问安全
HTTPS证书
如域名需要 HTTPS 访问，请配置证书，否则 HTTPS 不可用。
不需要 HTTPS 时可跳过。
重要
开启HTTPS将产生HTTPS请求数，静态HTTPS请求数每月前500万次免费，超过500万次后，开始计费。HTTPS请求数计费不能使用CDN流量包抵扣，请确保您的账户余额充足，或购买HTTPS请求包，避免欠费导致CDN停止服务。详情请见[静态](../product-overview/billing-of-https-requests-for-static-content.md)[HTTPS](../product-overview/billing-of-https-requests-for-static-content.md)[请求数](../product-overview/billing-of-https-requests-for-static-content.md)。
已在阿里云数字证书管理服务中购买了证书，请选择云盾（SSL）证书中心，并在证书名称中选择已购买的证书，如果无法选择您购买的证书，请检查已购买证书绑定的域名和加速域名是否相同。
使用的是第三方服务商签发的证书，请选择自定义上传（证书+私钥），您需要在设置证书名称后，上传证书（公钥）和私钥，该证书将在阿里云数字证书管理服务中保存。您可以在[我的证书](https://yundun.console.aliyun.com/?spm=5176.2020520110.all.12.16df56a1u1IhI6&p=cas#/cas/home)中查看。
Referer黑/白名单
Referer黑/白名单基于HTTP请求头中的Referer字段，通过设置黑名单/白名单来控制访问，防止资源盗用。黑白名单互斥。详情可以参考[配置](../user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)[Referer](../user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)[黑/白名单](../user-guide/configure-a-referer-whitelist-or-blacklist-to-enable-hotlink-protection.md)。
说明
您可以提前打开[定制和订阅运营报表](../user-guide/customize-an-operations-report-template-and-create-a-tracking-task.md)功能，运营报表会统计并展示用户访问的PV/UV、地区和运营商、域名排行、热门Referer、热门URL、回源热门URL和Top客户端IP等内容。然后根据热门Referer再来配置Referer黑/白名单。
### Q：CDN回源OSS图片场景下，快捷配置中防流量盗刷与限制带宽的具体配置方法是什么？
针对CDN回源OSS图片的场景，您可以通过以下快捷配置来防范流量盗刷和控制带宽费用：
防流量盗刷：在快捷配置的「提升访问安全」模块中，配置Referer防盗链（设置白名单仅允许您的域名访问）或IP黑名单（封禁恶意IP），防止资源被非法盗用。
限制带宽：在快捷配置的「防止费用超额」模块中设置阈值，当实际带宽超过该值时将触发封顶规则，下线该加速域名以有效控制流量和费用风险。到达解封时间后，域名将自动重新上线。
### 三、配置CNAME
配置 CNAME 将域名解析指向最近的 CDN 节点，使用户请求通过 CDN 加速。
CNAME记录是一种DNS记录类型，用于将一个域名指向另一个域名，更多关于CNAME的介绍，敬请参考[CNAME](../what-is-a-dns-cname-record.md)[记录简介](../what-is-a-dns-cname-record.md)。
在DNS服务中配置CNAME
前往阿里云CDN控制台的[域名管理列表](https://cdn.console.aliyun.com/domain/list)，找到之前添加的域名，复制域名对应的CNAME值（如果此处值为空，请稍等五秒之后刷新重试）。
在DNS服务器中配置CNAME记录。不同DNS服务商配置CNAME域名解析的方法不同，请以实际情况为准。本文以阿里云和腾讯云为例。
### 阿里云配置CNAME方法
如果您的DNS服务商是阿里云，您可以根据以下步骤完成CNAME配置。
使用加速域名所在的阿里云账号，登录[云解析](https://dns.console.aliyun.com)[DNS](https://dns.console.aliyun.com)[控制台](https://dns.console.aliyun.com)
在公网权威解析页面，找到加速域名的主域名example.com，并单击右侧的解析设置。
单击添加记录，添加CNAME记录。
记录类型选择CNAME。
主机记录输入www，解析请求来源选择默认，记录值输入CNAME地址（例如www.example.com.w.kunlun.com），TTL保持默认10分钟，然后单击确定。
重要
主机记录就是域名的前缀。www.example.com的主机记录是www；如果您的加速域名就是主域名example.com，那么对应的主机记录填写@。
对于同一个主机名，CNAME记录和A记录是相互冲突，只能有一个存在。如果您要加速的域名存在相同主机记录的A记录，需要将A记录暂停或删除，才能配置CNAME记录。
暂停A记录，配置CNAME的时候，会导致域名短暂的不可访问，为减少对您域名的影响，请根据您日常流量的变化情况，在合适的时间进行配置。
单击确认，完成添加。
### 腾讯云配置CNAME方法
如果您的DNS服务商是腾讯云，您可以根据以下步骤完成CNAME配置。
登录DNSPod控制台。
在对应域名的域名解析页，单击添加记录，添加CNAME记录。
| 参数 | 说明 | 填写样例 |
| --- | --- | --- |
| 主机记录 | 加速域名为子域名的情况下，主机记录为子域名的前缀。 加速域名为泛域名的情况下，主机记录为 * 。 加速域名为根域名自身时，主机记录为 @ 。 | 子域名示例： 加速域名为 www.example.com ，主机记录为 www 。 加速域名为 www.example.aliyundoc.com ，主机记录为 www.example 。 泛域名示例： 加速域名为 .example.com ，主机记录为 * 。 加速域名为 *.example.aliyundoc.com ，主机记录为 *.example 。 根域名示例：根域名为 example.com 且配置加速域名为 example.com 时，主机记录填写 @ 。 说明 域名解析设置是针对您注册的域名（如 example.com ）或域名的左侧部分进行解析设置。配置主机记录时，您仅需要填写要解析的部分（如解析 www.example.com 时填写 www ）。 |
| 记录类型 | 选择 CNAME。 | CNAME |
| 线路类型 | 选择“默认”类型。 | 推荐保持默认 |
| 记录值 | 输入加速域名对应的 CNAME 记录值。 说明 一级域名（如 www.example.com ）和二级域名（如 www.example.aliyundoc.com ）对应的 CNAME 值不同。如果您要加速二级域名，需要将二级域名也添加到 CDN 上并解析到对应的 CNAME 记录值，或者在 CDN 上添加泛域名，泛域名的 CNAME 可以被二级域名使用。添加泛域名或二级域名，请参见 [添加加速域名](../add-a-domain-name.md) 。 | www.example.com.w.kunlunsl.com |
| 权重 | 无需填写。 | 不涉及 |
| MX | 无需填写。 | 不涉及 |
| TTL | TTL 为缓存时间，数值越小，修改记录后各地生效时间越快。 | 推荐保持默认 |
单击保存，完成添加。
验证配置的CNAME是否生效。
## CNAME状态
前往阿里云CDN控制台的[域名管理列表](https://cdn.console.aliyun.com/domain/list)。
选择目标域名，将鼠标指向加速域名的CNAME状态处，状态为已配置时，则表示CNAME配置已生效。
说明
在配置CNAME之后，控制台中CNAME状态可能仍会显示待配置，请刷新页面或等5分钟再来验证。
## 通过nslookup命令验证
打开cmd程序（Windows）、终端（macOS/Linux）。
输入nslookup -type=CNAME加速域名（例如nslookup -type CNAME www.example.com），如果返回的解析结果和CDN控制台上该加速域名的CNAME值一致，则表示配置的CNAME已经生效。
~ % nslookup -type=CNAME www.example.com Server: 30.30.30.xxx Address: 30.30.30.xxx Non-authoritative answer: www.example.com canonical name = www.example.com.w.kunlun.com. Authoritative answers can be found from:
### 四、资源预热
首次接入CDN后，可选择将热点静态资源提前预热至CDN节点。用户访问时可直接由CDN节点响应，提升初次访问速度。
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击刷新预热。
在刷新缓存/预热缓存页签，选择操作类型为预热。
在预热内容输入框中，输入需要预热的完整文件 URL，每行一个。不支持预热目录。例如：https://www.example.com/install/package.zip。
单击提交，系统将开始执行预热任务。
在操作记录页签中查看资源刷新或预热的详细记录和进度。进度为100%，表示任务执行完成。
说明
刷预热任务一旦提交成功，将无法中止。
预热任务的完成时间取决于文件大小、数量和源站性能，通常需要 5-30 分钟。
### 五、验证阿里云CDN缓存是否生效
验证阿里云CDN缓存是否生效
Windows系统 ：按下Windows键+R键，在弹出的运行输入框里，输入cmd，点击确定，打开cmd命令行。
macOS系统 ：打开“终端”。
在窗口中输入 "curl -I" + 加速域名资源，例如curl -I www.example.com/10.JPG。
norman@Norman ~ % curl -I http://xxx/public/picture/xueshan.jpg HTTP/1.1 200 OK Server: Tengine Content-Type: image/jpeg Content-Length: 319717 Connection: keep-alive Date: Fri, 07 Feb 2025 06:15:50 GMT x-oss-request-id: 67xxx333314984F6 Vary: Origin x-oss-cdn-auth: success Accept-Ranges: bytes ETag: "F641480662xxx1E55F6C851AF" Last-Modified: Thu, 14 Nov 2024 01:42:56 GMT x-oss-object-type: Normal x-oss-hash-crc64ecma: 14568304759889530959 x-oss-storage-class: Standard Content-MD5: 9kFIBmLCpOlayx5V9shRrw== x-oss-server-time: 83 Via: cache40.l2cn3160[0,0,200-0,H], cache55.l2cn3160[1,0], kunlun3.cn7174[0,0,200-0,H], kunlun8.cn7174[7,0] Age: 26 Ali-Swift-Global-Savetime: 1738908951 X-Cache: HIT TCP_MEM_HIT dirn:-2:-2 X-Swift-SaveTime: Fri, 07 Feb 2025 06:16:08 GMT X-Swift-CacheTime: 2591983 Timing-Allow-Origin: * EagleId: b4a3921c17389089757582374e
当响应头结果中有Age、X-Cache、X-Swift-SaveTime、X-Swift-CacheTime时，证明阿里云CDN已经生效。
说明
X-Cache：字段为MISS，则表示未命中缓存，需要进行回源处理；X-Cache字段为HIT，则表示命中了CDN缓存，会直接读取缓存数据。
Age: 表示文件在CDN节点上缓存的时间（秒）。文件被刷新或首次访问无此字段。Age为0表示缓存过期，需回源校验。
X-Swift-SaveTime：表示资源首次被缓存到CDN节点上的时间（GMT）。转换为中国北京时间需加上8小时。
X-Swift-CacheTime：字段值表示CDN节点上的允许缓存时间，即该文件可以在CDN节点上缓存多久。如果是0，则表示该请求无法缓存。
说明
如果您按照上述流程配置完成之后，仍然出现无法访问或访问异常，请见[无法访问/访问异常排查](../support/faq.md)。
至此，阿里云CDN的主要配置已完成，您的网站现在可以通过阿里云CDN实现访问加速。
## 参考文档
[阿里云](../support/faq.md)[CDN](../support/faq.md)[常见问题排查](../support/faq.md)
[什么是阿里云](../product-overview/what-is-alibaba-cloud-cdn.md)[CDN](../product-overview/what-is-alibaba-cloud-cdn.md)
[阿里云](../product-overview/competitive-advantages-of-alibaba-cloud-cdn.md)[CDN](../product-overview/competitive-advantages-of-alibaba-cloud-cdn.md)[的五大竞争力](../product-overview/competitive-advantages-of-alibaba-cloud-cdn.md)
[CDN](../use-cases/best-practices-for-preventing-traffic-theft.md)[防范流量盗刷最佳实践](../use-cases/best-practices-for-preventing-traffic-theft.md)
[提高](../use-cases/increase-the-cache-hit-ratios-of-alibaba-cloud-cdn.md)[CDN](../use-cases/increase-the-cache-hit-ratios-of-alibaba-cloud-cdn.md)[缓存命中率](../use-cases/increase-the-cache-hit-ratios-of-alibaba-cloud-cdn.md)
[客户案例](../product-overview/customer-use-cases.md)
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
