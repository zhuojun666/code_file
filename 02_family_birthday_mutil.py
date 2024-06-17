#这是第二个协作python练手程序

#目的：在01程序中，只能一次输入一个家人在一个特定年份的阳历生日，如果人多，且需要查看很多年的话，程序需要输入多次，非常麻烦，需要进行迭代。

#内容：通过多次循环输入家人信息以及希望查询的年份范围，按格式输出每个人在特定年份的阳历生日

#要求：格式化输出，不需要存储为文件，不需考虑异常处理代码

import datetime
from lunarcalendar import Converter,Lunar,Solar



#-----------------苗苗部分开始-----------------
#使用字典，将单一输入变为多轮输入，没轮输入完成时都询问“是否已经完成全部输入”，如输入为“Y”则视为完成；
#输入年份使用特定格式，即“起始年-终止年”

#提示输入name、born_date、the_year
name=input('输入你的名字:')
#print("姓名："+name)
born_date=input('输入你的生日，例如：1954，6，3:')
#print("生日："+born_date)
the_year=input('输入年份:')
#print("年份："+the_year)


#-----------------苗苗部分结束-----------------






#-----------------jerry部分开始-----------------
#根据born_date计算阴历生日






def convert_to_lunar(birth_date):
    # 将阳历生日转换为阴历
    solar_date = Solar(birth_date.year, birth_date.month, birth_date.day)
    lunar_date = Converter.Solar2Lunar(solar_date)
    return lunar_date

def convert_to_solar(lunar_date, the_year):
    # 将阴历生日转换为指定年份的阳历生日
    the_year = int(the_year)
    new_lunar_date = Lunar(the_year, lunar_date.month, lunar_date.day, lunar_date.isleap)
    new_solar_date = Converter.Lunar2Solar(new_lunar_date)
    return datetime.date(new_solar_date.year, new_solar_date.month, new_solar_date.day)

# 输入出生日期（阳历）
born_year,born_month,born_day = map(int, born_date.split(','))
birth_date = datetime.date(born_year,born_month,born_day)
lunar_birth_date = convert_to_lunar(birth_date)
print(f"阴历生日: {lunar_birth_date}")

# 输入目标年份
#target_year = 2024
solar_birthday = convert_to_solar(lunar_birth_date, the_year)
print(f"{name}在{the_year}年的阳历生日: {solar_birthday}")

#-----------------jerry部分结束-----------------