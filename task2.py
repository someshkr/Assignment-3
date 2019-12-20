subjects = ["Americans","Indians"]
verbs = ["play", "watch"]
objects = ["Baseball","Cricket"]

sentences = [(sub+' '+vbs+' '+obj) for sub in subjects for vbs in verbs for obj in objects]
for sen in sentences:
    print(sen)
