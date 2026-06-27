| 参数 | 说明 | 示例值 |
| --- | --- | --- |
| entrypoint | 定义入口模板。 | main |
| repo_url | Git 仓库的 URL。 | https://github.com/ivan-cai/echo-server.git |
| repo_name | 仓库名称。 | echo-server |
| target_branch | 仓库的目标分支。 默认为 main。 | main |
| container_image | 要构建的镜像。格式如下： <ACR EE Domain>/<ACR EE 命名空间>/<仓库名>。 | test-registry.cn-hongkong.cr.aliyuncs.com/acs/echo-server |
| container_tag | 要构建的镜像 Tag。 默认为 v1.0.0。 | v1.0.0 |
| dockerfile | Dockerfile 目录和文件名。 项目根目录下的相对路径，默认为 ./Dockerfile 。 | ./Dockerfile |
| enable_suffix_commitid | 是否在镜像 Tag 后追加 Commit ID。 true：追加 false：不追加 默认值为 true。 | true |
| enable_test | 是否开启运行 Go Test 步骤。 true：开启 false：不开启 默认值为 true。 | true |
