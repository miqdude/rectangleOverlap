class Rectangle:
    def __init__(self, x, y, width, height, id):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height
        self.id = id

# check the intersect of two rectangles
def isIntersect(rect1, rect2):
    # if rect2 is on the side of rect1
    if rect2.x1 > rect1.x2 or rect2.x2 < rect1.x1:
        return False

    # if the rect2 in either on top or below rect1
    if rect2.y1 > rect1.y2 or rect2.y2 < rect1.x1:
        return False

    return True

# check the intersection of a rectangle with combined rectangles
def isIntersectCombined(rectArr, rect):

    for rect1 in rectArr:
        if isIntersect(rect1, rect) == False:
            return False

    return True

def findMultipleIntersection(rectangleArr, rect):
    x1s = []
    y1s = []

    x2s = []
    y2s = []

    for r in rectangleArr:
        x1s.append(r.x1)
        y1s.append(r.y1)

        x2s.append(r.x2)
        y2s.append(r.y2)

    x1s.append(rect.x1)
    y1s.append(rect.y1)

    x2s.append(rect.x2)
    y2s.append(rect.y2)

    anchorPoints = (max(x1s), max(y1s))
    farPoints = (min(x2s), min(y2s))

    length = (farPoints[0] - anchorPoints[0], farPoints[1] - anchorPoints[1])

    return anchorPoints, length

# variable to store all of the possible rectangles
rectangleArr = []

inputRectangle = []

inputRectangle.append(Rectangle(100,100,250,80,1))
inputRectangle.append(Rectangle(120,200,250,150,2))
inputRectangle.append(Rectangle(140,160,250,100,3))
inputRectangle.append(Rectangle(160,140,350,190,4))

for rectangle in inputRectangle:
    if len(rectangleArr) == 0:
        rectangleArr.append([rectangle])
    else:
        # checking if the new rectangle is intersecting with existing rectangles
        newRects = []
        for rectangleCheck in rectangleArr:
            if isIntersectCombined(rectangleCheck, rectangle):
                if len(rectangleCheck) == 1:
                    print("Between rectangle {} and {} ".format(rectangleCheck[0].id, rectangle.id), end= "")
                    
                    intersectAnchorPoint, intersectLength = findMultipleIntersection(rectangleCheck, rectangle)
                    print("at {}, w={}, h={}.".format(intersectAnchorPoint, intersectLength[0], intersectLength[1]))
                else:
                    print("Between rectangle ", end = "")
                    for i,r in enumerate(rectangleCheck):
                        if i == len(rectangleCheck)-1:
                            print("{}".format(r.id), end = "")
                        else:
                            print("{}, ".format(r.id), end = "")

                    print(" and {} ".format(rectangle.id), end = "")

                    intersectAnchorPoint, intersectLength = findMultipleIntersection(rectangleCheck, rectangle)
                    print("at {}, w={}, h={}.".format(intersectAnchorPoint, intersectLength[0], intersectLength[1]))
                
                # deep copy so it doesn't change the rectangleCheck
                temp = rectangleCheck.copy()
                temp.append(rectangle)
                newRects.append(temp)

        # append the rectangle into the rectangleArr
        rectangleArr.append([rectangle])

        for nr in newRects:
            rectangleArr.append(nr)