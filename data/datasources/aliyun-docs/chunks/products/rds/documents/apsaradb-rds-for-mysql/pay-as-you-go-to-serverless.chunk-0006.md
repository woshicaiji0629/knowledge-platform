## 常见问题
Q：按量付费转换为Serverless后，为什么我在费用与成本>订购订单>我的订单中看到的订单为新购订单？
A：因为转换的实现原理为新购Serverless实例，再将原实例切换为新购实例，所以看到的订单为新购订单。
Q：使用自定义密钥加密的云盘实例，为什么不支持将付费类型从按量付费转换为Serverless？
A：由于Serverless实例为通用型规格的实例，[仅支持使用服务密钥（Default Service CMK）进行云盘加密](announcements-change-of-cloud-disk-encryption-instance-creation-from-january-15-2024.md)。
Q：按量付费转换为Serverless后，是否支持Sequence Engine?
A：支持，详情请参见[Sequence Engine](sequence-engine.md)。
