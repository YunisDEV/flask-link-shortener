import shortuuid
def generateLink():
    randomGen = shortuuid.ShortUUID().random(length=7)
    return randomGen