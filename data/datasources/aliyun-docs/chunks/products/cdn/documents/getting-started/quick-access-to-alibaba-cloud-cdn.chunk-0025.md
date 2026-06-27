X-Cache、X-Swift-SaveTime、X-Swift-CacheTime时，证明阿里云CDN已经生效。
说明
X-Cache：字段为MISS，则表示未命中缓存，需要进行回源处理；X-Cache字段为HIT，则表示命中了CDN缓存，会直接读取缓存数据。
Age: 表示文件在CDN节点上缓存的时间（秒）。文件被刷新或首次访问无此字段。Age为0表示缓存过期，需回源校验。
X-Swift-SaveTime：表示资源首次被缓存到CDN节点上的时间（GMT）。转换为中国北京时间需加上8小时。
X-Swift-CacheTime：字段值表示CDN节点上的允许缓存时间，即该文件可以在CDN节点上缓存多久。如果是0，则表示该请求无法缓存。
说明
如果您按照上述流程配置完成之后，仍然出现无法访问或访问异常，请见[无法访问/访问异常排查](../support/faq.md)。
至此，阿里云CDN的主要配置已完成，您的网站现在可以通过阿里云CDN实现访问加速。
