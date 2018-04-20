def conversionTempCaF(c):
	f = c * 1.8 +32
	return f

def conversionTempFaC(f):
	c =  (f - 32)/1.8
	return c

print("60 °C es ", conversionTempCaF(60), " en Farenheit")
print("45 °f es ", conversionTempFaC(45), " en Celsius")
