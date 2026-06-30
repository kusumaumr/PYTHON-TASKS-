#task :separate vowels and consonants in string "hi hello kusuma"
s="hi hello kusuma"
v=[vow for vow in s if vow in "aeiou"]
c=[con for con in s if con !=" " and con not in "aeiou"]
print(v)
print(c)


l=[[vow for vow in s if vow in "aeiou"] ,[con for con in s if con !=" " and con not in "aeiou"]]
print(l)


