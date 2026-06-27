### No more cluster attempts left
可能原因：JedisCluster在API超时之后会默认重试5次（MaxAttempts，默认为5），并且在均失败之后抛出此错误。
解决方法：适当增大超时时间或进行[实例诊断](../user-guide/create-a-diagnostic-report.md)。
