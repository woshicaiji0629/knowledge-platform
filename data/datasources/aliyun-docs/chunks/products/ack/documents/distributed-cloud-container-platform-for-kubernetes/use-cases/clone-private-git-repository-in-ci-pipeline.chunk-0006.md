## 方法二：基于Argo Workflows Git Artifact与SSH Private Key
和方法一基本相同，主要差异如下：
git-clone的artifacts中引用保存的私有仓库凭据的git-credssecret中的ssh private key。
在提交Workflow时，repo_url需要为ssh格式，例如：git@github.com:ivan-cai/gitops-demo-private.git。
