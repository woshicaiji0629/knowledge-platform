## 定时配置Serverless实例弹性伸缩范围
实践教程：[定时配置](configure-scheduled-tasks-to-adjust-the-number-of-rcus-for-serverless-apsaradb-rds-instances.md)[Serverless](configure-scheduled-tasks-to-adjust-the-number-of-rcus-for-serverless-apsaradb-rds-instances.md)[实例的](configure-scheduled-tasks-to-adjust-the-number-of-rcus-for-serverless-apsaradb-rds-instances.md)[RCU](configure-scheduled-tasks-to-adjust-the-number-of-rcus-for-serverless-apsaradb-rds-instances.md)
简介：Serverless实例RCU弹性伸缩的耗时通常为秒级，极小概率下可能因为跨机弹性扩容而耗时3~5分钟。如果您对特定时段的稳定性有严格要求，您可以定时配置Serverless实例的RCU，提前增加RCU数量。本教程将介绍如何对RCU的范围进行周期性配置。
涉及功能：[RDS MySQL Serverless](rds-mysql-serverless.md)[实例](rds-mysql-serverless.md)
