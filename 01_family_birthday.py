#这是第一个协作python练手程序

#目的：为家人计算阴历生日对应的年份的阳历生日

#内容：通过输入名字、出生日期、想要获取的年份，生成相应年份的阳历生日

#要求：格式化输出，不需要存储为文件，不需考虑异常处理代码

import datetime
from lunarcalendar import Converter,Lunar,Solar



#-----------------苗苗部分开始-----------------
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

#根据阴历生日查询对于年份的阳历日期（thisyeardate）

#格式化输出：$name在$the_year的生日是$thisyeardate




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