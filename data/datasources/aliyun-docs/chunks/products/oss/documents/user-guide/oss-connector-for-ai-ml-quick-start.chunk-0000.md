## 部署环境
操作系统：Linux x86-64
glibc：>=2.17
Python：3.8-3.12
PyTorch： >=2.0
使用OSS Checkpoint功能需Linux内核支持userfaultfd
说明
以Ubuntu系统为例，您可以执行sudo grep CONFIG_USERFAULTFD /boot/config-$(uname -r)命令确认Linux是否支持userfaultfd，当返回结果中显示CONFIG_USERFAULTFD=y时，则表示内核支持。返回结果显示CONFIG_USERFAULTFD=n时，则表示内核不支持，即无法使用OSS Checkpoint功能。
