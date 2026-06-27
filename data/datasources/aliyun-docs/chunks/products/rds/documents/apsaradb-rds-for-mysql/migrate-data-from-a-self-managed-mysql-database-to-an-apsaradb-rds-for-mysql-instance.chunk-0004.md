## 计费说明
使用DTS将自建MySQL迁移至RDS MySQL时，库表结构迁移、全量迁移和公网流量均免费，以下内容收费：
增量迁移：当配置迁移任务时选择了增量迁移，则在增量迁移正常运行期间计费（库表结构迁移和全量迁移运行期间、增量迁移暂停或失败期间均不收费）。
数据校验：当配置迁移任务时选择了数据校验，可能会产生[数据校验费用](https://help.aliyun.com/zh/dts/user-guide/billing-method-of-data-verification#task-2314652)。
