#这是第二个协作python练手程序

#目的：在01程序中，只能一次输入一个家人在一个特定年份的阳历生日，如果人多，且需要查看很多年的话，程序需要输入多次，非常麻烦，需要进行迭代。

#内容：通过多次循环输入家人信息以及希望查询的年份范围，按格式输出每个人在特定年份的阳历生日

#要求：格式化输出，不需要存储为文件，不需考虑异常处理代码

import datetime
from lunarcalendar import Converter,Lunar,Solar



#-----------------苗苗部分开始-----------------
#提示循环输入家人信息，全部输入完成后再输入查询年份的时间范围


#-----------------苗苗部分结束-----------------






#-----------------jerry部分开始-----------------
#根据输入循环输出

#根据阴历生日查询对于年份的阳历日期（thisyeardate）

#格式化输出：$name在$the_year的生日是$thisyeardate




def convert_to_lunar(birth_date):
    # 将阳历生日转换为阴历
    solar_date = Solar(birth_date.year, birth_date.month, birth_date.day)
    lunar_date = Converter.Solar2Lunar(solar_date)
    return lunar_date

def convert_to_solar(lunar_date, target_year):
    # 将阴历生日转换为指定年份的阳历生日
    new_lunar_date = Lunar(target_year, lunar_date.month, lunar_date.day, lunar_date.isleap)
    new_solar_date = Converter.Lunar2Solar(new_lunar_date)
    return datetime.date(new_solar_date.year, new_solar_date.month, new_solar_date.day)

# 输入出生日期（阳历）
birth_date = datetime.date(1954, 6, 3)
lunar_birth_date = convert_to_lunar(birth_date)
print(f"阴历生日: {lunar_birth_date}")

# 输入目标年份
target_year = 2024
solar_birthday = convert_to_solar(lunar_birth_date, target_year)
print(f"在{target_year}年的阳历生日: {solar_birthday}")

#-----------------jerry部分结束-----------------