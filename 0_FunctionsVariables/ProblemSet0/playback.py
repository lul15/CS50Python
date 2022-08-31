def main():
    lecture = input()
    print(playback(lecture))

def playback(lecture):
    return lecture.replace(" ", "...")

main()
