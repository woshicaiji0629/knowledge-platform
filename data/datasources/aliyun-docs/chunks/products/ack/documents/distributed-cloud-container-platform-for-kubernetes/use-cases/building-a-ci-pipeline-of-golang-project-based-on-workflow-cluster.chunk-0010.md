## 操作步骤
本文以公共Git仓库为例为您介绍构建CI Pipeline的操作，如果您在工作流的CI Pipeline中使用的是私有Git仓库，则需要在CI流程中先成功Clone该私有仓库。具体的Clone操作，请参见[在](clone-private-git-repository-in-ci-pipeline.md)[CI Pipeline](clone-private-git-repository-in-ci-pipeline.md)[中](clone-private-git-repository-in-ci-pipeline.md)[Clone](clone-private-git-repository-in-ci-pipeline.md)[私有](clone-private-git-repository-in-ci-pipeline.md)[Git](clone-private-git-repository-in-ci-pipeline.md)[仓库](clone-private-git-repository-in-ci-pipeline.md)。
重要
保存容器镜像访问凭证的Secret和挂载的NAS存储卷都需要与最终提交的工作流在同一个命名空间下。
