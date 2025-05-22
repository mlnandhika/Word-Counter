import time
from collections import Counter
from multiprocessing import Pool, cpu_count

def count_words(filename):
    word_counts = Counter()
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.strip()
            words = line.split()
            for word in words:
                word = word.strip('.,!?":;')
                word = word.lower()
                if word:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

    return word_counts.most_common(20)

if __name__ == "__main__":
    filename = 'data.txt'

    start_time = time.time()
    num_cpu_available = cpu_count()

    with Pool (num_cpu_available - 1) as mp_pool:
        result = mp_pool.map(count_words, [filename] )
    
    print("Top 20 words:")
    print(result)
    end_time = time.time()

    print(f"Execution time with pool Multiprocessing: {end_time - start_time} seconds")
