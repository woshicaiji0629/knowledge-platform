## 影响
按量付费转Serverless会导致实例切换，请确保应用具有自动重连机制。自动重连机制需要在您的应用程序中设置。实例切换的影响请参见[实例切换的影响](untitled-document-1701914031929.md)。
按量付费转Serverless的实例，如果开启了PFS（performance schema），会导致内存占用率较高，进而影响RCU的弹降效率。
