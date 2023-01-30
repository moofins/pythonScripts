import argparse
import sys
import pathlib
import asyncio
import aiohttp
import pyfiglet
from colorama import Fore

banner = pyfiglet.figlet_format("Fuzzing . . .")
print(banner)

dirList = []                        

async def checkDir(session, fullUrl, progress, headers):
    async with session.get(fullUrl, allow_redirects=False) as r:
        
        if (r.status == 404):                       #if its a 404, ignore it and keep guessing. r.status rather than r.status_code
            sys.stdout.write("\033[K")  #clear line 
            print (Fore.WHITE + f"[progress: {progress}] | {fullUrl}", end='\r')  

        else:   #any non-404 response is printed to a new line.
            if (r.status == 200):
                sys.stdout.write("\033[K")
                print (Fore.GREEN + f"[{r.status}] | {fullUrl}", end='\n')
                dirList.append(f"[{r.status}] | {fullUrl}\n") #add to list
            elif (r.status == 301):
                sys.stdout.write("\033[K")
                print (Fore.BLUE + f"[{r.status}] | {fullUrl}", end='\n')   #would like to display redirect location after
                dirList.append(f"[{r.status}] | {fullUrl}\n") #add to list
            else:
                sys.stdout.write("\033[K")
                print (Fore.RED + f"[{r.status}] | {fullUrl}", end='\n')


async def fuzz(url,wordlist,extensions,headers):
    progress = 0
    async with aiohttp.ClientSession() as session:              #open session here, slightly diff syntax to requests
        tasks = []
        for line in wordlist.readlines():                       #for each word
            for extension in extensions:                        #for each extension specified, otherwise just blank
                fullUrl = url + line.strip() + extension
                progress += 1
                task = asyncio.ensure_future(checkDir(session,fullUrl,progress,headers))
                tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


def arguments():    #parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--url', required=True)
    parser.add_argument('-w','--wordlist', required=True)
    parser.add_argument('-x','--extension', nargs='*')  #can optionally supply extensions (.html, .php, etc)
    parser.add_argument('-e','--header')                #would like to add a header option, though currently does nothing
    args = parser.parse_args()

    return args

if __name__ == "__main__":
    argList = arguments()

    url = argList.url
    #if (url[0:4] != "http" or url[len(url)-1] != "/"):
    #    print("\"http://\" or \"https://\" required at start and \"/\" required at end!")   #specify input requirements
    #    exit(0)

    wordlistDest = argList.wordlist

    extensions = []
    if argList.extension:                   #if extensions were specified, otherwise the list is just a blank entry
        extensions = argList.extension
        extensions.append('')
    else:
        extensions.append('')

    headers = ""
    if argList.header:
        headers = argList.header

    with open(wordlistDest, 'r', encoding='latin-1') as wordlist:    #open wordlist and send it to the fuzz
        asyncio.get_event_loop().run_until_complete(fuzz(url,wordlist,extensions,headers))

    with open(pathlib.Path(__file__).parent / 'curDirList.txt','w',encoding='latin-1') as dirFile:
        dirFile.writelines(dirList)