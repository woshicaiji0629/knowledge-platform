## 步骤三：创建Event Sensor
通过轻量消息队列（原 MNS）创建Eventbus时，在Event Sensor创建完成后，会自动创建一个轻量消息队列（原 MNS）与之对应，队列命名格式为：ackone-argowf-<namespace>-<sensor-name>-<sensor-uid>。
创建event-sensor.yaml文件，在Event Sensor中嵌入待执行的工作流定义。Event Sensor示例代码如下所示：
展开查看示例代码
apiVersion: argoproj.io/v1alpha1 kind: Sensor metadata: name: ali-mns spec: template: serviceAccountName: default dependencies: - name: test-dep eventSourceName: ali-mns # 匹配eventsource名称。 eventName: example # 匹配eventsource中的事件名称定义。 triggers: - template: name: mns-workflow k8s: operation: create source: resource: apiVersion: argoproj.io/v1alpha1 # 嵌入工作流定义。 kind: Workflow metadata: generateName: ali-mns-workflow- spec: entrypoint: whalesay arguments: parameters: # 参数传递事件内容。 - name: message # this is the value that should be overridden value: hello world templates: - name: whalesay inputs: parameters: - name: message container: image: docker/whalesay:latest command: [cowsay] args: ["{{inputs.parameters.message}}"] parameters: - src: # 解析事件内容，传递给工作流。 dependencyName: test-dep dataKey: body dest: spec.arguments.parameters.0.value
应用event-sensor.yaml文件创建Event Sensor。
kubectl apply -f event-sensor.yaml
查看Event Sensor Pod是否正常启动。
kubectl get pod
