import time
from threading import Thread, Lock
import sys

lock = Lock()


def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()


def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)


def sing_song():
    lyrics = [
        ("This is me praying that", 0.1),
        ("This was the very first page", 0.1),
        ("Not where the story line ends", 0.1),
        ("My thoughts will echo your name,", 0.1),
        ("until I see you again", 0.1),
        ("These are the words I held back, a I was leaving too soon", 0.12),
        ("I was enchanted to meet you.....", 0.11),
        ("\n""Please don't be in love with someone else", 0.12),
        ("Please don't have somebody waiting on you", 0.16),        
        ("Please don't be in love with someone else", 0.12),
        ("Please don't have somebody waiting on you", 0.16),
    ]
    delays = [0.3, 1.7, 3.5, 5.2, 6.4, 7.9, 10.0, 12.6, 15.2, 16.8, 19.4]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    sing_song()
