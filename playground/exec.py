exec('print(dir())')

p_code = """
import random
firstDayOfMonth = None
thirdDayOfMonth = None
secondDayOfMonth = None


firstDayOfMonth = random.randint(1, 10)
thirdDayOfMonth = random.randint(firstDayOfMonth + 10, 28)
secondDayOfMonth = random.randint(firstDayOfMonth + 1, thirdDayOfMonth - 1)

print(firstDayOfMonth, thirdDayOfMonth, secondDayOfMonth)"""

exec(p_code)
