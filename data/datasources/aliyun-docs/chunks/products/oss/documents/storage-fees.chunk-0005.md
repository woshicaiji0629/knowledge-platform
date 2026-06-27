### 不足规定时长容量（本地冗余）

| 计费项 | 计费项 Code | 最低存储时长计算方法 |
| --- | --- | --- |
| 低频访问（本地冗余）不足规定时长容量 | LessthanMonthDatasize | 以文件存储在 OSS 的 Last Modified 时间开始计算 |
| 归档存储（本地冗余）不足规定时长容量 | LessthanMonthDatasize |  |
| 冷归档存储（本地冗余）不足规定时长容量 | EarlyDeletionCA | 以文件转为冷归档或者深度冷归档类型的时间开始计算 |
| 深度冷归档存储（本地冗余）不足规定时长容量 | EarlyDeletionDeepCA |  |

为避免产生不足规定时长容量费用，您需要了解不同存储类型Object的最低存储时长计算方法，确保满足其最低存储时长后再进行转储或者删除。更多信息，请参见[如何避免产生存储不足规定时长容量费用？](how-can-i-avoid-the-cost-of-insufficient-storage.md)。
