## 跨域校验规则
重要
是否允许重复和跨域校验这两个配置项之间存在互斥，是否允许重复配置为允许的情况下，跨域校验将会失效。
任意匹配：自定义响应头参数Access-Control-Allow-Origin的值设置为*不论用户请求里面是否携带Origin参数，也不论携带的Origin参数为何值，都固定返回Access-Control-Allow-Origin:*。
精确匹配：自定义响应头参数Access-Control-Allow-Origin的值设置了单个或者多个值（多个值之间用,分隔）。
如果用户请求头里携带的Origin参数值与被设置的任意一个值精确匹配，就会响应对应的跨域头。
如果都没有精确匹配上，则不响应跨域头。
泛域名匹配：自定义响应头参数Access-Control-Allow-Origin的值设置了泛域名，则会校验请求头中Origin值是否能匹配上Access-Control-Allow-Origin的泛域名。
您可以参考[配置跨域资源共享](configure-cors.md)来了解如何配置。
