__author__ = 'Tony Beltramelli www.tonybeltramelli.com - 06/09/2015'

import numpy as np


class Label:
    def __init__(self, path):
        file_path = "{}labels.csv".format(path)
        data = np.genfromtxt(file_path, delimiter=',', skip_header=1,
                             names=['timestamp', 'label'], dtype=[("timestamp", long), ('label', int)])

        self.timestamp = data['timestamp']
        label = data['label']

        self.label = []

        for i in range(0, len(label)):
            self.label.append(chr(int(label[i])))