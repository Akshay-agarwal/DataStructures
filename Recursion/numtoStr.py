def toStr(num,base):
  basestring = "01234567"
  if num < base:
    return basestring[num]

  else:
    return toStr(num//base,base)+basestring[num%base]

print(toStr(1234,8))
