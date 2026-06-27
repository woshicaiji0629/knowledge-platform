## Pod常见操作
执行以下命令查看default命名空间下的所有Pods。
curl --cert ./client-cert.pem --key ./client-key.pem -k $APISERVER/api/v1/namespaces/default/pods
执行以下命令创建Pod（JSON格式）。
cat nginx-pod.json { "apiVersion":"v1", "kind":"Pod", "metadata":{ "name":"nginx", "namespace": "default" }, "spec":{ "containers":[ { "name":"nginx", "image":"nginx:alpine", "ports":[ { "containerPort": 80 } ] } ] } } curl --cert ./client-cert.pem --key ./client-key.pem -k $APISERVER/api/v1/namespaces/default/pods -X POST --header 'content-type: application/json' -d@nginx-pod.json
执行以下命令创建Pod（YAML格式）。
cat nginx-pod.yaml apiVersion: v1 kind: Pod metadata: name: nginx namespace: default spec: containers: - name: nginx image: nginx:alpine ports: - containerPort: 80 curl --cert ./client-cert.pem --key ./client-key.pem -k $APISERVER/api/v1/namespaces/default/pods -X POST --header 'content-type: application/yaml' --data-binary @nginx-pod.yaml
执行以下命令查询Pod状态。
curl --cert ./client-cert.pem --key ./client-key.pem -k $APISERVER/api/v1/namespaces/default/pods/nginx
执行以下命令查询Pod日志。
curl --cert ./client-cert.pem --key ./client-key.pem -k $APISERVER/api/v1/namespaces/default/pods/nginx/log
执行以下命令查询Pod的metrics数据（通过metric-server API）。
curl --
