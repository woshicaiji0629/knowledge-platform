mountPath: /.docker securityContext: seccompProfile: type: Unconfined runAsUser: 1000 runAsGroup: 1000 resources: requests: memory: 4Gi cpu: 2 activeDeadlineSeconds: 1200 depends: run-test
模板中暴露的参数如下：
