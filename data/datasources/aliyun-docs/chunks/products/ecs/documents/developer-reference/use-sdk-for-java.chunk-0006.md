### 4. 异常处理
Java SDK将异常进行了细致的分类，主要划分为TeaUnretryableException和TeaException。
TeaUnretryableException：主要是因为网络问题造成，一般是网络问题达到最大重试次数后抛出。
TeaException：主要以业务报错为主的异常。
建议采取合理的措施来处理异常，比如合理地传播异常、记录日志、尝试恢复等，以确保系统的健壮性和稳定性。
