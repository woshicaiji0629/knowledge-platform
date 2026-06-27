e, rejected) (irate(apiserver_admission_webhook_admission_duration_seconds_bucket{type="validating"}[$interval])) ) | 使用到的 admit 类型的 Webhook 名称、操作、是否拒绝以及相应的执行时间。 指标 Bucket 的阈值为 {0.005、0.025、0.1、0.5、2.5} 。单位：秒。 |
| 准入 Webhook 请求 QPS | sum(irate(apiserver_admission_webhook_admission_duration_seconds_count[$interval]))by(name,operation,type,rejected) | 准入 Webhook 的请求 QPS。 |
