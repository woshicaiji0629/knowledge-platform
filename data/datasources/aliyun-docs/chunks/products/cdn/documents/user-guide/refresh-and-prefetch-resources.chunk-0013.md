### 强制刷新
适用场景：紧急清理违规或错误资源、修复错误的Cache-Control响应头配置后需要强制全网更新、源站文件同名更新等场景。
机制：通过[刷新缓存](../developer-reference/api-cdn-2018-05-10-refreshobjectcaches.md)提交刷新任务时，将参数Force设置为true来触发。此模式下，CDN 边缘节点会无条件地将缓存资源标记为失效，不再进行304校验。
效果：下次访问该资源时，CDN 边缘节点将必须回源获取新版本，即使源站上的文件并未改变。
强制刷新的典型应用场景
以下场景建议使用强制刷新（通过[刷新缓存 API](../developer-reference/api-cdn-2018-05-10-refreshobjectcaches.md)设置Force=true）：
违规内容或木马清理：源站删除恶意文件后，必须使用强制刷新，或确保源站对该 URL 返回正确的 HTTP 状态码（如404）。否则边缘节点可能因标记刷新回源校验后仍保留旧缓存，继续提供违规内容。
同名文件更新（配置变更）：若源站文件同名替换但内容不同，标记刷新可能因源站返回304 Not Modified状态码而继续使用旧缓存。此时应使用强制刷新确保全网更新到最新内容。
页面显示异常或首页循环：若访问网站其他页面时一直显示首页，或图片显示异常，且 URL 刷新无效，建议使用目录刷新并通过 API 设置Force=true进行强制刷新。
API 强制刷新参数示例：
{ "ObjectType": "Directory", "ObjectPath": "https://www.example.com/static/", "Force": true }
关键参数说明：
ObjectType：填写Directory（目录）或File（文件）。
ObjectPath：填写以/结尾的完整目录路径，或具体的文件URL。
Force：设置为true开启强制刷新，忽略源站的If-Modified-Since/If-None-Match校验，直接清除缓存。
