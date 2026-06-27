# RDS实例间数据迁移
本文介绍如何使用数据传输服务（Data Transmission Service，简称DTS），实现RDS实例间的数据迁移。DTS支持结构迁移、全量数据迁移以及增量数据迁移，同时使用这三种迁移类型可以实现在自建应用不停服的情况下，平滑地完成数据库的迁移。
重要
本文以阿里云账号内的RDS实例间数据迁移为例，如果您需要进行跨阿里云账号的RDS实例间数据迁移，请参见[配置跨阿里云账号的任务](https://help.aliyun.com/zh/dts/user-guide/synchronize-or-migrate-data-across-alibaba-cloud-accounts)。
在使用[DTS](https://help.aliyun.com/zh/dts/product-overview/what-is-dts)前，请确保DTS有访问云资源的权限，详情请参见[授予](https://help.aliyun.com/zh/dts/user-guide/authorize-dts-to-access-alibaba-cloud-resources)[DTS](https://help.aliyun.com/zh/dts/user-guide/authorize-dts-to-access-alibaba-cloud-resources)[访问云资源的权限](https://help.aliyun.com/zh/dts/user-guide/authorize-dts-to-access-alibaba-cloud-resources)。
