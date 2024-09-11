y=input("File name: ").strip(" ")
if y.endswith(".gif") or y.endswith(".GIF"):
    print("image/gif")
elif y.endswith(".jpg") or y.endswith(".JPG"):
    print("image/jpeg")
elif y.endswith(".jpeg") or y.endswith(".JPEG"):
    print("image/jpeg")
elif y.endswith(".png") or y.endswith(".PNG"):
    print("image/png")
elif y.endswith(".pdf") or y.endswith(".PDF"):
    print("application/pdf")
elif y.endswith(".txt") or y.endswith(".TXT"):
    print("text/plain")
elif y.endswith(".zip") or y.endswith(".ZIP"):
    print("application/zip")
else :
    print("application/octet-stream")