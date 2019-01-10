from sleepAffectCalcUnderthehood import processAlg


def main():
    # where the data will be entered
    iSleepAm = int(input("ideal sleep amount \n"))
    aSleepAm = int(input("avg sleep amount \n"))
    lSleepAm = int(input("amount slept previous night\n"))
    menialComponent = int(input("percentiage of time taken that can be done on autopilot\n"))
    timeTakenForTaskWithoutSleepDeficit = int(input("time task generaly takes without sleep deficit in minutes\n"))
    # method call
    processAlgrocessAlg.processAlgIdealDeviation(iSleepAm, aSleepAm, lSleepAm, menialComponent,
                                                 timeTakenForTaskWithoutSleepDeficit)


if __name__ == '__main__':
    main()
