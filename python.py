from random import choice, shuffle
from time import sleep

cores = {'azneg':'\033[1;34m',  #azul e negrito
         'vdneg':'\033[1;32m',  #verde e negrito
         'vmneg':'\033[1;31m',  #vermelho e negrito
         'clean':'\033[m'}      #limpa a formatação

#números que foram vendidos [rifa de chocolate e rifa de beleza]
rifa_chocolate = [
  001,002,003,004,005,007,008,009,010,
  011,012,013,014,015,016,017,018,019,
  028,029,030,031,040,042,077,086,088,
  090,101,102,103,104,105,112,116,117,
  118,119,120,121,122]
rifa_beleza = [
  001,002,003,004,005,006,007,008,009,
  010,011,012,013,014,015,016,017,018,
  019,020,021,022,023,024,025,026,027,
  028,029,030,031,032,033,034,035,036,
  037,038,054,065,099,130,131,151]

print('\033[1;44;37m', '=-='*14, '\033[m')
print('{}{:^38}{}'.format('\033[1;44;37m', ' |       RIFA       DA       DOGUINHA     | ', '\033[m'))
print('\033[1;44;37m', '=-='*14, '\033[m\n\n')

shuffle(rifa_chocolate)
escolhido_chocolate = choice(rifa_chocolate)
shuffle(rifa_beleza)
escolhido_beleza = choice(rifa_beleza)

print('\033[1mSORTEANDO OS NÚMEROS DA \033[1;34mCESTA DE CHOCOLATES\033[m')
sleep(4)
print('O \033[1;32mGANHADOR\033[m DA \033[1;34mCESTA DE CHOCOLATES\033[m')
sleep(2.5)
print('É O NÚMERO: {}{}{}\n\n\n'.format(cores['vdneg'], escolhido_chocolate, cores['clean']))
sleep(1)

print('\033[1mSORTEANDO OS NÚMEROS DA \033[1;34mRIFA DE BELEZA\033[m')
sleep(4)
print('O \033[1;32mPRIMEIRO GANHADOR\033[m DA \033[1;34mRIFA DE BELEZA\033[m')
sleep(2.5)
print('É O NÚMERO: {}{}{}\n\n\n'.format(cores['vdneg'], escolhido_beleza, cores['clean']))
sleep(1)
print('\033[1mSORTEANDO O \033[1;32mPRÓXIMO GANHADOR\033[m')
sleep(5)

shuffle(rifa_beleza)
escolhido_beleza = choice(rifa_beleza)

print('E O \033[1;32mSEGUNDO GANHADOR\033[m DA \033[1;34mRIFA DE BELEZA\033[m')
sleep(2.5)
print('É O NÚMERO: {}{}{}\n\n\n'.format(cores['vdneg'], escolhido_beleza, cores['clean']))
