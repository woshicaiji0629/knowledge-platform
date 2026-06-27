## 前提条件
已创建RAM用户，并对RAM用户授权。具体操作，请参见[创建](../../ram/documents/user-guide/create-a-ram-user.md)[RAM](../../ram/documents/user-guide/create-a-ram-user.md)[用户](../../ram/documents/user-guide/create-a-ram-user.md)和[授权](authorize-ram-users-to-operate-cloudlens-for-sls.md)[RAM](authorize-ram-users-to-operate-cloudlens-for-sls.md)[用户操作](authorize-ram-users-to-operate-cloudlens-for-sls.md)[CloudLens for SLS](authorize-ram-users-to-operate-cloudlens-for-sls.md)。
已开启全局日志：错误日志、指标监控采集功能。具体操作，请参见[开启日志采集功能](enable-the-log-collection-feature-1.md)。
重要
为了构建实时资源配额水位监控，全局日志需开启：错误日志、指标监控；并且这两种全局日志需存储于同一Project内。
为了避免监控日志存放在业务Project导致监控占用Project的配额，可选择系统推荐的固定地域目标Project，如杭州地域：log-service-{用户ID}-cn-hangzhou。
