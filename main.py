#name = "Nayem"
#Age = 37
#Student = "no"
#১. ভ্যারিয়েবল ও ডাটা টাইপ:

Nayem = True
Age = True
Student = False

print(Nayem)
print(type(Nayem))
print(Age)
print(type(Age))
print(Student)
print(type(Student))

#২. অ্যারিথমেটিক অপারেশন:
multiply = f"my age is 37, multiply 100 = {37*100} "
plus = f"my age is 37, plus 100 = {37+100} "
division = f"my age is 37, division 100 = {37/100} "
minus = f"my age is 37, minus 100 = {37-100} "

print(multiply)
print(plus)
print(division)
print(minus)

MyAge = 37
multiply = 100
plus = 100
division = 100
minus = 100

print(MyAge * multiply)
print (MyAge + plus)
print (MyAge / division)
print (MyAge - minus)

#৩. কম্পারিজন অপারেটর:
myage = 37
x = 18
print(myage == x)
print(myage != x)
print(myage > x)
print(myage < x)

#৪. লজিক্যাল অপারেটর:
x=5
print (x>3 and x == 5)
print (x != 5 or x < 10)
print (not(x == 5 or x < 1))

#৫. অ্যাসাইনমেন্ট অপারেটর:
y=10
y+=5
print(y)
y-=5
print(y)
y*=5
print(y)
y/=5
print(y)

#৬. আইডেন্টিটি অপারেটর:
data1  = [1,2,3]
data2 = [1,2,3]
d=data1
print(data1 is data2)
print(data1 is d)
print(data1 is not d)

#৭. মেম্বারশিপ অপারেটর
city = ['dhaka', "barishal", "coxbazar"]
print ("chitagong" in city)
print ("coxbazar" not in city)