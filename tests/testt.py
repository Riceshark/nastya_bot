from nastya_bot import first
from nastya_bot import second
from nastya_bot import third
from nastya_bot import second_add
from nastya_bot import generate_advice

advices_list = first + second + second_add + third
string = generate_advice()
print(any(substring in string for substring in advices_list))