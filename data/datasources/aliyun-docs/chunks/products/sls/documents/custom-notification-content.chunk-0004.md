# 标题一 ## 标题二 ### 标题三 #### 标题四 ##### 标题五 ###### 标题六
加粗
**bold**
链接
[这是一个链接](http://work.weixin.qq.com/api/doc)
行内代码段
`code`
引用
> 引用文字
字体颜色
只支持3种内置颜色。
<font color="info">绿色</font> <font color="comment">灰色</font> <font color="warning">橙红色</font>
飞书
飞书渠道的内容支持Markdown语法，具体支持的元素如下。更多信息，请参见[使用](https://open.feishu.cn/document/ukTMukTMukTM/uADOwUjLwgDM14CM4ATN)[markdown](https://open.feishu.cn/document/ukTMukTMukTM/uADOwUjLwgDM14CM4ATN)[标签](https://open.feishu.cn/document/ukTMukTMukTM/uADOwUjLwgDM14CM4ATN)。
加粗
**粗体**
斜体
*斜体*
删除线
～～删除线～～
超链接
<a>https://open.feishu.cn</a>
文字链接
[开发文档](https://open.feishu.cn)
图片
![hover_text](image_key)
分割线
---
Slack
Slack应用中的Incoming Webhook支持Markdown类型的消息，但只支持部分Markdown语法。更多信息，请参见[Slack Markdown Reference](https://www.markdownguide.org/tools/slack/#messages)。
Webhook
Webhook渠道支持逐条发送和合并发送。
内容模板：
{ "项目": "${project}", "告警名称": "${alert_name}" }
合并发送的通知内容：
[ { "项目": "project-name1", "告警名称": "alert-name1" }, { "项目": "project-name2", "告警名称": "alert-name2" } ]
邮件
邮件渠道的内容支持HTML标签。更多信息，请参见[HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)。例如：
使用<br>换行。
使用<a href="${query_url}">查看详情</a>添加链接。您可以单击该链接查看触发告警的详细信息。
使用<strong>${severity}</strong>加粗显示告警严重度。
该
