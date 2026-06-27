## 示例
本文通过运行TensorFlow的分布式作业来展示Gang scheduling的效果。当前测试集群有4个GPU卡。
安装Arena，在Kubernetes集群中部署Tensorflow作业运行环境。具体操作，请参见[安装](../../cloud-native-ai-suite/user-guide/install-arena.md)[Arena](../../cloud-native-ai-suite/user-guide/install-arena.md)。
说明
Arena是基于Kubernetes的机器学习系统开源社区Kubeflow中的子项目之一。Arena用命令行和SDK的形式支持了机器学习任务的主要生命周期管理（包括环境安装、数据准备，到模型开发、模型训练、模型预测等），有效提升了数据科学家工作效率。
使用以下模板向集群中提交Tensorflow分布式作业，含有1个PS和4个Worker，每个Worker类型的Pod需要2个GPU。
展开查看完整示例
apiVersion: "kubeflow.org/v1" kind: "TFJob" metadata: name: "tf-smoke-gpu" spec: tfReplicaSpecs: PS: replicas: 1 template: metadata: creationTimestamp: null labels: pod-group.scheduling.sigs.k8s.io/name: tf-smoke-gpu pod-group.scheduling.sigs.k8s.io/min-available: "5" spec: containers: - args: - python - tf_cnn_benchmarks.py - --batch_size=32 - --model=resnet50 - --variable_update=parameter_server - --flush_stdout=true - --num_gpus=1 - --local_parameter_device=cpu - --device=cpu - --data_format=NHWC image: registry.cn-hangzhou.aliyuncs.com/kubeflow-images-public/tf-benchmarks-cpu:v20171202-bdab599-dirty-284af3 name: tensorflow ports: - containerPort: 2222 name: tfjob-port resources: limits: cpu: '1' workingDir: /opt/tf-benchmarks/scripts/tf_cnn
