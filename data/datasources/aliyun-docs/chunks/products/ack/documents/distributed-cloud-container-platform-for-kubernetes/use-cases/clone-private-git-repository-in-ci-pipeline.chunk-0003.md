## 方法一：基于Argo Workflows Git Artifact与用户名密码
该方法主要是在执行构建CI Pipeline的操作前，先执行Git Clone私有仓库操作，再进行Git Checkout操作。
以下YAML为了方便展示，和上文[预置工作流模板](building-a-ci-pipeline-of-golang-project-based-on-workflow-cluster.md)内容相比，仅保留了上述CI Pipeline中的git-checkout-pr任务（其他方法均相同），基于此增加git-clone任务，并设置git-checkout-pr依赖git-clone。
git-checkout-pr的command中，shell script无需修改。
git-clone的artifacts中引用保存的私有仓库凭据的git-credssecret中的用户名、密码。
