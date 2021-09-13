def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort()
    blueShirtHeights.sort()
    redFront = True
    blueFront = True
    for idx, red in enumerate(redShirtHeights):
        if red < blueShirtHeights[idx]:
            blueFront = False
        elif blueShirtHeights[idx] < red:
            redFront = False
        else:
            return False
    return blueFront or redFront
