"https://www.codewars.com/kata/56606694ec01347ce800001b/train/python"

"Find the next perfect square!"

def find_next_square(sq):
    root = sq ** 0.5
    
    if root == int(root):
        next_root = int(root) + 1
        
        return next_root * next_root
    else:
        return -1