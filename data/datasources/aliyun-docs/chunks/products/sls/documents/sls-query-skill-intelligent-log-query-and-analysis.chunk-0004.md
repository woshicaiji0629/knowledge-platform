## 方式一（推荐）：通过 npx 命令安装
npx 命令随 Node.js 一起提供。安装前，执行以下命令确认本地环境可用：
node -v npx -v
如果终端提示node或npx不存在，请先前往[Node.js 官网](https://nodejs.org/)下载并安装。
执行以下命令安装 alibabacloud-sls-query Skill：
npx skills add aliyun/alibabacloud-aiops-skills --skill alibabacloud-sls-query
安装完成后，确认 skills 目录下存在alibabacloud-sls-query目录，然后重启 Agent 使 Skill 生效。
