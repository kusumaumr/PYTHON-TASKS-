#task --> str-int str-float str -complex
#int-str int-float int-complex
#float-str float-int float-complex

#int-str int-float int-complex
val=123
print(type(val))
print(val)
val=str(val)
print(type(val))
print(val)
val=float(val)
print(type(val))
print(val)
val=complex(val)
print(type(val))
print(val)

#float-str float-int float-complex
val1=3.14
print(type(val1))
print(val1)
val1=str(val1)
print(type(val1))
print(val1)
val1=int(val1)
print(type(val1))
print(val1)
val1=complex(val1)
print(type(val1))
print(val1)

#str-str str-int str-float str-complex
val2="123.45"
print(type(val2))
print(val2)
val2=str(val2)
print(type(val2))
print(val2)
val2=int(float(val2))
print(type(val2))
print(val2)
val2=float(val2)
print(type(val2))
print(val2)
val2=complex(val2)
print(type(val2))
print(val2)
