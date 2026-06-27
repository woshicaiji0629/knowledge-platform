## 步骤四：验证通过向轻量消息队列（原 MNS）发送消息触发工作流
登录[轻量消息队列（原 MNS）控制台](https://mns.console.aliyun.com/)。
在队列列表页面中，找到队列test-event-queue，在其操作列单击收发消息。
在收发消息快速体验页面中，输入消息内容test trigger argo workflow，然后单击发送消息。
在工作流集群中查看工作流的运行情况。
argo list
预期输出如下：
NAME STATUS AGE DURATION PRIORITY ali-mns-workflow-5prz7 Running 6s 6s 0
获取工作流日志，查看消息内容。
argo logs ali-mns-workflow-5prz7
重要
该命令中的工作流名称必须和上一步骤中返回的工作流名称一致，ali-mns-workflow-5prz7仅为示例值，请修改为实际环境中的返回值。
消息内容使用Base64编码。
预期输出如下：
ali-mns-workflow-5prz7-whalesay-2429203954: time="2023-12-14T08:33:37.964Z" level=info msg="capturing logs" argo=true ali-mns-workflow-5prz7-whalesay-2429203954: ali-mns-workflow-5prz7-whalesay-2429203954: < dGVzdCBOcmlnZ2VyIGFyZ28gd29ya2Zsb3c= > ali-mns-workflow-5prz7-whalesay-2429203954: ----------------------------------------- ali-mns-workflow-5prz7-whalesay-2429203954: \ ali-mns-workflow-5prz7-whalesay-2429203954: \ ali-mns-workflow-5prz7-whalesay-2429203954: \ ali-mns-workflow-5prz7-whalesay-2429203954: ## . ali-mns-workflow-5prz7-whalesay-2429203954: ## ## ## == ali-mns-workflow-5prz7-whalesay-2429203954: ## ## ## ## === ali-mns-workflow-5prz7-whalesay-2429203954: /""""""""""""""""___/ === ali-mns-workflow-5prz7-whalesay-2429203954: ~~~
