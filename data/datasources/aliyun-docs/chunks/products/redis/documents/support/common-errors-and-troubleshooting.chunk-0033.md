### NOSCRIPT No matching script. Please use EVAL.
可能原因：使用EVALSHA命令时，若SHA1值对应的脚本未缓存至Tair中。
解决方法：通过EVAL命令或SCRIPT LOAD命令将目标脚本缓存至Tair中后进行重试，更多信息请参见[NOSCRIPT](usage-of-lua-scripts.md)[错误](usage-of-lua-scripts.md)。
