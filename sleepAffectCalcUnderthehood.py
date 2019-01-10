class processAlg():

    def processAlgIdealDeviation(idealsleeptime, avgweeksleeptime, lastnightsleeptime, menialComponent,
                                 taskTimeUnderIdealSleepConditions):
        # derives relevant variables from three initial points of data

        undersleep = 0
        totalweeksundersleeptime = 0
        if (idealsleeptime == lastnightsleeptime and idealsleeptime == avgweeksleeptime):
            undersleep = 0
            totalweeksundersleeptime = 0
        elif (idealsleeptime > lastnightsleeptime):
            undersleep = idealsleeptime - lastnightsleeptime
        elif (idealsleeptime < lastnightsleeptime):
            oversleep = avgweeksleeptime - lastnightsleeptime
        elif (idealsleeptime > avgweeksleeptime):
            totalweeksundersleeptime = ((idealsleeptime - avgweeksleeptime) * 7)
        elif (idealsleeptime < avgweeksleeptime):
            totalweeksoversleeptime = ((avgweeksleeptime - idealsleeptime) * 7)
        else:
            print("invalid")

        if (undersleep == 0 and totalweeksundersleeptime == 0):
            effect = 0
        elif (totalweeksundersleeptime < 3.5 or undersleep < .5):
            effect = .10
        elif (totalweeksundersleeptime < 7 or undersleep < 1):
            effect = .25
        elif (totalweeksundersleeptime <= 14 or undersleep <= 3):
            effect = .50
        elif (totalweeksundersleeptime <= 28 or undersleep <= 6):
            effect = .75
        else:
            effect = 1
        # derives the percentage effect on different components of tasks to be used for specific tasks from sleep information
        mentalComponent = (100 - menialComponent)
        menialEffect = menialComponent * 2 * effect
        mentalEffect = mentalComponent * 6 * effect
        totaleffectratio = (menialEffect + mentalEffect) / 100
        # takes the percentages derived in generalaffectalg and multiplies each percentage affect by it's components percentage composition then adds them together for a final effect ratio
        taskTime = taskTimeUnderIdealSleepConditions + taskTimeUnderIdealSleepConditions * totaleffectratio
        print("\n")
        print(taskTime)
        # multiplies the ratio obtained in specificAffectAlg by the unmodified task time to obtain current task completion time
