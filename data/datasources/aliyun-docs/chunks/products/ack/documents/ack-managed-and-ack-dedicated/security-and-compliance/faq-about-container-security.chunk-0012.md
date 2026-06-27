### Deployment的Pod扩缩容相关操作的审计日志查询方法
在查询 / 分析文本框中输入以下SQL查询命令，然后单击查询 / 分析。更多操作，请参见[审计日志查询方法](faq-about-container-security.md)。
requestURI: deployments and (verb: update or verb: patch) and replicas and deployments and <deployment_name> not deployment-controller
说明
上述查询命令在查询时，需要将<deployment_name>替换为实际的Deployment名称。
该文章对您有帮助吗？
反馈
