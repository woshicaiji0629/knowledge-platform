### 3. 设置优雅终止时间
在spec.template.spec中设置足够的终止宽限期，以确保 LoongCollector 有足够时间上传剩余日志。
spec: # ... 您现有的其他 spec 配置 ... template: spec: terminationGracePeriodSeconds: 600 # 10分钟优雅停止时间
