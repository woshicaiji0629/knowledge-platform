{{ alert.dashboard }} 。 |
| alert_url | 告警的详细 URL 地址。 | string | https://sls.console.aliyun.com/lognext/project/test-xxxx/alert/alert-1617164106-940166 | 告警 URL 为 {{ alert.alert_url }} 。 |
| query_url | 查询统计中第一个查询页面的 URL 地址。 | string | https://sls.console.aliyun.com/lognext/project/test-xxx/logsearch/test-alert-access?encode=base64&endTime=1617175989&queryString=KiB8IHNlbGVjdCBjb3VudCgxKSBhcyBjbn****&queryTimeType=99&startTime=1617175089 | 查询统计中第一个查询页面的 URL 地址为 {{ alert.query_url }} 。 |
| alert_history_dashboard_url | 告警历史统计报表的 URL 地址。 | string | https://sls.console.aliyun.com/lognext/project/test-xx/dashboard/internal-alert-analysis | 告警历史统计报表的 URL 地址为 {{ alert.alert_history_dashboard_url }} 。 |
| dashboard_url | 告警关联的仪表盘地址。 | string | https://sls.console.aliyun.com/next/project/myproject/dashboard/mydashboard | 告警关联的仪表盘地址为 {{ alert.dashboard_url }} 。 |
| fingerprint | 告警指纹。更多信息，请参见 [基于告警指纹去重](deduplicate-alerts-based-on-fingerprints.md) 。 | string | 478325709134bc5c | 告警指纹为 {{ alert.fingerprint }} 。 |
| signin_url | 免登录控制台即可查看告警详情。更多信息，请参见 [免登录查看告警详情](view-alert-details-in-logon-free-mode.md) 。 | string | https://sls.console.aliyun.com/console/AlertAjax/slsSignIn.json?token=xxxx
