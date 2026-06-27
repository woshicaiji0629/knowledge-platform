# 使用Argo Workflow编排动态DAG Fan-out/Fan-in任务
在工作流编排过程中，为了加快大任务处理的速度，可以使用Fan-out Fan-in任务编排，将大任务分解成小任务，然后并行运行小任务，最后聚合结果。分布式工作流Argo集群（简称工作流集群）支持动态DAG方式编排Fan-out Fan-in任务，可按需调度云上算力、利用云上弹性可调用数万核CPU资源，减少运行时间，运行结束后能够及时回收资源节省成本。本文为您介绍如何使用工作流集群的Argo Workflow编排动态DAG Fan-out Fan-in任务。
