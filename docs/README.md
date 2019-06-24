#2019/06/24

1. 创建django 2.2.2开发框架，要求如下：
    * 使用django restful framework来写后台api。
    * 开发框架下支持多个环境，如测试，开发，生产，所以要设置不同的配置文件，这方面可以根据jumpserver源代码参考来写。
    * 将views.py系统文件改成包类型。

2. apps目录说明：
    * django2_framework为project级别。
    * 其他目录为app级别（如app_demo1和app_demo2）或自定义包级别（如common）用来存放公共工具之类的。
    
3. apps/app_demo1目录说明：
    * admin.py文件，这个用于后台管理此app下的model（也就是表），这个做成包后，在包里可以针对不同的表分别建一个文件，
      如有个价格表，那么就可以创建一个a_price.py文件（文件名规范先以a_xxx.py格式为准，其中a表示是在admin包下的文件），
      然后在admin包里的__init__.py文件中导入a_price.py中的类即可。
      
    * models.py文件操作和admin.py文件方式一样，文件名规范为m_xxx.py格式。
    
    * serializers.py文件操作和admin.py文件方式一样，文件名规范为s_xxx.py格式。
    
    * views.py文件操作和admin.py文件方式一样，文件名规范为v_xxx.py格式。
    
    * urls.py文件做成包后，里面文件名统一为api.py，api_v2.py, api_v3.py依次类推，这里是允许多版本的api共存的，涉及到的视图
      函数要变更的，那么文件名就要改为v_xxx_v2.py格式，涉及到其他文件的也需要修改。
      
4. data目录说明：暂时没用上，先预留目录。

5. logs目录说明：保存日志，只用于开发模式，因为在生产环境下会使用nginx+uwsig+supervisor来部署django应用。

6. requirements目录说明：用来存放pip包清单，还有其他包（如rpm）的依赖文件。

7. tmp目录说明：存放些临时文件。