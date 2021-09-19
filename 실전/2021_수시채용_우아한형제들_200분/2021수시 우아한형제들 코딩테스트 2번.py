# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    extesnsions_music = ["mp3", "aac", "flac"]
    extesnsions_image = ["jpg", "bmp", "gif"]
    extesnsions_movie = ["mp4", "avi", "mkv"]

    bytes_music = 0
    bytes_images = 0
    bytes_movies = 0
    bytes_other = 0

    items = S.split("\n")

    for item in items:
        splited_item = item.split(" ")
        full_name = splited_item[0]
        splited_full_name = full_name.split(".")
        
        bytes = splited_item[1]
        extension = splited_full_name[len(splited_full_name)-1]

        if extension in extesnsions_music:
            bytes_music += int(bytes.replace("b", ""))
        elif extension in extesnsions_image:
            bytes_images += int(bytes.replace("b", ""))
        elif extension in extesnsions_movie:
            bytes_movies += int(bytes.replace("b", ""))
        else:
            bytes_other += int(bytes.replace("b", ""))


    return "music " + str(bytes_music) + "b\n" + "images " + str(bytes_images) + "b\n" + "movies " + str(bytes_movies) + "b\n" + "other " + str(bytes_other) + "b\n" 

 

S = """my.song.mp3 11b
greatSong.flac 1000b
not3.txt 5b
video.mp4 200b
game.exe 100b
mov!e.mkv 10000b"""
print("Result: \n"+str(solution(S)))

print("""Expect:
music 1011b
images 0b
movies 10200b
other 105b""")