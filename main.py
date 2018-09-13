import pyaudio
import wave
import sys

chunk = 1024
sample_dir = 'num_samples/'
p = pyaudio.PyAudio()

def play_wav(filename: str):
    #open a wav format music  
    f = wave.open(sample_dir + filename,"rb")
    #open stream  
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                    channels = f.getnchannels(),  
                    rate = f.getframerate(),  
                    output = True)  
    #read data  
    data = f.readframes(chunk)  

    #play stream  
    while data:  
        stream.write(data)  
        data = f.readframes(chunk)  

    #stop stream  
    stream.stop_stream()  
    stream.close()  


def select_ending(end_num: int, pow: int):
    if pow == 0 or pow > 2:
        return ''
    body = '1000' if pow == 1 else 'mil'
    ending = ''
    if end_num == 1:
        ending = '_a'
    elif end_num in range(2, 5):
        ending = '_i'
    else:
        ending = '_s'
    return body + ending
 

def play_triple(num: int, pow: int):
    hun = int(num / 100)
    ten = int(num / 10) % 10
    ed = num % 10

    if hun > 0 and hun < 10:
        play_wav(str(hun*100) + '.wav')
    if ten > 0 and ten < 10:
        if ten == 1:
            ed += 10
        else:
            play_wav(str(ten*10) + '.wav')
    if ed > 0 and ed < 20:
        if pow == 1 and (ed == 1 or ed == 2):
            play_wav(str(ed) + '_a.wav')
        else:
            play_wav(str(ed) + '.wav')
    ending = select_ending(ed, pow)
    if ending != '' and num != 0:
        play_wav(ending + '.wav')


if __name__ == '__main__':
    while(True):
        try:
            in_number = int(input('Введите число: '))
        except:
            print("Не является числом.")
            continue
        if in_number >= 1000000000:
            print("Введенное число слишком велико.")
            continue
        stack = []
        while in_number > 0:
            stack.append(in_number % 1000)
            in_number = int(in_number / 1000)
        cur_pow = len(stack)
        while stack:
            cur_pow -= 1
            play_triple(stack.pop(), cur_pow)

        
    
p.terminate()