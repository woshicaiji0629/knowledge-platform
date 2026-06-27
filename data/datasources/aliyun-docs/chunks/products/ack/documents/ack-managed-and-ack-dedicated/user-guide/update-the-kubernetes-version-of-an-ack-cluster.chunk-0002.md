### 1. 前置检查
控制面升级前置检查包括检查废弃API、组件兼容性、集群状态等。
1.20及以上版本的集群会检查当前版本是否使用了[废弃](cluster-check-items-and-suggestions-on-how-to-fix-cluster-issues.md)[API](cluster-check-items-and-suggestions-on-how-to-fix-cluster-issues.md)。检查结果不影响升级流程，仅作为提示信息。建议在升级前完成修复，避免影响下一版本集群的正常运行。
在集群升级页面单击前置检查，提前扫描集群升级可能存在的潜在风险。检查完成后，在前置检查结果区域查看检查结果。示例如下。
结果正常：升级检查成功，继续执行升级。
结果异常：不影响当前集群的运行及集群状态。请参见解决方案完成修复。更多信息，请参见[集群检查项及修复方案](cluster-check-items-and-suggestions-on-how-to-fix-cluster-issues.md)。
