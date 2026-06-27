input artifact. # and put it at /tmp/message. - name: message path: /tmp/message container: image: alpine:latest command: [sh, -c] args: ["cat /tmp/message"]
执行以下命令，提交工作流。
argo submit artifact-passing.yaml
执行以下命令，查看工作流状态。
argo list
该文章对您有帮助吗？
反馈
