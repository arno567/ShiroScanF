# shiroFscan
shiro反序列化批量ip快速检测脚本
魔改的 https://github.com/sv3nbeast/ShiroScan 之前的老版本
自行安装相关模块
1. 增加线程池快速扫描 代码中第50行可以修改线程数
2. 解决https检测问题
3. payload中自动将模块、key值、检测目标url添加到dnslog的头部，dnslog平台会接收到存在漏洞的ip地址信息，方便进行筛查和漏洞记录。
4. 增加100key
# 简单使用
1. 下载文件解压
2. 在 https://github.com/sv3nbeast/ShiroScan 中下载ysoserial.jar放在目录下
3. 修改第47行的dnslog地址
4. url.txt中写入目标地址列表，格式 http://xxxx 或者 https://xxxxx:000
5. python3运行脚本 观察dnslog服务器即可
# 演示
![ys](https://github.com/arno567/shiroFscan/blob/master/ceshi.jpg)


