import requests
import argparse

def fileget(url, filename):
	r = requests.get(url, allow_redirects=True)
	file = open(filename, 'wb')	#wb means open in binary, no modification happening to contents at all
	file.write(r.content)


def arguments():
    argList = [] #null list
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--url', required=True)
    parser.add_argument('-f','--file', required=True)
    args = parser.parse_args()

    return args

if __name__ == "__main__":
    argList = arguments()
    url = argList.url
    filename = argList.file
    fileget(url, filename)