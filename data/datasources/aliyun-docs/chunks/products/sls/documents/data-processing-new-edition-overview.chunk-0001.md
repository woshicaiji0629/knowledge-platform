## 加工原理
日志服务提供的数据加工（新版）功能，通过托管实时数据消费的任务，结合日志服务SPL规则消费功能，实现对日志数据的实时加工处理。关于SPL规则细节请参考[SPL](user-guide/spl-syntax.md)[语法](user-guide/spl-syntax.md)，对应SPL的实时消费应用场景，SPL规则消费请参考[普通消费概述](overview-of-real-time-consumption.md)。
重要
数据加工功能基于日志服务实时消费接口，不依赖源LogStore的索引配置。
