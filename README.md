# 

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

```

