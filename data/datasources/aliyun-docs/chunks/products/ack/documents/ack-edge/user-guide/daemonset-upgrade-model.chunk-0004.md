### OTA升级模型
OTA升级接口
边缘节点上的edge-hub组件提供了与OTA升级相关的REST APIs。
GET /pods
通过此接口可以获取节点上的Pod信息。可以通过Pod.status.conditions中的PodNeedUpgrade来检查Pod是否可以更新。
POST /openyurt.io/v1/namespaces/{ns}/pods/{podname}/imagepull
此接口允许用户触发特定的DaemonSet Pod的镜像拉取。路径参数{ns}和{podname}分别代表 Pod 的命名空间和名称。一些Pod镜像体积较大、启动时间长，可通过这个API进行预拉取，加速启动时间。
镜像拉取的接口仅支持集群为1.32-aliyun.1及以上的版本。
POST /openyurt.io/v1/namespaces/{ns}/pods/{podname}/upgrade
通过此接口允许触发特定的DaemonSet Pod的更新。路径参数{ns}和{podname}分别代表Pod的命名空间和名称。请根据实际需求对指定的Pod执行升级操作。
OTA升级使用示例
创建一个名为nginx-daemonset的DaemonSet，使用OTA升级模型，当DaemonSet的镜像更新后，节点上的Pod并不会自动更新，请在边缘节点上通过REST API来检查和触发Pod的升级。
cat <<EOF | kubectl apply -f - apiVersion: apps/v1 kind: DaemonSet metadata: name: nginx-daemonset annotations: apps.openyurt.io/update-strategy: OTA spec: selector: matchLabels: app: nginx updateStrategy: type: OnDelete template: metadata: labels: app: nginx spec: containers: - name: nginx image: nginx:1.19.4 EOF
OTA升级用例
登录边缘节点，查看节点上的所有Pod是否有升级需求。
curl http://127.0.0.1:10267/pods
若输出结果中default/nginx-daemonset-bwzss pod.Status.Conditions的PodNeedUpgrade=true，表明对应的Pod需要升级。
（可选）预拉取镜像。
curl -X POST http://127.0.0.1:10267/openyurt.io/v1/namespaces/default/pods/nginx-daemonset-bwzss/imagepull
