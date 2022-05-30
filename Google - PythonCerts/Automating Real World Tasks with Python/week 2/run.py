import os
import requests

def jsonparser():

    diction = {
        "title" : "",
        "name" : "",
        "date" : "",
        "feedback" : ""
    }

    for i in os.listdir():
        if i.endswith(".txt"):
            with open(i, "r") as f:
                diction["title"] = f.readline().rstrip()
                diction["name"] = f.readline().rstrip()
                diction["date"] = f.readline().rstrip()
                # this will read the characters from the current line from the 0th index to the last index of the last line in the file.
                diction["feedback"] = f.readline()[0:]

                url = "http://34.133.241.120/feedback/"
                x = requests.post(url, data=diction)

                if x.ok:
                    print("Uploaded")
                else:
                    print(f"error with status code: {x.status_code}")
   

if __name__ == '__main__':
    jsonparser()
    