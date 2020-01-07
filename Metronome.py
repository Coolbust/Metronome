import time
import winsound


def main(bpm = 120, bpb = 4):
        sleep = 60.0 / bpm
        counter = 0
        while True:
            counter += 1
            if counter % bpb:
                print('tick')
                winsound.PlaySound("*",winsound.SND_ASYNC)
            else:
                print('TICK')
                winsound.PlaySound("SystemExit", winsound.SND_ASYNC)

            time.sleep(sleep)

main()
