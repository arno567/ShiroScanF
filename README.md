# shiroFscan
shiro反序列化批量ip快速检测脚本
魔改的https://github.com/sv3nbeast/ShiroScan之前的老版本
自行安装相关模块
1. 增加线程池快速扫描
2. 解决https检测问题
3. 将模块、key值、检测目标url添加到dnslog的头部，dnslog平台接收到解析信息后进行base64解码就能获得存在漏洞的ip地址，方便进行筛查和漏洞记录。
# 简单使用
1.修改第45行的dnslog地址
2.url.txt中写入目标地址列表，格式http://xxxx或者https://xxxxx
3.python3运行脚本即可


