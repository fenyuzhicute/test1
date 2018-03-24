#endconding = utf-8
"""
Created by fenyuzhi on 2018/3/11
"""
menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}


now_layer = menu # 当前菜单
pre_layer=[] #上一级菜单

while True:
    for i in now_layer:
        print(i)
    user_opt = input("菜单选项>>").strip()
    if user_opt == None:
        continue
    elif user_opt == "q":
        exit()
    elif user_opt == "b":
        if now_layer == menu:#若当前节点已是初始菜单，则不返回
            continue
        else:
            now_layer = pre_layer.pop()#返回一级，上一级菜单变成当前菜单
    elif user_opt in now_layer:
        pre_layer.append(now_layer)#前进一级，当前菜单变为上一级菜单
        now_layer = now_layer[user_opt]#下一级菜单变为当前菜单