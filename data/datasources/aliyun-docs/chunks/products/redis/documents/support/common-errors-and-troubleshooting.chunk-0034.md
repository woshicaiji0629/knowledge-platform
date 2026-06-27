### BUSY Redis is busy running a script. You can only call SCRIPT KILL or SHUTDOWN NOSAVE.
可能原因：处理Lua脚本超时。
解决方法：通过SCRIPT KILL命令终止Lua脚本或等待Lua脚本执行结束，更多信息请参见[Lua](usage-of-lua-scripts.md)[脚本超时错误](usage-of-lua-scripts.md)。
