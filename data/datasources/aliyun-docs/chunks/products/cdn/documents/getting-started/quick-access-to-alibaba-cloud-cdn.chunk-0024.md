### 五、验证阿里云CDN缓存是否生效
验证阿里云CDN缓存是否生效
Windows系统 ：按下Windows键+R键，在弹出的运行输入框里，输入cmd，点击确定，打开cmd命令行。
macOS系统 ：打开“终端”。
在窗口中输入 "curl -I" + 加速域名资源，例如curl -I www.example.com/10.JPG。
norman@Norman ~ % curl -I http://xxx/public/picture/xueshan.jpg HTTP/1.1 200 OK Server: Tengine Content-Type: image/jpeg Content-Length: 319717 Connection: keep-alive Date: Fri, 07 Feb 2025 06:15:50 GMT x-oss-request-id: 67xxx333314984F6 Vary: Origin x-oss-cdn-auth: success Accept-Ranges: bytes ETag: "F641480662xxx1E55F6C851AF" Last-Modified: Thu, 14 Nov 2024 01:42:56 GMT x-oss-object-type: Normal x-oss-hash-crc64ecma: 14568304759889530959 x-oss-storage-class: Standard Content-MD5: 9kFIBmLCpOlayx5V9shRrw== x-oss-server-time: 83 Via: cache40.l2cn3160[0,0,200-0,H], cache55.l2cn3160[1,0], kunlun3.cn7174[0,0,200-0,H], kunlun8.cn7174[7,0] Age: 26 Ali-Swift-Global-Savetime: 1738908951 X-Cache: HIT TCP_MEM_HIT dirn:-2:-2 X-Swift-SaveTime: Fri, 07 Feb 2025 06:16:08 GMT X-Swift-CacheTime: 2591983 Timing-Allow-Origin: * EagleId: b4a3921c17389089757582374e
当响应头结果中有Age、X-Cache、X-Swift-SaveTime、X-Swift-CacheTime时，证明阿里云CDN已经生效。
说明
X-Cache：字段为MISS，则表示未命中缓存，需要进行回源处理；X-Cache字段为HIT，则表示命中了CDN缓存，会直接读取缓存数据。
Age: 表示文件在CDN节点上缓存的时间（秒）。文件被
