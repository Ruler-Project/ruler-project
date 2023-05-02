import argparse, os, bisect 

# python3 build-nav.py -d ../docs/RULER

# https://www.geeksforgeeks.org/python-program-to-insert-an-element-into-sorted-list/
def insert(list, n):
    bisect.insort(list, n) 
    return list

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directory", help="directory to process", required=True)
args = parser.parse_args()

inputdir = args.directory

listing = {}

toplevel = {
    "edr": "Endpoint Detection and Response",""
    "av": "Anti-Virus",
    "mail": "Mail",
    "web": "Web",
    "sync": "Sychronisation",
    "remote": "Remote Administration/Access applications"
}

space = "    "

for filename in os.listdir(inputdir):
    fullfilepath = os.path.join(inputdir, filename)
    nextlevellist = []
    if not os.path.isfile(fullfilepath):
        # print (filename)
        lookupfoldername = toplevel[filename] 
        print (f"- '{lookupfoldername}':")
        for nextlevel in os.listdir(fullfilepath):
            nextlevellist = insert(nextlevellist, nextlevel)
            # nextlevellist.append(nextlevel)

        for nextlevel in nextlevellist:
            first = nextlevel.replace('.md', '')
            if ' ' in first:
                first = "'" + first + "'"

            second = f"'RULER/{filename}/{nextlevel}'"
            print (f"{space} - {first}: {second}")
        