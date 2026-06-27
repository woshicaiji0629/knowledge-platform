## 错误信息
错误信息："rejected by podgroup xxx"。
原因：当集群中同时存在多个PodGroup调度时，由于调度器存在BackOff队列，可能存在一个PodGroup的所有Pod的调度没有完全聚合在一起的情况。此时已经预占资源的Pod可能会影响后续PodGroup的Pod调度，因此在后续PodGroup的Pod调度时，会拒绝上一个调度的PodGroup中已经预占资源的Pod。这是一种正常现象，通常不会持续很久，若持续时间超过二十分钟，您可以[提交工单](https://selfservice.console.aliyun.com/ticket/createIndex)进行排查。
