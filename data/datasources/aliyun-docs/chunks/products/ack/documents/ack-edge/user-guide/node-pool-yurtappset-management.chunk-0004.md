rkloadTweaks[*].tweaks.patches[*].operation | 指定需要在 path 上执行的操作（目前支持：add/remove/replace）。 | 否 |
| spec.workload.workloadTweaks[*].tweaks.patches[*].value | 指定修改后的最新取值（只对 add/replace 操作生效）。 | 否 |
| status.conditions | 表示 YurtAppSet 当前状态，包括节点池选中状态、workload 状态等。 |  |
| status.readyWorkloads | 表示 YurtAppSet 当前管理的 workload 中，所有副本都 ready 的 workload 数量。 |  |
| status.updatedWorkloads | 表示 YurtAppSet 当前管理的 workload 中，所有副本都已经更新到最新版本的 workload 数量。 |  |
| status.totalWorkloads | 表示 YurtAppSet 当前管理的 workload 数量。 |  |
