delivery.md) 后，在 [CDN](https://cdnnext.console.aliyun.com/log/realtime/pushData) [实时日志数据统计](https://cdnnext.console.aliyun.com/log/realtime/pushData) 页面查看和分析。 |

访问报错403 Forbidden如何排查？
403错误可能来自OSS或CDN的权限拦截，建议直接访问OSS默认域名观察是否正常。
正常：问题在CDN侧，需排查CDN的Referer防盗链、URL鉴权、私有Bucket回源是否开启等配置。
也报403错误：问题在OSS侧，需要排查OSS的Bucket ACL、Referer防盗链、Bucket Policy等配置。
为什么业务切换到CDN后OSS仍产生下行流量费用？
可能原因：
存在直接访问OSS的请求：检查业务代码或第三方系统集成中是否有未替换为CDN加速域名的OSS域名。
CDN缓存未命中导致回源：回源会产生OSS的CDN回源流出流量。检查CDN缓存命中率，如果较低请优化缓存配置。
Bucket为公共读被恶意访问：如果Bucket权限为公共读，可能被恶意访问。建议在业务允许的情况下将Bucket设为私有并开启CDN私有回源。
该文章对您有帮助吗？
反馈
