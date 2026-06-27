## 什么是泛域名加速？
泛域名加速是指使用通配符做加速域名以实现所有的次级域名的加速效果。例如.aliyundoc.com是一个泛域名，example.aliyundoc.com是这个泛域名对应的次级域名，image.developer.aliyundoc.com是这个泛域名对应的三级域名。
示例：您添加.aliyundoc.com泛域名作为加速域名。当您将.aliyundoc.com泛域名解析至CDN生成的CNAME域名时，所有此泛域名的次级域名（例如example.aliyundoc.com、demo.aliyundoc.com等）均可以解析到CDN上添加的泛域名.aliyundoc.com的CNAME加速。
重要
CDN泛域名加速不支持次级域名再往下级域名的加速，例如泛域名.aliyundoc.com的次级域名example.aliyundoc.com在CDN上面可以正常加速，而三级域名image.developer.aliyundoc.com将无法通过CDN平台实现加速，如果三级域名image.developer.aliyundoc.com的请求访问到CDN节点上，CDN节点将会拒绝该请求，并响应403状态码。
对于类似“.com.cn、.net.cn、.gov.cn、.edu.cn、.org.cn”这样的域名后缀（全量域名后缀参考官方链接[https://publicsuffix.org/list/public_suffix_list.dat](https://publicsuffix.org/list/public_suffix_list.dat)），CDN平台将会识别为顶级域名，即.aliyundoc.com.cn是一个泛域名，example.aliyundoc.com.cn是这个泛域名对应的次级域名，image.developer.aliyundoc.com.cn是这个泛域名对应的三级域名。
刷新或预热缓存时不支持泛域名URL或泛域名文件目录，但支持刷新或预热精确域名（包含次级域名）的URL和目录。例如不支持http://.aliyundoc.com/example/b.mp4的刷新或预热，支持http://example.aliyundoc.com/example/b.mp4的刷新或预热。
