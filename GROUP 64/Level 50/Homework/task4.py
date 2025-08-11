c_to_f = lambda c: (c * 9/5) + 32

celsius_temps = [0, 20, 37, 100]

for c in celsius_temps:
    print(f"{c}°C = {c_to_f(c)}°F")
