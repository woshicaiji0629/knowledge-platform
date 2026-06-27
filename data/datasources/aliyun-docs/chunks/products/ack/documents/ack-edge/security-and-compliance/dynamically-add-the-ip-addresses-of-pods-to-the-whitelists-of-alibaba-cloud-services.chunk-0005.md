## 使用ack-kubernetes-webhook-injector动态添加RDS白名单示例
在Pod副本控制器的Pod Spec中，您可以使用Annotation指定Pod需加入的RDS实例ID和RDS白名单分组名称。Pod创建时，ack-kubernetes-webhook-injector会将Pod的IP地址加入到白名单中，并且在Pod删除时移除规则。
Pod的Annotation需包括的RDS白名单如下：
RDS实例ID：ack.aliyun.com/rds_id
RDS白名单分组名称：ack.aliyun.com/white_list_name
本文以自动添加RDS白名单规则为例，展示如何使用ack-kubernetes-webhook-injector为Pod动态添加安全规则。
使用以下YAML示例创建一个Deployment，在其中的Pod定义中加入RDS实例ID和RDS白名单分组名称的Annotation。
apiVersion: apps/v1 kind: Deployment metadata: labels: app: inject-test name: inject-test spec: replicas: 1 selector: matchLabels: app: inject-test template: metadata: annotations: ack.aliyun.com/rds_id: <rm-wz9nanjcud75b****> ack.aliyun.com/white_list_name: <rds_group> labels: app: inject-test spec: containers: - command: - sleep - "3600" image: alpine:latest name: inject-test
执行以下命令，查看Pod的IP地址。
kubectl --kubeconfig .kube/config_sts_test -n inject-test get pod -o wide
预期输出：
NAME READY STATUS RESTARTS AGE IP NODE inject-test-68cc8f9bbf-gj86n 1/1 Running 0 22s 172.25.0.28 cn-hangzhou.xxx
预期输出中，Pod的IP地址为172.25.0.28。
登录[RDS](https://rdsnext.console.aliyun.com/?spm=5176.2020520152.nav-right.2.469016ddzrU6KW#/detail/rm-bp12685y16w4zjz9d/security/whiteList?region=cn-hangzhou)
