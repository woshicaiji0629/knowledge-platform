## 工作原理
回源301/302跟随功能指CDN节点在回源请求资源时，若收到源站返回的301/302状态码，CDN节点会直接跳转到Location地址获取资源，而不会将301/302状态码返回给用户。
用户请求访问http://example.com/examplefile.txt文件。
CDN节点上未缓存该文件，回源请求。
源站返回301/302状态码，Location地址为http://www.example.org/examplefile.txt。
CDN节点收到源站的响应后，向Location地址http://www.example.org/examplefile.txt发起请求获取资源。
CDN节点获取到所需资源后，缓存到CDN节点上。
CDN节点将获取到的资源返回给用户。
此时，如果其他用户再请求访问http://example.com/examplefile.txt文件，会直接在CDN节点命中缓存并返回给用户。
