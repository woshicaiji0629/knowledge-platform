## 预置工作流模板说明
工作流集群中默认已经预置了名为ci-go-v1的CI工作流模板（ClusterWorkflowTemplate），其使用BuildKit Cache和NAS存储Go mode cache，可大幅加速CI Pipeline的流程。
您可以直接使用预置模板，也可以基于预置模板自定义自己的CI工作流模板。
预置的CI工作流模板中包含以下流程：
Git Clone & Checkout
用于Clone Git仓库，将Git仓库Checkout到目标分支。
获取Commit ID，在构建镜像时根据Commit ID追加Tag后缀。
Run Go Test
默认运行Git Repo（Go项目）中的所有测试用例。
可通过工作流参数enable_test控制是否运行该步骤。
其中Go mod cache存储在NAS的/pkg/mod目录，用于go test和后续的go build的加速。
Build & Push Image
使用BuildKit构建和推送容器镜像，并使用BuildKit Cache中registry类型的cache来加速镜像构建。
镜像Tag默认使用{container_tag}-{commit_id}格式，可在提交工作流时通过参数控制是否追加Commit ID。
推送镜像的同时，也会推送覆盖其latest版本镜像。
预置的CI工作流模板内容如下：
展开查看模板内容
apiVersion: argoproj.io/v1alpha1 kind: ClusterWorkflowTemplate metadata: name: ci-go-v1 spec: entrypoint: main volumes: - name: run-test emptyDir: {} - name: workdir persistentVolumeClaim: claimName: pvc-nas - name: docker-config secret: secretName: docker-config arguments: parameters: - name: repo_url value: "" - name: repo_name value: "" - name: target_branch value: "main" - name: container_image value: "" - name: container_tag value: "v1.0.0" - name: dockerfile value: "./Dockerfile" - name: enable_suffix_commitid value: "true" - name: enable_test value: "true" templates: - name: main
