## 常见问题
Q：我的数据安全吗？阿里云百炼会用我的数据进行训练吗？
A：不会。阿里云严格保护数据隐私，不会将您的数据用于模型训练。构建应用或训练模型时传输的所有数据均经过加密处理。详情请参见[合规资质与隐私说明](privacy-notice.md)。
Q：阿里云百炼提供哪些地域的服务？不同地域有什么区别？
A：目前提供以下地域的模型服务：
华北2（[北京](https://bailian.console.aliyun.com/?tab=model#/model-market)）、美国（[弗吉尼亚](https://modelstudio.console.aliyun.com/us-east-1)）、国际（[新加坡](https://modelstudio.console.aliyun.com/?tab=doc#/doc/?type=model&url=2840914)）、德国（[法兰克福](https://modelstudio.console.aliyun.com/eu-central-1)）和日本（[东京](https://modelstudio.console.aliyun.com/ap-northeast-1)）地域
建议选择邻近地域以降低网络延迟。各地域的接入点（Endpoint/Base URL）不同，API Key 不通用，支持的模型、平台功能与价格也有所差异，详情请参见[选择模型](models.md)。
Q：如何避免产生费用？
A：百炼采用按量付费，本身没有"自动扣费"开关。以下措施可有效控制费用：
删除API Key：前往[阿里云百炼控制台](https://bailian.console.aliyun.com/cn-beijing?spm=5176.29619931.J__Z58Z6CX7MY__Ll8p1ZOR.1.7dd7521cmX1pAh&tab=model#/model-market)，选择目标地域，进入[API-KEY](https://bailian.console.aliyun.com/?apiKey=1&tab=globalset#/efm/api_key)页面，删除所有API Key，从源头阻断调用。
停止所有调用：停止应用程序、智能体、工作流中的模型调用，并排查定时任务和后台进程。
清理计费资源：删除不再使用的知识库；前往[模型部署](https://bailian.console.aliyun.com/?tab=model#/efm/model_deploy)页面，下线按算力时长计费的部署实例。
开启"[免费额度用完即停](new-free-quota.md)"（仅限新用户且在免费额度有效期内）：在模型详情页开启此开关，免费额度耗尽后服务自动停止，不会转为付费。仅适用于华北2（北京）地域（[中国内地服务部署
