import heapq
from collections import defaultdict, Counter

def compress(text):
   frequency = Counter(text)

   heap = [[weight,[char,""]] for char , weight in frequency.items()]
   heapq.heapify(heap)

   while len(heap) > 1 :
      lo = heapq.heappop(heap)
      hi = heapq.heappop(heap)
      for pair in lo[1:]:
         pair[1] = '0' + pair[1]
      for pair in hi[1:]:
         pair[1] = '1' + pair[1]
      heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

   huffman_codes = sorted(heap[0][1:], key=lambda p: (len(p[-1]), p))
   huffman_dict = {char: code for char, code in huffman_codes}

   encoded_text = "".join(huffman_dict[char] for char in text)

   return encoded_text, huffman_dict
