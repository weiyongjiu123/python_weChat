# python_weChat

有关本文件夹下的代码说明

remind文件夹下的代码是做课表提醒<br>
app文件夹下的代码是公众号的后台

remind/crontab    是linux任务时间表<br>
app/weChatPublic.sql    是后台需要的mysql的数据库表

另外还需要设置公众号菜单按钮，按钮数据如下

{
  "button":[
    {
      "name":"开启提醒",
      "sub_button":[
        {
          "type":"click",
          "name":"当日提醒",
          "key":"setDayRemindOpen"
        },
        {
          "type":"click",
          "name":"课前提醒",
          "key":"setBeforeRemindOpen"
        }
      ]
    },{
      "name":"关闭提醒",
      "sub_button": [
        {
          "type":"click",
          "name":"当日提醒",
          "key":"setDayRemindClose"
        },{
          "type":"click",
          "name":"课前提醒",
          "key":"setBeforeRemindClose"
        }
      ]
    },{
      "name":"我的",
      "sub_button":[
        {
          "type":"click",
          "name":"提醒状态",
          "key":"getRemindStatus"
        },{
          "type":"click",
          "name":"查看课表",
          "key":"getSchedule"
        }
      ]
    }
  ]
}

