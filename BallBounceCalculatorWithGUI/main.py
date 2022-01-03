from breezypythongui import EasyFrame

class BallBounce(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Ball Bounce Calculator")

        ##Input Starting Height
        self.addLabel(text="Starting Height", row=0, column=0)
        self.startHeight = self.addIntegerField(value=0, row=0, column=1, width=10)

        ##Number of Bounces
        self.addLabel(text="Number of Bounces", row=1, column=0)
        self.numBounces = self.addIntegerField(value=0, row=1, column=1, width=10)

        ##Bounciness
        self.addLabel(text="Bounciness *Use Whole Number*", row=3, column=0)
        self.bounciness = self.addFloatField(value=0, row=3, column=1, precision=2, width=10)

        ##Output
        self.addLabel(text="Distance Traveled", row=5, column=0)
        self.Distance = self.addFloatField(value=0.00, row=5, column=1, width=10, precision=2, state="readonly")

        ##Output Button
        self.addButton(text="Calculate Distance", row=6, column=0, columnspan=2, command=self.calcBounces)


    ##Bounce Distance Calculator
    def calcBounces(self):
        ##Income Adjustments
        start = self.startHeight.getNumber()
        bounces = self.numBounces.getNumber()
        bounciness = self.bounciness.getNumber()
        newHeight = start
        totalDistance = start
        for i in range(bounces):
            newHeight = newHeight * (bounciness/100)
            totalDistance = totalDistance + (2 * newHeight)
            i - 1
        self.Distance.setNumber(totalDistance)


def main():
    BallBounce().mainloop()

if __name__ == "__main__":
    main()