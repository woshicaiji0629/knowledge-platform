## 使用自动轮转密钥开启Secret落盘加密
您可以使用KMS自动轮转密钥功能进行Secret的落盘加密。当密钥发生自动轮转时，存量的Secret仍旧使用轮转前的密钥版本进行加密，新增的Secret将使用轮转后的新密钥版本进行加密。关于自动轮转密钥具体操作，请参见[密钥轮转](../../../../kms/documents/key-management-service/user-guide/configure-key-rotation.md)。
如需确保存量的Secret也使用新的密钥版本进行加密，请在密钥发生自动轮转后，执行以下命令强制使用新的密钥版本重新加密所有的存量Secret。
kubectl get secrets --all-namespaces -o json | kubectl annotate --overwrite -f - encryption-key-rotation-time="$(date -u +'%Y-%m-%dT%H:%M:%S%z')"
