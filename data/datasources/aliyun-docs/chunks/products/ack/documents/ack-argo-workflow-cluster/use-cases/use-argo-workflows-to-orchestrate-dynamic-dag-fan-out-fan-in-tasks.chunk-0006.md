ers/python-log-count command: [python] args: ["merge.py"] env: - name: NUM_PARTS value: "{{inputs.parameters.numParts}}" volumeMounts: - name: workdir mountPath: /mnt/vol outputs: artifacts: - name: result path: /mnt/vol/result.json
使用动态DAG方式实现Fan-out Fan-in编排任务。
大文件拆分为多个split子任务后，会在标准输出中输出一个JSON字符串，包含子任务要处理的partId，例如：
["0", "1", "2", "3", "4"]
map任务使用withParam引用split任务的输出，并解析JSON字符串获得所有{{item}}，并使用每个{{item}}作为输入参数启动多个map任务。
- name: map template: map arguments: parameters: - name: partId value: '{{item}}' depends: "split" withParam: '{{tasks.split.outputs.result}}'
更多定义方式，请参见[开源](https://argo-workflows.readthedocs.io/en/latest/walk-through/loops/)[Argo Workflow](https://argo-workflows.readthedocs.io/en/latest/walk-through/loops/)。
工作流运行后，您可以在[容器](https://csnew.console.aliyun.com/#/next/argowf)[Argo](https://csnew.console.aliyun.com/#/next/argowf)[工作流集群控制台](https://csnew.console.aliyun.com/#/next/argowf)查看任务DAG流程与运行结果。
阿里云OSS文件列表中，log-count-data.txt为输入日志文件，split-output，cout-output为中间结果目录，result.json为最终结果文件。
