import string

probabilities = {char: 1/27 for char in string.ascii_lowercase + ' '}  

cumulative_probs = {}
cumulative_sum = 0.0

for symbol, prob in probabilities.items():
    cumulative_probs[symbol] = cumulative_sum
    cumulative_sum += prob

def compress(sequence):
    for symbol in sequence:
        if symbol not in cumulative_probs:
            raise ValueError(f"Symbol '{symbol}' is not in the probabilities table.")
    
    low = 0.0
    high = 1.0

    for symbol in sequence:
        range_width = high - low
        high = low + range_width * (cumulative_probs[symbol] + probabilities[symbol])
        low = low + range_width * cumulative_probs[symbol]

    encoded_value = (low + high) / 2
    return encoded_value
