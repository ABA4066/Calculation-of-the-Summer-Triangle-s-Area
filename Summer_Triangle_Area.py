import math
# Calculation of the Summer Triangle's Area
# The Summer Triangle is formed by Altair, Deneb, and Vega

ra1 = math.radians(19.84638849*15) #Right ascension of Altair(J2000)
dec1 = math.radians(8.868321194) #Declination of Altair(J2000)

ra2 = math.radians(20.69053198*15) #Right ascension of Deneb(J2000)
dec2 = math.radians(45.28033881) #Declination of Deneb(J2000)

ra3 = math.radians(28.61564899*15) #Right ascension of Vega(J2000)
dec3 = math.radians(38.78368894) #Declination of Vega(J2000)

a = math.acos(math.sin(dec1)*math.sin(dec2)+math.cos(dec1)*math.cos(dec2)*math.cos(abs(ra1-ra2))) #The edge between Altair and Deneb (Radian)

b = math.acos(math.sin(dec2)*math.sin(dec3)+math.cos(dec2)*math.cos(dec3)*math.cos(abs(ra2-ra3))) #The edge between Deneb and Vega (Radian)

c = math.acos(math.sin(dec3)*math.sin(dec1)+math.cos(dec3)*math.cos(dec1)*math.cos(abs(ra3-ra1))) #The edge between Altair and Deneb (Radian)


A = math.acos((math.cos(a) - math.cos(b) * math.cos(c)) / (math.sin(b) * math.sin(c))) #The angle formed by Vega, Altair and Deneb (radians)

B = math.acos((math.cos(b) - math.cos(a) * math.cos(c)) / (math.sin(a) * math.sin(c))) #The angle formed by Altair, Deneb and Vega (radians)

C = math.acos((math.cos(c) - math.cos(a) * math.cos(b)) / (math.sin(a) * math.sin(b))) #The angle formed by Deneb, Vega and Altair (radians)

E = A+B+C-math.pi #spherical excess (radians squared)

Area = E * 1**2
Area_deg2 = Area * (180 / math.pi)**2

print("The Summer Triangle's spherical area (J2000) is {:.2f} square degrees".format(Area_deg2))