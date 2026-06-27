# 配置源站修改入站响应头-CDN(CDN)-阿里云帮助中心

Source: https://help.aliyun.com/zh/cdn/user-guide/rewrite-http-response-headers

[大模型](https://www.aliyun.com/product/tongyi)[产品](https://www.aliyun.com/product/list)[解决方案](https://www.aliyun.com/solution/tech-solution/)[权益](https://www.aliyun.com/benefit)[定价](https://www.aliyun.com/price)[云市场](https://market.aliyun.com/)[伙伴](https://partner.aliyun.com/management/v2)[服务](https://www.aliyun.com/service)[了解阿里云](https://www.aliyun.com/about)

查看 "" 全部搜索结果

[AI 助理](https://www.aliyun.com/ai-assistant?displayMode=side)

[文档](https://help.aliyun.com/)[备案](https://beian.aliyun.com/)[控制台](https://home.console.aliyun.com/home/dashboard/ProductAndService)

[官方文档](https://help.aliyun.com/zh)

- [产品概述](products/cdn/documents/product-overview.md)

- [快速入门](products/cdn/documents/getting-started.md)

- [操作指南](products/cdn/documents/user-guide.md)

- [实践教程](products/cdn/documents/use-cases.md)

- [安全合规](products/cdn/documents/security-and-compliance.md)

- [开发参考](products/cdn/documents/developer-reference.md)

- [服务支持](products/cdn/documents/support.md)

- [视频专区](products/cdn/documents/videos.md)

[首页](https://help.aliyun.com/zh)

# 修改入站响应头

更新时间：

复制 MD 格式

[产品详情](https://www.aliyun.com/product/cdn)

[我的收藏](https://help.aliyun.com/my_favorites.html)

当CDN节点上的缓存过期或者没有命中缓存时，CDN节点会向源站发起请求来获取最新内容，源站返回的内容以及相关的HTTP头部信息就是回源响应头。您可以通过调整源站修改入站响应头，来设置缓存策略、跨域资源共享等，从而优化网站的加载速度、增强内容安全性、控制资源可访问性，并提高用户体验。

## 背景信息

HTTP响应头是HTTP的响应消息头的组成部分之一，可携带特定响应参数信息并传递给客户端。

当CDN节点上没有缓存用户请求的内容时，CDN会回源站拉取资源，源站收到CDN的请求后会给出响应。为了便于用户识别源站的响应信息，您可以修改入站响应头功能，改写用户源站响应报文中的HTTP Header信息。例如，改写回源响应头中Content-Type参数的值，然后再传递给客户端，以确保客户端解析正常（如果源站返回的Content-Type值有误，客户端直接解析将出现乱码，因此需要在CDN上改写）。

说明

- 

入站响应指源站收到CDN节点的请求后，返回给CDN节点的HTTP消息。修改入站响应头配置只会影响源站响应给CDN节点的HTTP消息，对于CDN节点直接响应给用户的HTTP消息不作修改。

- 

不支持对泛域名修改入站响应头。

## 适用场景

以下是一些常见的场景和示例：

- 

内容类型不正确：如果源站返回的内容类型（Content-Type）与实际内容不符，客户端可能会无法正确解析。例如，一个HTML文件被错误地标记为纯文本。这时可以通过配置回源响应头来修正。

示例：将Content-Type: text/plain更改为Content-Type: text/html。

- 

缓存策略控制：如果您需要对CDN缓存策略进行更精细的控制，可以调整源站的回源响应头中的Cache-Control或Expires字段。这有助于优化内容的更新频率和缓存命中率。

示例：将Cache-Control: max-age=3600更改为Cache-Control: max-age=86400，以延长缓存有效期。CDN的默认缓存规则具体请参见[阿里云](products/cdn/documents/user-guide/configure-the-cdn-cache-expiration-time.md)[CDN](products/cdn/documents/user-guide/configure-the-cdn-cache-expiration-time.md)[默认缓存规则及优先级](products/cdn/documents/user-guide/configure-the-cdn-cache-expiration-time.md)。

- 

跨域资源共享（CORS）：如果您希望允许其他域名的Web应用访问CDN上托管的资源，则需要在源站设置Access-Control-Allow-Origin和其他相关的CORS头。这些设置确保在浏览器执行跨域请求时，CDN能够提供适当的响应头给客户端，避免CORS错误。关于跨域访问问题，您可以参见[配置跨域资源共享](products/cdn/documents/user-guide/configure-cors.md)。

示例：

- 

Access-Control-Allow-Origin: *：允许所有域名进行跨域资源请求。

- 

Access-Control-Allow-Methods: GET, POST, OPTIONS：指定允许跨域请求的HTTP方法。

- 

压缩传输：如果源站支持压缩传输但没有启用，或者使用的压缩算法不是最有效的，可以通过设置回源响应头中的Accept-Encoding来让源站使用最优的压缩方式。

示例：将Accept-Encoding: gzip, deflate更改为Accept-Encoding: br，以优先使用Brotli压缩。关于Brotli压缩相关内容具体请参见[Brotli](products/cdn/documents/user-guide/configure-brotli-compression.md)[压缩](products/cdn/documents/user-guide/configure-brotli-compression.md)。

- 

重定向：当源站需要重定向用户到另一个URL时，回源响应头可以设置正确的重定向响应头。关于重定向具体请参见[配置回源](products/cdn/documents/user-guide/configure-301-or-302-redirection.md)[301/302](products/cdn/documents/user-guide/configure-301-or-302-redirection.md)[跟随](products/cdn/documents/user-guide/configure-301-or-302-redirection.md)。

示例：Location: https://www.example.com/new-page.html：通知CDN及用户浏览器新的资源位置，用于301或302重定向。

- 

自定义回源行为：在某些情况下，源站可能需要提供一些自定义的头部信息给客户端，以实现特定的功能或跟踪目的，您可以通过配置回源响应头来添加这些自定义头部。

## 注意事项

- 

在添加了多条配置的情况下，执行顺序按配置列表从上到下，因此需要注意多个配置操作将会叠加，最终结果可能会与预期不符。以下例子中配置2最终生效：

- 

配置1：增加HTTP响应头：cache-control: max-age=3600

- 

配置2：增加HTTP响应头：cache-control: no-cache

- 

引用规则条件时，按所关联规则条件的优先级匹配，而非按功能自身的配置顺序匹配。

## 操作步骤

- 

登录[CDN](https://cdn.console.aliyun.com)[控制台](https://cdn.console.aliyun.com)。

- 

在左侧导航栏，单击域名管理。

- 

在域名管理页面，找到目标域名，单击操作列的管理。

- 

在指定域名的左侧导航栏，单击回源配置。

- 

单击修改入站响应头页签。

- 

单击添加。

- 

修改入站响应头信息。

重要

当不同的操作方式同时作用于同一个回源响应头参数时，会存在操作冲突。此时按照操作类型的优先级来执行，优先级顺序为替换＞增加＞变更和删除。例如，当增加和删除操作同时作用于同一个参数时，会先增加再删除。

### 增加响应头参数

- 

- 

- 

- 

| 配置项 | 示例 | 说明 |
| --- | --- | --- |
| 响应头操作 | 增加 | 在回源 HTTP 请求中增加指定的响应头参数。 |
| 自定义响应头参数 | 自定义回源响应头 | 选择 自定义回源响应头 或选择已经预设好的响应头参数。 |
| 自定义响应头名称 | x-code | 自定义响应头名称为 x-code。 |
| 响应头值 | key1 | 一个响应头参数中可以配置多个值，多个值用英文逗号（,）分隔。 |
| key1，key2 |  |  |
| 是否允许重复 | 允许 | 允许 ：可以添加重复的响应头参数。例如 x-code:key1 ， x-code:key2 。 不允许 ：添加同一个响应头参数，新值将覆盖旧值。例如先添加 x-code:key1 ，再添加 x-code:key2 ，最终的值为 x-code:key2 。 |
| 规则条件 | 不使用 | 规则条件能够对用户请求中携带的各种参数信息进行识别，以此来决定某个配置是否对该请求生效。 不使用 ：不使用规则条件。 若需新增或编辑规则条件，请在 [规则引擎](products/cdn/documents/user-guide/rules-engine.md) 中进行管理。 |


### 删除响应头参数

- 

- 

| 配置项 | 示例 | 说明 |
| --- | --- | --- |
| 响应头操作 | 删除 | 删除所有与响应头参数名称匹配的参数值，无论是否有重复的响应头参数。 |
| 自定义响应头参数 | 自定义回源响应头 | 选择 自定义回源响应头 或选择已经预设好的响应头参数。 |
| 自定义响应头名称 | x-code | 自定义响应头名称为 x-code。 |
| 规则条件 | 不使用 | 规则条件能够对用户请求中携带的各种参数信息进行识别，以此来决定某个配置是否对该请求生效。 不使用 ：不使用规则条件。 若需新增或编辑规则条件，请在 [规则引擎](products/cdn/documents/user-guide/rules-engine.md) 中进行管理。 |


### 变更响应头参数

- 

- 

| 配置项 | 示例 | 说明 |
| --- | --- | --- |
| 响应头操作 | 变更 | 当响应头参数不存在重复时，可以正常变更参数，如果有多个重复的响应头参数，则不允许变更。 |
| 自定义响应头参数 | 自定义回源响应头 | 选择 自定义回源响应头 或选择已经预设好的响应头参数。 |
| 自定义响应头名称 | x-code | 自定义响应头名称为 x-code。 |
| 响应头变更为 | key1，key3 | 一个响应头参数中可以配置多个值，多个值用英文逗号（,）分隔。 |
| 规则条件 |  | 规则条件能够对用户请求中携带的各种参数信息进行识别，以此来决定某个配置是否对该请求生效。 不使用 ：不使用规则条件。 若需新增或编辑规则条件，请在 [规则引擎](products/cdn/documents/user-guide/rules-engine.md) 中进行管理。 |


### 替换响应头参数

- 

- 

- 

- 

| 配置项 | 示例 | 说明 |
| --- | --- | --- |
| 响应头操作 | 替换 | 当响应头参数不存在重复时，可以正常替换参数，如果有多个重复的响应头参数，则不允许替换。 |
| 自定义响应头参数 | 自定义回源响应头 | 选择 自定义回源响应头 或选择已经预设好的响应头参数。 |
| 自定义响应头名称 | x-code | 自定义响应头名称为 x-code。 |
| 查找 | key | 正则表达式查找需要替换的参数值。 |
| 替换为 | abc | 正则表达式替换需要替换的参数值。 |
| 匹配 | 匹配所有 | 匹配所有 ：所有匹配上的值都会被替换。例如 x-code:key1,key2,key3 ，正则匹配值 key 替换为 abc，替换后的结果为 x-code:abc1,abc2,abc3 。 仅匹配第一个 ：只有第一个匹配上的值会被替换。例如 x-code:key1,key2,key3 ，正则匹配值 key 替换为 abc，替换后的结果为 x-code:abc1,key2,key3 。 |
| 规则条件 | - | 规则条件能够对用户请求中携带的各种参数信息进行识别，以此来决定某个配置是否对该请求生效。 不使用 ：不使用规则条件。 若需新增或编辑规则条件，请在 [规则引擎](products/cdn/documents/user-guide/rules-engine.md) 中进行管理。 |


- 

单击确定。

## 默认预设响应头

阿里云CDN默认预设了Cache-Control、Content-Type、Expires、Last-Modified四个修改入站响应头，这四个响应头是HTTP协议中的重要组成部分，它们分别用于控制缓存、定义内容类型、设置过期时间以及记录资源的最后修改时间。

- 

- 

- 

- 

| CDN 默认预设响应头 | 说明 | 示例 |
| --- | --- | --- |
| Cache-Control | 用于控制资源在 CDN 缓存中的行为和时间周期的头信息。它为 CDN 节点和客户端浏览器提供了缓存指示，例如何时缓存内容、缓存多久，以及缓存的内容何时被认为是过时的。优先级高于旧的 Expires 头部。 | Cache-Control: no-cache 强制在使用缓存的资源之前总是向源站进行验证。 Cache-Control: max-age=3600 指示资源在 3600 秒（1 小时）内是新鲜的，可以从 CDN 缓存中提供，无需回源。 |
| Content-Type | 描述了返回给客户端的资源的数据类型。它帮助客户端正确地解释和显示接收到的数据。CDN 使用这个头信息来处理对应的数据类型以及如何传输它们。 | Content-Type: text/html 表示发送的内容是 HTML 格式。 Content-Type: image/jpeg 表示资源是 JPEG 图像格式。 |
| Expires | 提供了一个具体的日期/时间，这个时间点之后资源被认为是过期的。CDN 使用这个头来确定资源是否仍然有效，如果过期，CDN 将回源请求新的资源。 Expires 响应头是一个相对古老的头部，在 HTTP/1.1 中， Cache-Control 头部提供了更细粒度的控制，因此 Expires 的使用已经逐渐减少。 | Expires: Thu, 01 Dec 2023 16:00:00 GMT 指出在指定的 GMT 时间后，内容过期。 |
| Last-Modified | 表示资源最后一次被修改的时间。CDN 和浏览器使用这个响应头来判断自从该资源上次被缓存后是否有被修改过。 | Last-Modified: Wed, 21 Oct 2023 07:28:00 GMT 显示资源最后修改的时间。 |


## 配置示例

### 示例一：配置响应文档属于某种MIME类型

配置场景

如果您希望配置响应文档属于某种MIME类型。

说明

MIME类型主要包含以下几类：

- 

文本类型：包括文本文件（例如.txt、.csv）和HTML文件（例如.html、.htm、.shtml）。

- 

图片类型：包括常见的图片文件（例如.jpg、.png、.gif）。

- 

音频类型：包括音频文件（例如.mp3、.wav）。

- 

视频类型：包括视频文件（例如.mp4、.avi）。

- 

应用程序类型：包括应用程序文件（例如.pdf、.doc、.xls）。

配置方法

- 

响应头操作：增加

- 

自定义响应头名称：Content-Type。

- 

响应头值：text/html。

其中是否允许重复选择不允许，规则条件选择不使用，然后单击确定。

结果说明：在源站发送给CDN节点的响应信息中声明内容类型为text/html，再次配置将覆盖旧值。

### 示例二：删除响应头信息

配置场景

如果您希望删除响应头信息。

配置方法

- 

响应头操作：删除

- 

自定义响应头名称：Content-Type。

其中是否允许重复选择不允许，规则条件选择不使用，然后单击确定。

结果说明：删除请求头中的Content-Type信息，然后返回给用户。

说明

如果同时完成了示例一和示例二，那么会先增加响应头Content-Type信息（响应的内容属于text/html类型），然后删除该请求头，最终结果为：响应的资源没有MIME类型限制，直接以最初的类型返回用户。

## 常见问题

### 为什么已经配置了响应头Access-Control-Allow-Origin，但是访问资源仍提示跨域问题，response header中没有配置的响应头？

如果您在阿里云CDN中配置了回源响应头，如Access-Control-Allow-Origin等，但是在客户端访问资源时遇到跨域问题，并且在响应头（response header）中没有看到这些配置的响应头，可能原因有以下几点：

可能的原因

- 

配置未生效或错误：可能是配置没有正确设置或尚未生效，导致CDN没有按照预期返回跨域响应头。

- 

CDN缓存：CDN节点可能缓存了旧的响应头信息，这会导致即使您已更改配置，也仍然返回旧的头信息。

- 

源站问题：如果您在CDN上配置了跨域响应头，但是源站的响应中也包含了跨域响应头，并且这些响应头与CDN的配置冲突，这可能会导致问题。在这种情况下，需要统一CDN和源站的配置。

- 

浏览器缓存：浏览器可能缓存了旧的响应，导致它并未发起新的请求以获取更新后的响应头。

解决方案

- 

验证配置：确认CDN配置已正确设置并且已经生效，特别是跨域相关的响应头设置。

- 

清除CDN缓存：您可以使用CDN的刷新功能清空已缓存的内容，然后再次访问资源。具体请参见[刷新和预热资源](products/cdn/documents/user-guide/refresh-and-prefetch-resources.md)。

- 

检查源站设置：确认源站不会返回与CDN配置冲突的跨域响应头。建议将源站回源响应头与节点响应头中的跨域头设置为也一致，如果配置不一致，可能会导致冲突。

- 

清除浏览器缓存：清空浏览器缓存，或使用无痕（隐私）模式测试，确保浏览器获取最新的响应头。

- 

联系技术支持：如果您尝试了上述所有方法，但问题仍然存在，可能是CDN服务方面的问题。请联系阿里云CDN的技术支持或提交工单寻求帮助。

### 怎么检查源站上正确设置了Access-Control-Allow-Origin等响应头？

如果您的源站为阿里云服务器ECS

您需要确保在ECS上运行的Web服务器或应用程序正确设置了Access-Control-Allow-Origin以及其他CORS（跨源资源共享）相关的响应头，可以按照以下步骤进行：

- 

登录[ECS](https://ecs.console.aliyun.com)[管理控制台](https://ecs.console.aliyun.com)访问您的ECS实例。

- 

检查Web服务器跨域配置。

跨域响应头的配置可能因您使用的Web服务器或应用程序而异。常见的Web服务器有Apache、Nginx等。

## Apache

在.htaccess文件或服务器配置文件（如httpd.conf或vhosts.conf）中查找类似以下内容：

Header set Access-Control-Allow-Origin "*"

或者，对于特定的域名：

Header set Access-Control-Allow-Origin "http://example.com"

确认这些配置是否存在，并已经正确设置。

## Nginx

在Nginx配置文件（通常是/etc/nginx/nginx.conf或/etc/nginx/sites-available/default）中，找到与您的应用相关的server块，并检查如下设置：

location / { add_header 'Access-Control-Allow-Origin' '*'; }

或者，对于特定的域名：

location / { add_header 'Access-Control-Allow-Origin' 'http://example.com'; }

确认这些配置是否存在，并已经正确设置。

- 

重启Web服务器。

在修改配置文件后，需要重启Web服务器以使更改生效。例如对于Apache和Nginx，您可以使用以下命令重启服务器。

- 

对于Apache：

sudo service apache2 restart

- 

对于Nginx：

sudo service nginx restart

- 

浏览器验证响应头。

使用开发者工具的“网络”面板访问您的资源，检查是否在响应头中看到Access-Control-Allow-Origin。如果看不到，可能是配置没有生效，或者存在CDN缓存。

如果您的源站为阿里云对象存储OSS

阿里云OSS支持跨域资源共享（CORS），您可以通过OSS控制台检查OSS上是否正确设置了Access-Control-Allow-Origin等响应头，可以按照以下步骤进行：

- 

登录[OSS](https://oss.console.aliyun.com/)[管理控制台](https://oss.console.aliyun.com/)。

- 

单击Bucket 列表，然后单击目标Bucket名称。

- 

在左侧导航栏，选择数据安全>跨域设置。

- 

在跨域规则列表中，检查规则中是否包含Access-Control-Allow-Origin的配置项，并确认其值是否正确。

- 

如果您希望允许任何源访问，Access-Control-Allow-Origin应设置为*。

- 

如果您只想允许特定的源访问，Access-Control-Allow-Origin应设置为具体的源地址，如https://yourdomain.com。

- 

检查其他相关跨域头。

除了Access-Control-Allow-Origin外，可能还需要检查以下CORS相关头部是否已经正确配置：

- 

Access-Control-Allow-Methods：指定允许的HTTP方法，如GET,POST,PUT,DELETE等。

- 

Access-Control-Allow-Headers：指定允许的自定义请求头，如果请求中包含了非标准的头部字段。

- 

Access-Control-Max-Age：指定预检请求（OPTIONS）的结果能够被缓存的最大时间。

- 

保存和测试。

如果发现设置不正确或需要更新，按照提示修改相应的值，然后保存更改。保存后，可能需要等待一段时间让更改生效。

关于OSS跨域配置相关详细说明，请参见[跨域设置](products/oss/documents/user-guide/configure-cross-origin-resource-sharing.md)。

如果在以上步骤中遇到问题或仍然无法解决问题，请联系阿里云CDN技术支持或提交工单寻求帮助。

### CDN 加速页面出现乱码如何处理？

如果 CDN 加速后的页面出现乱码，通常是因为源站返回的Content-Type响应头未正确指定字符编码。可以通过以下步骤解决：

- 

登录域名管理控制台，找到目标域名。

- 

在域名详情页左侧导航栏中，单击回源配置，通过「修改出站响应头」功能，为对应的文件路径添加响应头规则，将Content-Type设置为text/plain; charset=utf-8。

- 

配置完成后，前往刷新和预热页面，刷新该路径下的缓存资源，使新规则生效。

说明

如果希望确保该文件不被缓存（避免后续更新不及时），可以在缓存配置中为该文件的对应路径（如/llms.txt）单独设置缓存过期时间为 0 秒。

### 全局强制设置 Content-Type 为 video/mp4 是否会影响其他资源（片）？如何精准配置？

如果对整个域名全局设置Content-Type为video/mp4，确实会影响该域名下的所有资源类型，包括图片、CSS、JS 等文件。为了避免影响其他文件，建议通过以下方式进行精准配置：

- 

按路径匹配：在「修改入站响应头」规则中，通过回源配置中的规则条件，指定仅对视频路径（如/vod-cd20e3/或.mp4后缀）生效。

- 

使用条件判断：CDN 控制台支持根据请求后缀或 Header 条件设置响应头，可限定仅对.mp4文件返回Content-Type: video/mp4。

通过上述方式，可以仅对视频文件修改Content-Type，而不会干扰图片等其他资源类型。

### 配置响应头控制视频下载或预览不生效怎么办？

可以通过缓存配置中的「修改出站响应头」功能配置Content-Disposition响应头来控制视频的下载或预览行为：

- 

设置为attachment; filename='video.mp4'时，用户访问该资源将触发下载。

- 

设置为inline时，资源将在浏览器中直接预览。

如果配置不生效，请检查以下事项：

- 

规则引擎匹配条件：确保规则的匹配条件针对的是 URI 路径（如包含/video-origin/20260414），而非仅匹配查询参数（query string）。规则引擎通过识别用户请求中的路径信息来决定配置是否生效。

- 

缓存问题：如果视频文件已被 CDN 缓存，旧的响应头可能仍然生效。请前往刷新和预热页面刷新该路径的缓存，使新配置生效。

### 因响应包含 Set-Cookie 导致 CDN 缓存命中率为 0，如何配置忽略 Set-Cookie？

当源站响应中包含Set-Cookie响应头时，CDN 默认不会缓存该响应，导致缓存命中率为 0。可以通过以下步骤解决：

- 

登录 CDN 控制台，在域名管理中找到目标域名，单击管理。

- 

在域名详情页左侧导航栏中，单击回源配置，进入修改入站响应头页签。

- 

单击添加，响应头操作选择删除，响应头名称填写Set-Cookie。

- 

配置完成后，刷新已有缓存资源，使新规则生效。

如果配置后缓存命中率仍未提升，请检查以下事项：

- 

确认源站侧是否已忽略源站缓存设置。

- 

检查缓存规则的路径配置，建议去掉 query 参数（如只保留路径livetstv4），避免查询参数导致缓存不命中。有关 CDN 默认缓存规则，请参见[阿里云 CDN 默认缓存规则及优先级](products/cdn/documents/user-guide/configure-the-cdn-cache-expiration-time.md)。

### JS 文件被当成 text/html 错误处理，首次刷新必现、第二次正常的原因及解决方法？

问题原因：

源站首次返回 JS 文件时，Content-Type响应头可能被错误设置为text/html。CDN 将该错误类型缓存后，首次访问时浏览器会按照text/html解析 JS 文件，导致乱码或执行异常。第二次访问时，由于源站已修正Content-Type或 CDN 重新回源获取了正确类型，页面恢复正常。

解决方法：

- 

在 CDN 控制台的「修改入站响应头」中配置规则，将 JS 文件的Content-Type强制替换为application/javascript。

- 

配置完成后，前往刷新和预热页面刷新该 JS 文件的缓存，使新规则立即生效。

### 修改入站响应头配置是否支持针对 JS 文件设置？设置后是否会影响其他文件类型？

支持。可以在「修改入站响应头」中只针对 JS 文件设置Content-Type为application/javascript，不会影响其他文件类型。

具体方法：在配置规则时，通过规则条件匹配.js后缀，使该响应头修改规则仅对 JS 文件生效。这样既能确保 JS 文件的 MIME 类型正确，又不会干扰 CSS、图片等其他资源类型。

### 修改入站响应头配置是否可用于确认 CDN 文件丢失或同步状态？

不可以。「修改入站响应头」的作用是修正或强制指定特定文件类型的 MIME 类型，以解决因源站首次返回错误类型导致的缓存异常问题。该功能不涉及检测 CDN 是否丢失文件，也不用于判断文件的同步状态。

如果需要排查 CDN 文件是否存在或同步状态异常，建议使用以下方法：

- 

通过 CDN 控制台的刷新和预热功能主动刷新目标文件，触发 CDN 回源验证文件是否存在。

- 

检查源站侧文件是否正常可访问。

- 

查看 CDN 日志，确认回源状态码是否正常。

[上一篇：配置IPv6回源](products/cdn/documents/user-guide/configure-back-to-origin-routing-over-ipv6.md)[下一篇：回源常见问题](products/cdn/documents/user-guide/back-to-source-faq.md)

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
