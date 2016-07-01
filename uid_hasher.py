import hashlib, uuid
import csv

finished_list = []

with open("ids_to_be_hashed.csv", 'rb') as source_file:
    contents = csv.reader(source_file, delimiter=',', quotechar='|')

    for lines in contents:
        line = []
        uid = lines[0]
        salt = uuid.uuid4().hex
        hashed_password = hashlib.sha512(uid + salt).hexdigest()
        line.append(uid)
        line.append(hashed_password)

        finished_list.append(line)

with open('finished_hash.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"')

    writer.writerows(finished_list)