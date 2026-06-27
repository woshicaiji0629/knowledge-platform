ditions的PodNeedUpgrade=true，表明对应的Pod需要升级。
（可选）预拉取镜像。
curl -X POST http://127.0.0.1:10267/openyurt.io/v1/namespaces/default/pods/nginx-daemonset-bwzss/imagepull
预期输出：
Image pre-pull requested for pod default/nginx-daemonset-bwzss
对该Pod进行升级并更新DaemonSet配置。
curl -X POST http://127.0.0.1:10267/openyurt.io/v1/namespaces/default/pods/nginx-daemonset-bwzss/upgrade
预期输出：
Start updating pod default/nginx-daemonset-bwzss
