## ossutil
使用命令行工具ossutil前，请先[安装](../install-ossutil2.md)[ossutil](../install-ossutil2.md)。
以使用 cp 命令下载对象为例，请指定--request-payer=requester参数
ossutil cp oss://examplebucket/examplefile.txt /localpath --request-payer=requester
