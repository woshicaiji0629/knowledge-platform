### 如何卸载已安装的logtail-ds、alibaba-log-controller等组件？
执行kubectl delete -R -f result卸载已安装的logtail-ds、alibaba-log-controller等组件。
重要
该命令会递归删除result目录中所有资源，若目录下存在其他资源请谨慎使用。
