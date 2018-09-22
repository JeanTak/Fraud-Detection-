def read_csv_file(filename):
    ret = []
    with open(filename) as fh:
        for l in fh.readlines():
            claim = l.split()
            claim = claim[0].split(',')
            for i in range(len(claim)):
                claim[i] = float(claim[i])
            ret.append(claim)
    return ret