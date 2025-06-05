photoWithData = 16 * 1024 * 1024 * 8 / 64
photoCompressed = photoWithData - 32 * 1024 * 8
photo = photoCompressed * 100 // 75
print(photoCompressed)
print(photo / (512*280))
print(2**17)