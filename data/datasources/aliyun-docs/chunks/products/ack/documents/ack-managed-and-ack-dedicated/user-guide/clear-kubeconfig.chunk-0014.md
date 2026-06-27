### 不能清除KubeConfig的场景有哪些？
集群状态异常：删除失败、删除中、已删除、失败四种状态的集群无法进行KubeConfig清除。
KubeConfig或证书状态异常：集群KubeConfig处于未颁发、已清除、未知状态的用户无法进行 KubeConfig清除。
用户无法清除自己的KubeConfig。
用户无法清除阿里云账号的KubeConfig。
