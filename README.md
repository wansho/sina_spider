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

1. python 虚拟开发环境搭建

   ```shell
   
   pip install virtualenv # 虚拟环境
   cd spider project # cd 到一个空目录，创建虚拟环境
   virtualenv --no-site-packages venv  # 创建一个虚拟的 python 开发环境，名字为 venv，其中默认不包含任何原环境的包，只有几个必要的包
   source venv/bin/activate # 进入该虚拟环境
   deactivate # 退出该虚拟环境
   ```

