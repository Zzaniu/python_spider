update-alternatives --config vim 可以让你在 python 和 python3 之间切换


一、"大数据时代"，数据获取的方式：

1. 企业生产的用户数据：大型互联网公司有海量用户，所以他们积累数据有天然的优势。
                有数据意识的中小型企业，也开始积累的数据。

2. 数据管理咨询公司：通常这样的公司有很庞大的数据采集团队，一般会通过市场调研、问卷调查、固定的样本检测，
        和各行各业的公司进行合作、专家对话（数据积累很多年了，最后得出科研结果）来采集数据。

3. 政府/机构提供的公开数据：政府通过各地政府统计上报的数据进行合并；机构都是权威的第三方网站。

4. 第三方数据平台购买数据：通过各个数据交易平台来购买各行各业需要的数据，根据获取难度不同，价格也会不同。

5. 爬虫爬取数据：如果市场上没有我们需要的数据，或者价格太高不愿意买，那么就可以招/做一个爬虫工程师，从互联网上定向采集数据。



二、什么是爬虫？

爬虫：就是抓取网页数据的程序。


三、爬虫怎么抓取网页数据：

网页三大特征：

-1. 网页都有自己唯一的URL（统一资源定位符）来进行定位
-2. 网页都使用HTML （超文本标记语言）来描述页面信息。
-3. 网页都使用HTTP/HTTPS（超文本传输协议）协议来传输HTML数据。

爬虫的设计思路：
-1. 首先确定需要爬取的网页URL地址。
-2. 通过HTTP/HTTP协议来获取对应的HTML页面。
-3. 提取HTML页面里有用的数据：
    a. 如果是需要的数据，就保存起来。
    b. 如果是页面里的其他URL，那就继续执行第二步。


四、为什么选择Python做爬虫？

可以做爬虫的语言有很多，如 PHP、Java、C/C++、Python等等...

- PHP 虽然是世界上最好的语言，但是他天生不是干这个的，而且对多线程、异步支持不够好，并发处理能力很弱。
            爬虫是工具性程序，对速度和效率要求比较高。

- Java 的网络爬虫生态圈也很完善，是Python爬虫最大的对手。但是Java语言本身很笨重，代码量很大。
    重构成本比较高，任何修改都会导致代码的大量变动。爬虫经常需要修改部分采集代码。

- C/C++ 运行效率和性能几乎最强，但是学习成本很高，代码成型比较慢。
        能用C/C++做爬虫，只能说是能力的表现，但是不是正确的选择。


- Python 语法优美、代码简洁、开发效率高、支持的模块多，相关的HTTP请求模块和HTML解析模块非常丰富。
        还有强大的爬虫Scrapy，以及成熟高效的 scrapy-redis分布式策略。
        而且，调用其他借口也非常方便（胶水语言）



五、课程介绍：

-1. Python的基本语法知识（已经搞定）

-2. 如何抓取HTML页面：
        HTTP请求的处理，urllib、urllib2、requests
        处理后的请求可以模拟浏览器发送请求，获取服务器响应的文件

-3. 解析服务器响应的内容
        re、xpath、BeautifulSoup4（bs4）、jsonpath、pyquery等
        使用某种描述性一样来给我们需要提取的数据定义一个匹配规则，
        符合这个规则的数据就会被匹配。

-4. 如何采集动态HTML、验证码的处理
    通用的动态页面采集：Selenium + PhantomJS(无界面)：模拟真实浏览器加载js、ajax等非静态页面数据
    Tesseract：机器学习库，机器图像识别系统，可以处理简单的验证码，复杂的验证码可以通过手动输入/专门的打码平台

-5 Scrapy框架：（Scrapy，Pyspider）
    高定制性高性能（异步网络框架twisted），所以数据下载速度非常快，
    提供了数据存储、数据下载、提取规则等组件。

-6 分布式策略 scrapy-reids：
    scrapy-redis，在Scrapy的基础上添加了一套以 Redis 数据库为核心的组件。
        让Scrapy框架支持分布式的功能，主要在Redis里做 请求指纹去重、请求分配、数据临时存储。


-7 爬虫 - 反爬虫 - 反反爬虫 之间的斗争：
    其实爬虫做到最后，最头疼的不是复杂的页面，也是晦涩的数据，而是网站另一边的反爬虫人员。

    User-Agent、代理、验证码、动态数据加载、加密数据。

    数据价值，是否值的去费劲做反爬虫。

    1. 机器成本 + 人力成本 > 数据价值，就不反了，一般做到封IP就结束了。
    2. 面子的战争....

    爬虫和反爬虫之间的斗争，最后一定是爬虫获胜！
    为什么？只要是真实用户可以浏览的网页数据，爬虫就一定能爬下来！




六、根据使用场景：分为 通用爬虫  聚焦爬虫


1.通用爬虫：搜索引擎用的爬虫系统。

-1目标：就是尽可能把互联网上所有的网页下载下来，放到本地服务器里形成备份，
        再对这些网页做相关处理（提取关键字、去掉广告），最后提供一个用户检索接口。

-2抓取流程：
    a) 首选选取一部分已有的URL，把这些URL放到待爬取队列。
    b) 从队列里取出这些URL，然后解析DNS得到主机IP，然后去这个IP对应的服务器里下载HTML页面，保存到搜索引擎的本地服务器。
        之后把这个爬过的URL放入已爬取队列。
    c) 分析这些网页内容，找出网页里其他的URL连接，继续执行第二步，直到爬取条件结束。

-3 搜索引擎如何获取一个新网站的URL：
    1. 主动向搜索引擎提交网址：http://zhanzhang.baidu.com/linksubmit/url
    2. 在其他网站里设置网站的外链。
    3. 搜索引擎会和DNS服务商进行合作，可以快速收录新的网站。

    DNS：就是把域名解析成IP的一种技术。

-4 通用爬虫并不是万物皆可爬，它也需要遵守规则：
Robots协议：协议会指明通用爬虫可以爬取网页的权限。
Robots.txt 只是一个建议。并不是所有爬虫都遵守，一般只有大型的搜索引擎爬虫才会遵守。
    咱们个人写的爬虫，就不管了。


-5 通用爬虫工作流程：爬取网页 - 存储数据 - 内容处理 - 提供检索/排名服务

-6 搜索引擎排名：
    1. PageRank值：根据网站的流量（点击量/浏览量/人气）统计，流量越高，网站也越值钱，排名越靠前。
    2. 竞价排名：谁给钱多，谁排名就高。


-7 通用爬虫的缺点：
    1. 只能提供和文本相关的内容（HTML、Word、PDF）等等，但是不能提供多媒体文件（音乐、图片、视频）和二进制文件（程序、脚本）等等。
    2. 提供的结果千篇一律，不能针对不同背景领域的人提供不同的搜索结果。
    3. 不能理解人类语义上的检索。


为了解决这个问题，聚焦爬虫出现了：

聚焦爬虫：爬虫程序员写的针对某种内容的爬虫。
面向主题爬虫，面向需求爬虫：会针对某种特定的内容去爬取信息，而且会保证信息和需求尽可能相关。


Python自带的模块：/usr/lib/python2.7/urllib2.py
Python的第三方模块： /usr/local/lib/python2.7/site-packages

urllib2 默认的 User-Agent：Python-urllib/2.7

User-Agent: 是爬虫和反爬虫斗争的第一步，养成好习惯，发送请求带User-Agent


response 是服务器响应的类文件，除了支持文件操作的方法外，还支持以下常用的方法：

# 返回 HTTP的响应码，成功返回200，4服务器页面出错，5服务器问题
print response.getcode()

# 返回 返回实际数据的实际URL，防止重定向问题
print response.geturl()

# 返回 服务器响应的HTTP报头
print response.info()


User-Agent 历史：

Mosaic 世界上第一个浏览器：美国国家计算机应用中心

Netscape 网景：Netscape（支持框架），慢慢开始流行....(第一款支持框架的浏览器)

Microsoft 微软：Internet Explorer（也支持框架）

第一次浏览器大战：网景公司失败..消失

Mozilla 基金组织：Firefox 火狐 - （Gecko内核）(第一款浏览器内核)

User-Agent 决定用户的浏览器，为了获取更好的HTML页面效果。

IE开了个好头，大家都开就给自己披着了个 Mozilla 的外皮

Microsoft公司：IE（Trident）

Opera公司：Opera（Presto）

Mozilla基金会：Firefox（Gecko）

Linux组织：KHTML （like Gecko）

Apple公司：Webkit（like KHTML）

Google公司：Chrome（like webkit）

其他浏览器都是IE/Chrome内核




# IE9 User-Agent
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)"

urllib 的 urlencode() 接收的参数是一个字典：
wd = {"wd" : "传智播客"}
urllib.urlencode(wd)

结果：wd=%E4%BC%A0%E6%99%BA%E6%92%AD%E5%AE%A2


Get 和 Post请求的区别：

Get : 请求的url会附带查询参数，
POST：请求的url不带参数

对于Get请求：查询参数在QueryString里保存
对于Post请求：查询参数在Form表单里保存


做爬虫最需要关注的不是页面信息，而是页面信息的数据来源。

AJAX 方式加载的页面，数据来源一定是JSON

拿到JSON，就是拿到了网页的数据

# 忽略未认证的证书（如12306网站）
context = ssl._create_unverified_context

~/.bash_profile文件中怎么写账号密码：
user="hugong2"
export user

passwd="wenjunai"
export passwd

# 代理用户名和密码用@把ip和port连接起来就OK
proxyhandler = urllib2.ProxyHandler({"http":"user:passwd@61.155.164.109:3128"})

source ~/.bash_profile 生效

# 获取系统变量
os.environ.get("keyword")


XPATH模糊查询：
//div[contains(@id, "qiushi_tag_")]     id是属性，后面是是属性值一部分，即可实现模糊匹配

谢耀宗邮箱：136085635@qq.com

MONGODB数据库基本操作：

# 启动
> mongod

# 进入MongoDB的shell
> mongo 

# 查看当前数据库
> db

# 查看所有数据库
> show dbs

# 连接到XXX数据库
> use XXX

# 查看yyy表里的数据
> db.yyy.find()
> db.yyy.findone()

# 删除当前数据库
> db.dropDatabase()

from selenium import webdriver
driver = webdriver.PhantomJS()
driver.get(url)
# 获取网页源码(js已加载，跟浏览器看到的一样)
html = driver.page_source
content = etree.HTML(html)
finger_value = content.xpath(r'//p/input[@name="fingerprint"]/@value')[0]
finger_value = int(finger_value)
driver.quit()


# lxml.etree._ElementStringResult类型
address=each.xpath('.//address/text()')[0]
# str类型
address = address.encode('utf-8')