def chillcalc(v, t):
    return round((13.12 + 0.6215*t - 11.37*(v**0.16) + 0.3965*t*(v**0.16)), 4) if v > 4.8 and t < 10 else "I can't compute for the wind chill with the values you specified."

if __name__ == "__main__":
    t_in = float(input("Input temp in Celsius: "))
    v_in = float(input("Enter wind speed in km/h: "))
    print(chillcalc(v_in, t_in))