# Read and print specific lines from a text file (e.g., lines 2 to 4).

def specific_lines(f,start,end):
    with open(f, 'r') as file:
        lines = file.readlines()
        print(lines)
        for line in lines[start-1:end]:
            print(line.strip())
            
        
specific_lines("txt2.txt",1,5)