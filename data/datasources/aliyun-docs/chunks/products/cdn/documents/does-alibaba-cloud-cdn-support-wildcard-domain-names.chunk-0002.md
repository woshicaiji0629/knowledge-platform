## 泛域名添加规则
泛域名添加规则如下：
域名（例如：image.example.com）总长度不超过100字符。
域名去掉根域名之后的子域名部分（例如：域名image.example.com去掉根域名example.com之后的子域名是image）的长度不超过64字符。
泛域名添加支持两种格式：.aliyundoc.com和*.aliyundoc.com，两种添加方式效果相同，添加之后控制台上显示都是.aliyundoc.com。
CDN支持多级泛域名，例如：*.example.aliyundoc.com、*.image.example.aliyundoc.com、*.cat.image.example.aliyundoc.com等。
泛域名的所有次级域名的流量都会和普通域名一样产生费用，资源监控中会将泛域名产生的流量做汇总，单个泛域名加速将按照一个加速域名计费，即不提供单个准确次域名的计费数据。
