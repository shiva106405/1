import random
def ranstr1 ():
    rand_num=random.randint(0,2)
    if rand_num==0:
        fruit_color,fruit_type,fruit_quantity='green','pear','10'
    elif rand_num==1:
        fruit_color,fruit_type,fruit_quantity='red','apple','20'
    else:
        fruit_color,fruit_type,fruit_quantity='yellow','mango','30'
    global via_record1,via_record2,via_record3
    via_record1=fruit_color
    via_record2 = fruit_type
    return



