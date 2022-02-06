import os
import tempfile
import argparse
import json
import pickle

parser = argparse.ArgumentParser()

parser.add_argument('--key', dest="key")
parser.add_argument('--val', dest="val")

args = parser.parse_args()
key = str(args.key)
val = str(args.val)

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
with open(storage_path, 'wb+') as tf:
    if key != "None":
        if val != "None":
            if (os.stat(storage_path).st_size != 0) and (tf.read() != b""):
                data_new = pickle.load(tf)
                if key in data_new:
                    data_new[key].append(val)
                else:
                    data_new[key] = list()
                    data_new[key].append(val)
                    pickle.dump(data_new, tf)
            else:
                template = {str(key): [str(val)]}
                print(template)
                pickle.dump(template, tf)
        else:
            if (os.stat(storage_path).st_size != 0) and (tf.read() != b""):
                data_new = pickle.load(tf)
                print(data_new)
                if key in data_new:
                    for i in data_new[key]:
                        print(data_new)

        print(tf.read())
