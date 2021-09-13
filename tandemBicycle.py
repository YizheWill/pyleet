def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    redShirtSpeeds = redShirtSpeeds[::-
                                    1] if fastest is True else redShirtSpeeds
    res = 0
    for idx, blue in enumerate(blueShirtSpeeds):
        res += max(blue, redShirtSpeeds[idx])
    return res
