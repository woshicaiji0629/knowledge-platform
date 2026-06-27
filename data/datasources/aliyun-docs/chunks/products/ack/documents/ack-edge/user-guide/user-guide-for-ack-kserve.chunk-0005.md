## （可选）步骤四：清理资源和卸载组件
为避免资源浪费，请在卸载ack-kserve️组件前删除集群内的KServe CR（Custom Resource ）及CRD（Custom Resource Definition）资源。
重要
删除CR和CRD资源之前，请确认业务不再使用CR和CRD资源。删除CRD资源会同步删除对应的CR资源，CR资源一旦删除将无法恢复。
确认业务不再使用后，再删除集群内所有的KServe CR资源。删除CR资源可能涉及以下命令：
