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
准备加密使用的key_info.txt文件，加密工具会根据该
