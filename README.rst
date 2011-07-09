ims -- inventoy management system
=================================

:Authors: simon.yang.sh <at> gamil <dot> com   
:Version: 0.1 of 2011/07

.. contents::

简述
~~~~~~~~~~
本项目出于学习目的，是一个货物管理的系统。

计划分以下两步来实现:

* 研究和实现web通用技术，其中包括：

  * Flask : A micro web framework
  * Extentions for Flask: SQLAlchmey, Login, Testing, Uploads, debuggertoolbar
  * SQLite3
  * jQuery/CSS/XHTML

* 融合上述技术，实现Ims

  * Login/Logout/Register
  * Product CURD
  * Printing
  * Management 
  * Deplyment

依赖
~~~~~~~~

  * Python
  * SQLite3
  * SQLAlchmey
  * feedparser
  * python-wtforms
  * python-markdown
  * python-profiler: pstats

    commands::

    sudo  apt-get install python sqlite3 python-sqlalchemy python-feedparser python-wtforms python-markdown python-profiler
 

部署
~~~~~~~~

  * Sanity Check run.py

    * download source code
    * install all above requirements
    * do setup in settings, like project directory
    * run #python run.py

  * lighttp/flup/fcgi

    * apt-get install lighttp python-flup
    * move source flask-ims to /var/www
    * grant flask-ims with user www-data  access
    * append fcgi.conf to lighttpd.conf
    * restart lighttp services
    * access: http://hostname/ims
   
  * cgi sitll not work
    

其他
~~~~~~~~

  * 工具

    * py.sh : 格式化代码
    * sub.sh : 提交代码
