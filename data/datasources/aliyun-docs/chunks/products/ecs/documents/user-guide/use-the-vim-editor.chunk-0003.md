### 打开文件
vim filename：打开单个文件。进入普通模式，如果文件不存在，Vim会新建一个文件。
vim filename1 filename2： 打开多个文件。
默认进入第一个filename1，正常编辑并使用:w保存filename1后，输入:bn进入下一个filename2，正常编辑并使用:w保存filename2。
输入:bp进入前一个filename1。
输入:ls可以查看编辑列表。
:open filename3：在Vim的命令模式下打开一个新的文件进行编辑。执行该命令前，请先使用:w保存原编辑文件。
