"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
class Solution:
    def __init__(self):
        self.buf_ptr = 0
        self.buf_count = 0
        self.buffer = ["" for i in range(4)]
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        ptr = 0
        while ptr < n:
            while ptr < n and self.buf_ptr < self.buf_count:
                buf[ptr] = self.buffer[self.buf_ptr]
                ptr += 1
                self.buf_ptr += 1
                if self.buf_ptr == self.buf_count:
                    self.buf_ptr = self.buf_count = 0
            if self.buf_ptr == 0:
                self.buf_count = read4(self.buffer)
                if self.buf_count == 0:
                    break
        return ptr
            
            
            
            
            
            
            
            
            
        
