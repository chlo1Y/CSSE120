def main():
    hey()
    eatyourfinger()
    hey()
    hey()

    print('------------------           ---------------------------')
    print('The remaining output comes from CALLING')
    print('the  hello_and_goodbye  FUNCTION.')
    print('---------------------------------------------')
    hey_and_eatyourfinger()


def hey():
    print('ri gui')


def eatyourfinger():
    print('Ahhh!')
    print('   Ciao!')
    print('   Whoops!')


def hey_and_eatyourfinger():
    hey()
    eatyourfinger()

main()
