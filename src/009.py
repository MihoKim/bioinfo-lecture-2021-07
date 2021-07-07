

def greet():
    print("Hello, Bioinformatics")

def greet1(name: str) -> None:
    print(f"Hello {name}")

def greet2(num: int) -> int:
    return num*2

greet()
ret1=greet1('miho')     #return 되는 값이 없기 때문에 None
print(ret1)             
ret2=greet2(3)          #3*2 계산한 값이 return되어 ret2 변수에 저장됨  
print(ret2)             

