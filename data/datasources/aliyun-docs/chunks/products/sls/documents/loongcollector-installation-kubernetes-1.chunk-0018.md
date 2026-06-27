### 5. 应用配置并验证
执行以下命令部署变更：
kubectl apply -f <YOUR-YAML>
查看 Pod 状态，确认 LoongCollector 容器已成功注入：
kubectl describe pod <YOUR-POD-NAME>
若看到两个容器（业务容器 +loongcollector），且状态正常，则注入成功。
