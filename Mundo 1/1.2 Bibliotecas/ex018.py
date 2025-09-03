from math import sin,cos,tan,radians

ang = float(input("Digite um ângulo: "))
sen = sin(radians(ang)) #calcula o ang em radianos e depois calcula os outros
cos = cos(radians(ang))
tan = tan(radians(ang))

print("="*15)
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(sen,cos,tan))
print("="*15)