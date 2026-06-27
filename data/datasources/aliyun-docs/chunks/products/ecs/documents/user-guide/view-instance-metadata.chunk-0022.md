# 部署监控服务 sudo acs-plugin-manager --exec --plugin ACS-ECS-ImdsPacketAnalyzer # 查看监控服务状态 sudo systemctl status imds_tracer_tool
定位问题进程运行命令，查看哪些进程仍在以普通模式访问元数据。日志会显示相关进程的PID。
cat /var/log/imds/imds-trace.* | grep WARNING
分析并改造根据日志中的PID，找到对应的应用程序或脚本，并对其进行升级改造，通过加固模式访问元数据。
该文章对您有帮助吗？
反馈
