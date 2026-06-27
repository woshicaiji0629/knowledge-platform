## HSTS
HSTS（HTTP Strict Transport Security，HTTP 严格传输安全），是一种网站用来声明它们只能使用安全连接（HTTPS）访问的方法。网站可通过声明HSTS，来强制客户端（如浏览器）只能使用HTTPS与服务器连接，拒绝所有的HTTP连接并阻止用户接受不安全的SSL证书，降低第一次访问请求被拦截的风险。具体配置方法，请参见[配置](../user-guide/configure-hsts.md)[HSTS](../user-guide/configure-hsts.md)。
例如，未开启HSTS的情况下，当您源站使用HTTPS请求时，在浏览器输入HTTP链接，用户请求访问到服务器上的时候，服务器会将该HTTP请求301或302重定向到HTTPS，在用户请求以HTTP协议访问服务器的过程中，HTTP请求可能被恶意拦截或者篡改，存在安全隐患。开启了HSTS以后，客户端只能使用HTTPS协议访问服务器，这样就可以杜绝这类隐患。
