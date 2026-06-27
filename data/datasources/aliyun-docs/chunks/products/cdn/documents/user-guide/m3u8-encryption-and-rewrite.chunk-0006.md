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
