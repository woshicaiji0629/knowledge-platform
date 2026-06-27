# 如何配置M3U8标准加密改写-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/m3u8-encryption-and-rewrite

# 配置M3U8标准加密改写
当客户端请求 M3U8 文件时，系统会将其携带的鉴权参数自动追加到 #EXT-X-KEY 标签中的密钥 URI 后。无需源站改造，即可实现密钥访问的安全控制，有效防止视频内容被盗播。
## 适用场景
在标准的 HLS 加密流程中，#EXT-X-KEY标签指明了获取解密密钥的 URI。如果此 URI 是一个固定的、无保护的公开地址，任何获取到 M3U8 文件的人都可以下载密钥，从而解密视频内容，导致视频加密失效。
为解决此问题，此功能为每次密钥请求附加一个动态、可验证的鉴权凭证，适用于需要对 HLS 加密视频的密钥进行访问控制的场景，例如：
付费视频/在线教育：为防止学员将 M3U8 地址分享给非付费用户，通过为每个登录用户生成唯一的鉴权参数，确保只有合法用户才能在有效期内获取到解密密钥。
直播版权保护：在大型体育赛事或活动直播中，通过动态生成的鉴权参数与 CDN 的 URL 鉴权功能结合，实现对直播流的精细化访问控制，有效防止盗链。
## 技术原理
客户端请求业务服务器，业务服务器根据业务逻辑（如用户登录）生成一个带有时效性和签名的鉴权参数（例如token=xxxx），并将其返回给客户端。
客户端使用这个鉴权参数，将其拼接在请求M3U8文件的URL末尾，然后向 CDN 节点发起 M3U8 文件请求。
CDN 节点在向客户端返回 M3U8 文件前，解析 M3U8 文件内容，找到#EXT-X-KEY标签，并将客户端请求 URL 中的鉴权参数追加到其URI属性的末尾。
客户端获取 CDN 返回的、已被改写的 M3U8 文件，并根据其中新的密钥 URI（已包含鉴权参数）向密钥服务器发起请求。
密钥服务器收到密钥请求，提取并校验 URL 中的鉴权参数。校验通过后，返回解密密钥；校验失败，则拒绝请求。
客户端获取密钥后，解密 TS 视频流并播放。
重要
此功能不负责对视频内容进行加密。使用此功能前，必须在源站确保视频切片（TS 文件）已完成 HLS 标准加密（如 AES-128），且原始 M3U8 文件中已包含正确的#EXT-X-KEY标签。视频加密请参考[如何生成](m3u8-encryption-and-rewrite.md)[M3U8](m3u8-encryption-and-rewrite.md)[文件并加密](m3u8-encryption-and-rewrite.md)。
引入业务服务器和密钥服务器是为了更好的介绍M3U8标准加密改写的作用，此功能不负责业务服务器和密钥服务器的实现。您需要自己实现业务服务器和密钥服务器的功能，以便完成整个HLS密钥鉴权的流程。
#EXT-X-KEY标签的作用是声明是否加密。更多关于M3U8文件标签的介绍请参见[M3U8](m3u8-encryption-and-rewrite.md)[标签简介](m3u8-encryption-and-rewrite.md)。
## 操作步骤
登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。
在左侧导航栏，单击域名管理。
在域名管理页面，找到目标域名，单击操作列的管理。
在指定域名的左侧导航栏，单击视频相关。
在M3U8标准加密改写区域，打开M3U8标准加密改写开关。
说明
开启M3U8标准加密改写功能后，默认的参数名为MtsHlsUriToken。
可选：如果您需要配合您的客户端修改参数名，请执行以下操作步骤。
单击自定义参数名对应的修改。
在自定义参数名对话框，设置参数名。
若不填写，参数名默认为MtsHlsUriToken。
说明
参数名大小写敏感，请确保设置的参数名和客户端请求携带的参数名完全一致。例如客户端请求携带MtsHlsUriToken参数，如果在CDN控制台设置自定义参数名为mtshlsuritoken将不生效。
单击确定，完成配置。
## 演示示例
在浏览器中访问经过CDN加速的M3U8文件，并在请求最后加上MtsHlsUriToken=tokenxxxxx。例如：http://<CDN 加速域名>/video.m3u8?MtsHlsUriToken=tokenxxxxx
通过Chrome浏览器开发者工具，在Network（网络）面板，可以看到请求M3U8文件是带上了自定义参数，但是请求密钥地址时没有携带该参数。
在CDN控制台开启M3U8标准加密改写，如果需要，可以设置自定义参数名（本次演示中使用默认参数MtsHlsUriToken）。在CDN控制台开启M3U8标准加密改写功能，自定义参数名设置为MtsHlsUriToken。
重复步骤1，在浏览器中访问经过CDN加速的M3U8文件，并在请求最后加上MtsHlsUriToken=tokenxxxxx。
通过浏览器开发者工具，在Network（网络）面板，可以看到在请求密钥地址时，带上了自定义的参数。
密钥文件encryption_key.key的请求 URL 中已附带MtsHlsUriToken=tokenxxxxx参数，返回状态码为 206，Content-Length 为 16 字节。
## 常见问题
什么是HLS协议？
HLS（HTTP Live Streaming的缩写）是一个由苹果公司提出的基于HTTP的流媒体网络传输协议。HLS协议基于HTTP协议，客户端按照顺序使用HTTP协议下载存储在服务器上的文件。HLS协议规定，视频的封装格式是TS（Transport Stream），除了TS视频文件本身，还定义了用来控制播放的M3U8文件（文本文件）。HLS协议的工作原理是把整个视频流分割成一个个小的TS格式视频文件来传输，在开始一个流媒体会话时，客户端会先下载一个包含TS文件URL地址的M3U8文件（相当于一个播放列表），给客户端用于下载TS文件。
HLS协议的M3U8文件里都有什么？
M3U8文件的基本字段：
#EXTM3U：M3U8文件头，必须放在第一行。
EXT-X-MEDIA-SEQUENCE：第一个TS分片的序列号，一般情况下是0，但是在直播场景下，这个序列号标识直播段的起始位置；#EXT-X-MEDIA-SEQUENCE:0。
#EXT-X-TARGETDURATION：每个分片TS的最大的时长；#EXT-X-TARGETDURATION:10，表示每个分片的最大时长是10秒。
#EXT-X-ALLOW-CACHE：是否允许cache，#EXT-X-ALLOW-CACHE:YES、#EXT-X-ALLOW-CACHE:NO，默认情况下是YES。
#EXT-X-ENDLIST：M3U8文件结束符。
#EXTINF：extra info，分片TS的信息，如时长，带宽等；一般情况下是#EXTINF:<duration>,[<title>]后面可以跟其他的信息，逗号之前是当前分片的TS时长。分片时长要小于#EXT-X-TARGETDURATION定义的值。
#EXT-X-VERSION：M3U8版本号。
#EXT-X-DISCONTINUITY：该标签表明其前一个切片与下一个切片之间存在中断。
#EXT-X-PLAYLIST-TYPE：表明流媒体类型。
#EXT-X-KEY：是否加密解析。例如：#EXT-X-KEY:METHOD=AES-128,URI="https://example.com/video.key?token=xxx"加密算法是AES-128，密钥通过请求https://example.com/video.key?token=xxx来获取，密钥请求回来以后存储在本地，并用于解密后续下载的TS视频文件。
如何生成M3U8文件并加密？
生成加密密钥。
这个密钥通常是一个16字节的随机字符串（对于AES-128加密）。可以使用 OpenSSL 工具用以下命令来生成包含16个随机字节的密钥。
openssl rand 16 > encryption_key.key
准备加密使用的key_info.txt文件，加密工具会根据该文件对HLS协议的视频文件进行加密。
https://example.com/encryption_key.key /path/to/local/encryption_key.key
第一行是步骤1生成的加密密钥的URL。推荐将该文件放置在CDN加速的OSS源站中，然后使用CDN加速域名来访问该文件。
第二行是本地密钥文件的绝对路径。
使用FFmpeg工具生成并加密HLS协议的视频文件。
ffmpeg -i input_video.mp4 -c:v copy -c:a copy -hls_time 10 -hls_key_info_file key_info.txt -hls_list_size 0 output_playlist.m3u8
-i input_video.mp4：指定需要转换的视频文件，例如，MP4格式视频。
-c:v copy: 视频流不重新编码，直接复制。
-c:a copy: 音频流不重新编码，直接复制。
-hls_time 10: 每个TS文件的时长为 10 秒，可以根据原始视频时长修改该设置。
-hls_key_info_file key_info.txt: 指定包含加密密钥信息的文件。
-hls_list_size 0：设置M3U8文件中保留的TS文件索引数量，0表示保留所有.ts文件索引。
output_playlist.m3u8: 输出的 HLS 播放列表文件名称（即M3U8文件名称）。
将加密后的TS文件和M3U8文件保存到服务器中（推荐使用CDN加速的OSS源站）。然后在浏览器中使用CDN加速域名访问M3U8文件，即可实现加密播放HLS协议的视频。
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
