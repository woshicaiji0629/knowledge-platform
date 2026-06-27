### Windows
CMD
在CMD中运行以下命令。
setx OSS_ACCESS_KEY_ID "YOUR_ACCESS_KEY_ID" setx OSS_ACCESS_KEY_SECRET "YOUR_ACCESS_KEY_SECRET"
运行以下命令，检查环境变量是否生效。
echo %OSS_ACCESS_KEY_ID% echo %OSS_ACCESS_KEY_SECRET%
PowerShell
在PowerShell中运行以下命令。
[Environment]::SetEnvironmentVariable("OSS_ACCESS_KEY_ID", "YOUR_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User) [Environment]::SetEnvironmentVariable("OSS_ACCESS_KEY_SECRET", "YOUR_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
运行以下命令，检查环境变量是否生效。
[Environment]::GetEnvironmentVariable("OSS_ACCESS_KEY_ID", [EnvironmentVariableTarget]::User) [Environment]::GetEnvironmentVariable("OSS_ACCESS_KEY_SECRET", [EnvironmentVariableTarget]::User)
参考上述方式修改系统环境变量后，请重启或刷新您的编译运行环境，包括IDE、命令行界面、其他桌面应用程序及后台服务，以确保最新的系统环境变量成功加载。
