from time import sleep

y = None


def rob_print(y):
    for i in y:
        sleep(0.1)
        print(i, end='', flush=True)
    print('')