"us-ascii" MIME-Version: 1.0 Content-Transfer-Encoding: 7bit Content-Disposition: attachment; filename="userdata.txt" #!/bin/bash mkdir test-userscript touch /test-userscript/userscript.txt echo "Created by bash shell script" >> /test-userscript/userscript.txt --//--
示例MIME multi-part文件包含cloud-init指令和一个Bash Shell脚本：
cloud-init指令创建一个文件 (/test-cloudinit/cloud-init.txt)，并写入Created by cloud-init。
Bash Shell脚本创建一个文件 (/test-userscript/userscript.txt)，并写入Created by bash shell script。
