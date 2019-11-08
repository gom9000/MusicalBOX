    import json

    def loadPrograms(file):
        fp = open(file, 'r')
        jsondata = json.load(fp)
        fp.close()
        return jsondata

    def savePrograms(jsondata, file):
        fp = open(file, 'w')
        json.dump(jsondata, fp, indent=4)
        fp.close()