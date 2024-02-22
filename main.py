C=print
B=range
import string as A,random as D,requests as E,colorama
from colorama import Fore,Back,Style
def F(length=16):C=A.ascii_letters+A.digits;E=''.join(D.choice(C)for A in B(length));return E
def G(code):
  A={'Authorization':'Bot MTIwMjY4MTE3MjU5ODE5NDMxNg.GRmnRi.FiiJEafZJ9moxkAK2_hRYBQjL-qfuaYeVjPZmA'};B=E.post(f"https://discord.com/api/v9/entitlements/gift-codes/{code}/redeem",headers=A)
  if B.status_code==200:return True
  else:return False
def H():
  C(Fore.RED+'\n███████╗███████╗     ██████╗ ███████╗███╗   ██╗\n██╔════╝╚══███╔╝    ██╔════╝ ██╔════╝████╗  ██║\n█████╗    ███╔╝     ██║  ███╗█████╗  ██╔██╗ ██║\n██╔══╝   ███╔╝      ██║   ██║██╔══╝  ██║╚██╗██║\n███████╗███████╗    ╚██████╔╝███████╗██║ ╚████║\n╚══════╝╚══════╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝\n    '+Style.RESET_ALL);D=int(input('Enter the amount of codes :  '))
  for E in B(D):A=F();C(f"Generated code: {A}, Valid: {G(A)}")
if __name__=='__main__':H()
