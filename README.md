# sina_spider

[TOC]

## Spider 框架

* 聚焦爬虫
  * 采集历史数据
  * 采集实时数据
  * 多线程采集多话题数据

* 通用爬虫

    通用爬虫需要维护一张去重的表

* 存储模块

  * 数据库增删改查

    每个话题都要用一张表来维护

  * 维护一张去重表

  * 数据库属性设计



## 开发日志

### 搭建环境

**数据库配置**：MySQL 5.6.34-1( jumbo install mysql)

**python版本**：python2.7

**Django版本**： Django==1.8.2



**Django 环境搭建和配置**

```shell
pip install django==1.8.2 # 安装 1.8.2版本的 Django
mkdir spider_project && cd spider_project 
django-admin.py startproject django_spider # init Django project
cd django_project

python manage.py runserver 10.64.0.95:8000 # 设置开发机的 IP 和端口，并开始运行

```



**Mysql 安装和配置**

```
jumbo install mysql # 安装
vim /home/work/.jumbo/etc/mysql/my.cnf # 修改端口号，mysqld 下添character_set_server=utf8
sh /home/work/.jumbo/share/mysql/mysql.server start # 开启 MySQL 服务
sh /home/work/.jumbo/share/mysql/mysql.server stop # 关闭 MySQL 服务
cd /home/work/.jumbo/bin/ && mysqladmin -u root password root # 创建 root 用户，密码同用户名
mysql -u root -p # 登录 MySQL，输入密码 root
create database spider_db; # 创建数据库

```



**工程结构**

```
django_spider/
	manager.py # command-line utility 
	django_spider/ # actual Python package for your project
		__init__.py # python package flag
		settings.py # django setting
		urls.py     # URL declarations for this Django project
		wsgi.py     # 
		
django_spider/
├── db.sqlite3      	#
├── django_spider   	# actual Python package for your project
├── ├── __init__.py  	# python package flag
├── ├── settings.py  	# django setting
├── ├── urls.py 	 	# URL declarations for this Django project
├── ├── wsgi.py
├── manage.py		 	# command-line utility 
└── spider			 	# my app
    ├── admin.py		
    ├── __init__.py		
    ├── migrations
    ├── └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
```



**Django 配置 MySQL 数据库**

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # 数据库引擎
        'NAME': 'spider_db',       # 你要存储数据的库名，事先要创建之
        'USER': 'root',         # 数据库用户名
        'PASSWORD': 'root',     # 密码
        'HOST': 'localhost',    # 主机
        'PORT': '3306',         # 数据库默认使用的端口
        }
}
```

