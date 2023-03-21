import sys, os, subprocess


def main():
    # command line args
    audio_file = os.path.abspath(sys.argv[2])
    subtitle = os.path.abspath(sys.argv[1])
    out_path = os.path.abspath(sys.argv[3])

    # FFmpeg command
    ffmpeg = "ffmpeg -i '{in}' -ss {from} -to {to} -c copy -y " + os.path.join(out_path, "wavs", "{out}.opus")

    # list of data
    ffmpeg_data: list[FFmpegFileData] = []

    # read the subtitle file
    with open(subtitle) as file:
        # prase the text in the subtitle file to get usable data
        items = []
        next_line = 3
        for num, line in enumerate(file, start=1):
            line = line.strip()
            if line:
                items.append(line)
            if num == next_line:
                ffmpeg_data.append(FFmpegFileData(items[0], items[2], items[1]))
                next_line += 4
                items = []

    with open(os.path.join(out_path, "metadata.txt"), "a") as meta:
        for i in ffmpeg_data:
            # with all of data now parse and ready to use
            # use it in the ffmpeg command and write out it's content with getMetaString
            map = {'in': audio_file} | i.getFFmpegArgs()
            arg = ffmpeg.format_map(map)
            subprocess.call(splitStr(arg), stderr=subprocess.DEVNULL)
            print(f"Processing file: {i}")
            meta.write(i.getMetaString() + "\n")

def splitStr(string):
    out = []
    temp = ""
    in_quote = False
    for i in string.split(" "):
        if not in_quote:
            if "'" in i and "'" != i[-1]:
                in_quote = True
                temp += i + " "
            else:
                out.append(i.replace("'", ""))
        else:
            temp += i + " "
            if "'" in i:
                in_quote = False
                out.append(temp[:-1].replace("'", ""))
                temp = ""

    return out
        
class FFmpegFileData():
    def __init__(self, name: str, transcribe: str, time: str) -> None:
        self.name = name
        self.transcribe = transcribe
        self.time = [i.replace(',', '.') for i in time.split(' --> ')]

    def getMetaString(self) -> str:
        return f"{self.name}|{self.transcribe}"

    def getFFmpegArgs(self) -> dict:
        return {'from': self.time[0],
                'to': self.time[1],
                'out': self.name}

    def __str__(self) -> str:
        return f"{self.name} | {self.time[0]} -> {self.time[1]} | {self.transcribe[:50]}..."

    def __repr__(self) -> str:
        return self.__str__()

if __name__ == "__main__":
    main()