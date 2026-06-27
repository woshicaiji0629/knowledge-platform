# Vim编辑器-云服务器 ECS(ECS)-阿里云帮助中心

Source: https://help.aliyun.com/zh/ecs/user-guide/use-the-vim-editor

# Vim编辑器
Vim是Linux中常见的文本编辑工具，在日常系统运维、编写Shell脚本等场景中会经常用到。本文介绍Vim编辑器的基本命令和模式切换，帮助您快速上手使用Vim编辑器。
## 安装情况
Linux系统都已经默认安装Vim工具，您无需进行安装。在终端中输入vim --version查看Vim版本信息。本文档以vim 8.0版本为例进行介绍，其他版本可能存在差异，请参考使用。
VIM - Vi IMproved 8.0 (2016 Sep 12, compiled Aug 10 2022 11:26:47) Included patches: 1-1763 Modified by OpenAnolis Community Compiled by OpenAnolis Community Huge version without GUI. Features included (+) or not (-): +acl +farsi +mouse_sgr -tag_any_white ......
## 模式切换
使用命令vim filename打开文件，即进入普通模式。如果文件不存在，Vim会新建一个文件。Vim的各个模式及切换方法如下所示。
| 模式 | 作用 | 模式转换 |
| --- | --- | --- |
| 普通模式 （Normal Mode） | 在该模式下，您可以复制、粘贴、删除字符或行。 | 运行 vim <文件名> 打开文件时，即进入普通模式。 在其他四个模式下，按 Esc 键即进入普通模式。 |
| 插入模式 （Insert Mode） | 在该模式下，您可以插入字符。 | 在普通模式下，按 i,I,a,A,o,O 中任一字符即进入插入模式。 说明 进入插入模式后，编辑器左下角会显示 -- INSERT -- 。 |
| 替换模式 （Replace Mode） | 在该模式下，您可以替换字符。 | 在普通模式下，按 R 即进入替换模式。 说明 进入替换模式后，编辑器左下角会显示 -- REPLACE -- 。 |
| 可视模式 （Visual Mode） | 在该模式下，您可以选择文本。命令（如，复制、替换、删除等）仅作用于选中的文档。 | 在普通模式下，按 v 即进入可视模式。 说明 进入可视模式后，编辑器左下角会显示 -- VISUAL -- 。 |
| 命令模式 （Command Mode） | 在该模式下，您可以查找字符串、替换字符串、显示行号、保存修改、退出编辑器等。 | 在普通模式下，按 : 即进入命令模式。 |
## 基本命令
### 打开文件
vim filename：打开单个文件。进入普通模式，如果文件不存在，Vim会新建一个文件。
vim filename1 filename2： 打开多个文件。
默认进入第一个filename1，正常编辑并使用:w保存filename1后，输入:bn进入下一个filename2，正常编辑并使用:w保存filename2。
输入:bp进入前一个filename1。
输入:ls可以查看编辑列表。
:open filename3：在Vim的命令模式下打开一个新的文件进行编辑。执行该命令前，请先使用:w保存原编辑文件。
### 移动光标
在普通模式下
方向键上/k：光标向上移动。
方向键下/j：光标向下移动。
方向键左/h：光标向左移动。
方向键右/l：光标向右移动。
在插入模式下
只能通过上、下、左、右方向键移动光标。
### 插入内容
在普通模式下，按i,I,a,A,o,O中任一字符即可进入插入模式。
i：在当前字符的左边插入。
I：在当前行的行首插入 。
a：在当前字符的右边插入。
A：在当前行的行尾插入。
o：在当前行下面插入一个新行。
O：在当前行上面插入一个新行。
### 复制和粘贴
类似于Word文档编辑器里Ctrl+C和Ctrl+V。在普通模式下：
yy：复制光标所在的行内容。可以直接使用p进行粘贴。
nyy：n为数字。例如2yy，复制光标所在行和下一行内容，即复制2行。
p：粘贴到光标所在的下一行。
P：粘贴到光标所在的上一行。
### 删除
在普通模式下
删除单个字符：按键盘x键删除当前光标所在位置的字符。
删除整行：按键盘dd删除当前行。类似于Word文档编辑器里Ctrl+X，可以直接使用p进行粘贴。
删除上一行：按键盘dk删除当前行和上一行。
删除下一行：按键盘dj删除当前行和下一行。
dG：按键盘dG删除当前行至文档末尾。
nx： n为数字。删除光标高亮的字符及其后面的n-1个字符。
ndd：n为数字。删除光标所在行及其下面的n-1行。类似于Word文档编辑器里Ctrl+X，可以直接使用p进行粘贴。
在插入模式下
将光标移动到想要删除内容的右侧，键入Delete键。
### 查询
在普通模式下
/text：查询text，默认精确匹配，回车后高亮显示命中字符。
如果要忽略大小写进行查询，先执行:set ignorecase。执行:set noignorecase返回精确匹配。
n：光标向下查询或下一个。
N：光标向上查询或上一个。
### 替换
在普通模式下
r：直接替换光标高亮的字符。
R：进入替换模式，连续替换光标高亮的字符，直至按下Esc键退出替换模式。
cc：直接删除光标所在的行，并进入插入模式。
:%s/oldtext/newtext/g：查询所有oldtext并替换为newtext。/g表示全部替换，若不加，则只替换所有行的第一个匹配。
在插入模式下
通过删除内容、插入内容的方式进行内容替换。
### 撤销与重做
在普通模式下
u：撤销插入或修改。类似于Word文档编辑器里的Ctrl+Z。
U：撤销对上一次行内容的所有插入和修改。
Ctrl+r：重做，即恢复撤销。相当于Word文档编辑器里的重做Ctrl+Y。
### 缩进与排版
在普通模式下
>>：整行向右缩进。默认值为8，即默认缩进一个制表符（Tab）的空格数。
<<：整行向左缩进。
在命令模式下
:ce：整行居中对齐。
:le：整行向左对齐。
:ri：整行向右对齐。
### 注释代码
说明
备份文件：在执行大范围替换操作前，建议备份文件或及时使用撤销功能（u）以防误操作。备份命令可参考sudo cp /etc/text.txt /etc/text.txt.bak。
正则表达式：确保理解 Vim 正则表达式的含义，避免意外删除不相关内容。在 Vim 的正则表达式中，/需要转义为\/。如果您对正则表达式不够熟悉，可以使用[Regex101](https://regex101.com/)等工具进行练习和调试。
不同语言的注释风格：根据具体使用的编程语言调整替换命令中的注释符。
在可视模式下
注释连续多行代码
上下移动光标选中待注释的行。
按:进入命令行模式，此时会自动填充:'<,'>，表示对选中的范围进行操作。
输入替换命令，例如要在每行前添加#，输入s/^/#/然后按Enter。
注释所有代码：输入替换命令:%s/^/#/g，全文使用#进行注释。
在插入模式下
手动插入注释符号的方式注释代码。
### 保存与退出
保存文件：在普通模式下输入:w并按下回车键。
退出 Vim：输入:q并按下回车键。
保存并退出：输入:wq或:x并按下回车键，或直接使用ZZ命令。
强制退出不保存：输入:q!并按下回车键。
强制退出并保存：输入:wq!并按下回车键。
### 加密文档
对文档进行加密：vim -x filename。自行设置密码后，进入普通模式。注意必须保存一次，否则加密不会生效。再次进入时需要进行密码验证。
取消文档加密。
在 Vim 中，执行命令:set key=取消加密。这条命令将清空当前文件的加密密钥，从而移除加密设置。
使用:wq命令保存并退出。
再次执行vim filename打开文件，不再出现密码验证提示。
### 执行命令
!pwd：在不退出Vim情况下，显示当前工作目录。
!ls：在不退出Vim情况下，列出当前目录下的文件和文件夹。
### 多窗口编辑
vim -o filename1 filename2：同时打开两个窗口显示文件。退出时需要分别执行退出命令。
:n：切换到另一个文件窗口，进行编辑。
:N：返回到上一个文件窗口，进行编辑。
### 帮助文档
在终端中输入vim --help查看Vim命令语法帮助信息。
在普通模式下
:help：查看Vim帮助文档。Vim帮助文档为只读，输入:q可退出帮助文档。
:help i：显示i的帮助文档。
:help yy：显示yy的帮助文档。
:set nu：显示行号。
## 示例
### 修改配置文件
在配置文件example.conf的第一行，插入Location。步骤如下：
运行vim example.conf命令打开文件，进入普通模式。
当前光标在该文件的第一个字符，按键盘i进入插入模式。
输入Location，按回车键换行。
按键盘Esc键退出插入模式。
输入:wq保存文件并退出。
### 在目标行插入内容
在配置文件example.conf第10行的行首，插入#。步骤如下：
运行vim example.conf命令打开文件，进入普通模式。
按键盘:10将光标定位到第10行。
按键盘i进入插入模式。
输入#。
按键盘Esc键退出插入模式。
输入:wq保存文件并退出。
### 查找并插入内容
在配置文件example.conf中，在Include conf.modules.d/*.conf行的下一行插入LoadModule rewrite_module modules/mod_rewrite.so。步骤如下：
运行vim example.conf命令打开文件，进入普通模式。
运行/Include conf.modules.d/*.conf找到目标行。
按键盘i进入插入模式。
输入LoadModule rewrite_module modules/mod_rewrite.so。
按键盘Esc键退出插入模式。
按:wq保存文件并退出。
### 删除内容
在配置文件example.conf中，将#Listen 12.34.XX:XX:80行首的#删除，并删除Listen 80。步骤如下：
运行vim example.conf命令打开文件，进入普通模式。
运行/#Listen 12.34.XX:XX:80找到目标，此时光标定位在#字符上。
按键盘x删除#。
光标移到Listen 80，按键盘dd删除该行。
输入:wq保存文件并退出。
### 编辑Docker.yaml
创建并编辑docker-compose.yaml文件，示例如下。
### 去除多行注释
假设注释#位于行首，可能有空格和缩进：
# This is a comment # Another comment # Yet another comment
执行以下命令：
:%s/^\s*#\s\?//
说明：
^：匹配行首。
\s*：匹配任意数量的空白字符（用于处理缩进）。
#：注释符号。
\s\?：匹配注释符后的一个可选空格。
//：表示将匹配到的内容替换为空，即删除。
命令会遍历整个文件，去除后文件如下所示：
This is a comment Another comment Yet another comment
## 升级Vim
如果当前操作系统的Vim不满足您的需求，您可以执行以下命令进行软件版本升级。
## Alibaba Cloud Linux 3/2
sudo yum update vim
## CentOS 7/8
sudo yum update vim
## Fedora
sudo yum update vim
## Ubuntu / Debian
sudo apt upgrade vim
## openSUSE
sudo zypper update vim
## 常见错误
退出时提示“No Write...”：
错误原因：文件有改动但没有保存。
解决方案：使用:wq保存并退出，或:q!放弃修改并退出。
无法输入文本：
错误原因：可能处于可视模式。
解决方案：按Esc键返回正常模式，然后进入插入模式。
无法保存文件：
错误原因：可能没有权限。当前用户对目标文件或其所在的目录没有写权限。例如，系统配置文件（如/etc/hosts、/etc/nginx/nginx.conf等）通常需要超级用户权限才能修改。
解决方案1：使用sudo命令以超级用户权限启动Vim。例如sudo vim example.conf。
解决方案2：使用:w !sudo tee %以管理员权限保存当前文件。如果需要变更配置文件的权限和归属，可进一步使用sudo chown或sudo chmod等命令。
存在“.swp”后缀文件：
错误原因：文件被其他Vim会话打开。
解决方案：确认没有其他终端正在编辑该文件，通过ll -a查询并删除.swp文件，然后再进行编辑；或者使用:recover命令进行恢复后进行编辑。
该文章对您有帮助吗？
反馈
### 为什么选择阿里云
[什么是云计算](https://www.aliyun.com/about/what-is-cloud-computing)[全球基础设施](https://infrastructure.aliyun.com/)[技术领先](https://www.aliyun.com/why-us/leading-technology)[稳定可靠](https://www.aliyun.com/why-us/reliability)[安全合规](https://www.aliyun.com/why-us/security-compliance)[分析师报告](https://www.aliyun.com/analyst-reports)
### 大模型
[千问大模型](https://www.aliyun.com/product/tongyi)[大模型服务](https://bailian.console.aliyun.com/?tab=model#/model-market)[AI应用构建](https://bailian.console.aliyun.com/app-center?tab=app#/app-center)
### 产品和定价
[全部产品](https://www.aliyun.com/product/list)[免费试用](https://free.aliyun.com/)[产品动态](https://www.aliyun.com/product/news/)[产品定价](https://www.aliyun.com/price/detail)[配置报价器](https://www.aliyun.com/price/cpq/list)[云上成本管理](https://www.aliyun.com/price/cost-management)
### 技术内容
[技术解决方案](https://www.aliyun.com/solution/tech-solution)[帮助文档](https://help.aliyun.com/)[开发者社区](https://developer.aliyun.com/)[天池大赛](https://tianchi.aliyun.com/)[阿里云认证](https://edu.aliyun.com/)
### 权益
[免费试用](https://free.aliyun.com/)[解决方案免费试用](https://www.aliyun.com/solution/free)[高校计划](https://university.aliyun.com/)[5亿算力补贴](https://www.aliyun.com/benefit/form/index)[推荐返现计划](https://dashi.aliyun.com/?ambRef=shouYeDaoHang2&pageCode=yunparterIndex)
### 服务
[基础服务](https://www.aliyun.com/service)[企业增值服务](https://www.aliyun.com/service/supportplans)[迁云服务](https://www.aliyun.com/service/devopsimpl/devopsimpl_cloudmigration_public_cn)[官网公告](https://www.aliyun.com/notice/)[健康看板](https://status.aliyun.com/)[信任中心](https://security.aliyun.com/trust-center)
### 关注阿里云
关注阿里云公众号或下载阿里云APP，关注云资讯，随时随地运维管控云服务
联系我们：4008013260
[法律声明](https://help.aliyun.com/product/67275.html)[Cookies 政策](https://terms.alicdn.com/legal-agreement/terms/platform_service/20220906101446934/20220906101446934.html)[廉正举报](https://aliyun.jubao.alibaba.com/)[安全举报](https://report.aliyun.com/)[联系我们](https://www.aliyun.com/contact)[加入我们](https://careers.aliyun.com/)
### 友情链接
[阿里巴巴集团](https://www.alibabagroup.com/cn/global/home)[淘宝网](https://www.taobao.com/)[天猫](https://www.tmall.com/)[全球速卖通](https://www.aliexpress.com/)[阿里巴巴国际交易市场](https://www.alibaba.com/)[1688](https://www.1688.com/)[阿里妈妈](https://www.alimama.com/index.htm)[飞猪](https://www.fliggy.com/)[阿里云计算](https://www.aliyun.com/)[万网](https://wanwang.aliyun.com/)[高德](https://mobile.amap.com/)[UC](https://www.uc.cn/)[友盟](https://www.umeng.com/)[优酷](https://www.youku.com/)[钉钉](https://www.dingtalk.com/)[支付宝](https://www.alipay.com/)[达摩院](https://damo.alibaba.com/)[淘宝海外](https://world.taobao.com/)[阿里云盘](https://www.aliyundrive.com/)[淘宝闪购](https://www.ele.me/)
© 2009-现在 Aliyun.com 版权所有 增值电信业务经营许可证：[浙B2-20080101](http://beian.miit.gov.cn/)域名注册服务机构许可：[浙D3-20210002](https://domain.miit.gov.cn/域名注册服务机构/互联网域名/阿里云计算有限公司 )
[浙公网安备 33010602009975号](http://www.beian.gov.cn/portal/registerSystemInfo)[浙B2-20080101-4](https://beian.miit.gov.cn/)
