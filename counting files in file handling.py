file=open("notes.txt","r")
content=file.read()
lines=len(content.splitlines())
words=len(content.split())
characters=len(content)
print("Lines:",lines,"Words:",words)
file.close