## 问题描述
在使用阿里云CDN时，CDN的缓存命中率很低。在浏览器中，按F12键，在访问页面中，单击Network，然后在Name选项中，单击Headers，在Response Headers模块中，确认URL响应头信息中X-Cache为MISS，则表示没有命中CDN缓存。但是在页面中，对应文件的URL响应头信息的X-Cache为HIT。
说明：本案例以Chrome浏览器为例。
