## 指标说明
主机CPU、内存、负载、磁盘、网络等指标说明如下：
CPU相关指标

| 指标名 | 说明 | 单位 | 示例 |
| --- | --- | --- | --- |
| cpu_count | CPU 核数 | 个 | 2.0 |
| cpu_util | CPU 使用率，计算方式为排除 idle、wait、steal 后的占比 | 百分号（%） | 7.68 |
| cpu_guest_util | 客户时间（guest time）占比 | 百分号（%） | 0.0 |
| cpu_guestnice_util | Nice 进程客户时间（nice guest time）占比 | 百分号（%） | 0.0 |
| cpu_irq_util | 硬中断处理时间（Hard Irq time）占比 | 百分号（%） | 0.0 |
| cpu_nice_util | Nice 时间（Nice time）占比 | 百分号（%） | 0.0 |
| cpu_softirq_util | 软中断处理时间（Soft Irq time）占比 | 百分号（%） | 0.06 |
| cpu_steal_util | 等待宿主机 CPU 时间（Steal time）占比 | 百分号（%） | 0.0 |
| cpu_sys_util | 内核态（System time）占比 | 百分号（%） | 2.77 |
| cpu_user_util | 用户态（User time）占比 | 百分号（%） | 4.84 |
| cpu_wait_util | 等待 IO（Waiting time）占比 | 百分号（%） | 0.11 |

内存相关指标

| 指标名 | 说明 | 单位 | 示例 |
| --- | --- | --- | --- |
| mem_util | 内存使用率 | 百分号（%） | 51.03 |
| mem_cache | 已申请但未使用的内存 | byte | 3566386668.0 |
| mem_free | 未使用的内存 | byte | 177350084.0 |
| mem_available | 可用内存 | byte | 3699885553.0 |
| mem_used | 已使用内存 | byte | 4041510463.0 |
| mem_swap_util | swap 内存使用率 | 百分号（%） | 0.0 |
| mem_total | 内存总量 | byte | 7919128576.0 |

磁盘相关指标
