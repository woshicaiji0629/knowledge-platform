明大页。 |
| khugepaged_alloc_sleep_millisecs | 当透明大页 THP 分配失败时， khugepaged 守护进程进行下一次大页分配前需要等待的时间，以避免短时间内连续发生大页分配失败。单位为毫秒。 | 请参见 [khugepaged](https://help.aliyun.com/zh/alinux/support/performance-tuning-method-related-to-transparent-large-page-thp-in#95896c5cd73ld) [碎片整理](https://help.aliyun.com/zh/alinux/support/performance-tuning-method-related-to-transparent-large-page-thp-in#95896c5cd73ld) 。 |
| khugepaged_scan_sleep_millisecs | khugepaged 守护进程每次唤醒的时间间隔。单位为毫秒。 |  |
| khugepaged_pages_to_scan | khugepaged 守护进程每次唤醒后扫描的内存页数量。单位为页。 |  |
