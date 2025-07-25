"https://www.codewars.com/kata/555086d53eac039a2a000083/train/python"

"Opposites Attract"

def lovefunc(flower1, flower2):
    is_flower1_even = flower1 % 2 == 0
    is_flower2_even = flower2 % 2 == 0

    if is_flower1_even and not is_flower2_even:
        return True
    elif not is_flower1_even and is_flower2_even:
        return True
    else:
        return False