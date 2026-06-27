## 方法三：基于Git Clone命令与用户名密码
和前两种方法不同，该方法不需要增加DAG（Directed Acyclic Graph）任务，但需要修改git-checkout-pr中git clone的命令，并通过env引用git-credssecret中的用户名、密码。命令如下：
git clone https://${GIT_USER}:${GIT_TOKEN}@github.com/${GITHUB_REPOSITORY}
