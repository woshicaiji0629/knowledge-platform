## 相关文档
kube-scheduler发布记录，请参见[kube-scheduler](../../product-overview/kube-scheduler.md)。
通过Kubernetes原生的ResourceQuota方式进行固定资源分配，集群的整体资源利用率不高。阿里云借鉴Yarn Capacity Scheduling的设计思路，基于Scheduling Framework的扩展机制，在调度侧通过引入弹性配额组实现了Capacity Scheduling功能，在确保用户资源分配的基础上通过资源共享的方式来提升集群的整体资源利用率。详细信息，请参见[使用](use-capacity-scheduling.md)[Capacity Scheduling](use-capacity-scheduling.md)。
该文章对您有帮助吗？
反馈
