import wave


def extract_data(frames):
    by = 0
    ret = []
    for i, frame in enumerate(frames):
        lsb = frame & 0b00000001
        by += (2**(7 - (i % 8))) * lsb

        if i % 8 == 7:
            ret.append(by.to_bytes(1, "little"))
            by = 0

    return b"".join(ret)



if __name__ == '__main__':
    filename = "yes.wav"
    wf = wave.open(filename, "rb")
    print(wf.getparams())

    frames = wf.readframes(wf.getnframes())
    flag = extract_data(list(frames)[:1000])
    wf.close()

    print(flag)
