
def compress(input_string):
   if not input_string: 
      return
   encoded_string = ""
   count = 1 
   prev_char = input_string[0] 

   for char in input_string[1:]:
      if char == prev_char:
         count+=1
      else:
         encoded_string += prev_char + str(count)
         prev_char = char
         count = 1
   return encoded_string
