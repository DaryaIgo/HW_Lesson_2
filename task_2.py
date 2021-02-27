my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

sec_p = my_list[1:2]
hour = int(sec_p[0])  # 5

four_p = my_list[3:4]
minutes = four_p[0]  # 17

six_p = my_list[8:9]
degrees = six_p[0]
plus = degrees[0]  # +
five = int(degrees[1])  # 5

first_p = my_list[:1]
str_first_p = first_p[0]

third_p = my_list[2:3]
str_third_p = third_p[0]

five_p = my_list[4:8]
str_five_p = " ".join(five_p)

seven_p = my_list[9:10]
str_seven_p = seven_p[0]

print(str_first_p, f'"{hour:02d}"', str_third_p, f'"{minutes}"', str_five_p, f'"{plus}{five:02d}"', str_seven_p)
