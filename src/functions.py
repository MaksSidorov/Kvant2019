import dlib

# Функция для первого упражнения
def func1(landmarks, x2, x1, y2, y1):
    d = (((((landmarks.part(37).y - landmarks.part(19).y) ** 2 + (
            landmarks.part(37).x - landmarks.part(19).x) ** 2)) ** 0.5) + (((
            (landmarks.part(38).y - landmarks.part(20).y) ** 2 + (
            landmarks.part(38).x - landmarks.part(20).x) ** 2)) ** 0.5)) / (
                (((x2 - x1) ** 2 + (y2 - y1) ** 2)) ** 0.5)
    if d >= 0.19:
        return True
    elif d < 0.16:
        return False



# Функция для второго упражнения
def func2(landmarks, x2, x1, y2, y1):
    d = (((((landmarks.part(41).y - landmarks.part(37).y) ** 2 + (
            landmarks.part(41).x - landmarks.part(37).x) ** 2)) ** 0.5) + (((
            (landmarks.part(39).y - landmarks.part(40).y) ** 2 + (
            landmarks.part(39).x - landmarks.part(40).x) ** 2)) ** 0.5)) / (2 * ((((
            (landmarks.part(36).y - landmarks.part(39).y) ** 2 + (
            landmarks.part(36).x - landmarks.part(39).x) ** 2)) ** 0.5)))
    if d >= 0.3:
        return False
    elif d < 0.26:
        return True

# Функция для третьего упражнения(правая сторона)
def func3_1(landmarks, x2, x1, y2, y1):
    d = (((((landmarks.part(41).y - landmarks.part(37).y) ** 2 + (
            landmarks.part(41).x - landmarks.part(37).x) ** 2)) ** 0.5) + (((
            (landmarks.part(38).y - landmarks.part(40).y) ** 2 + (
            landmarks.part(38).x - landmarks.part(40).x) ** 2)) ** 0.5)) / (2 * ((((
            (landmarks.part(36).y - landmarks.part(39).y) ** 2 + (
            landmarks.part(36).x - landmarks.part(39).x) ** 2)) ** 0.5)))
    if d >= 0.3:
        return False
    elif d < 0.26:
        return True

# Функция для третьего упражнения(левая сторона)
def func3_2(landmarks, x2, x1, y2, y1):
    d = (((((landmarks.part(47).y - landmarks.part(43).y) ** 2 + (
            landmarks.part(47).x - landmarks.part(43).x) ** 2)) ** 0.5) + (((
            (landmarks.part(46).y - landmarks.part(44).y) ** 2 + (
            landmarks.part(46).x - landmarks.part(44).x) ** 2)) ** 0.5)) / (2 * ((((
            (landmarks.part(42).y - landmarks.part(45).y) ** 2 + (
            landmarks.part(42).x - landmarks.part(45).x) ** 2)) ** 0.5)))
    if d  >= 0.26:
        return False
    elif d < 0.18:
        return True

# Функция для четвертого упражнения(левая сторона)
def func4_1(landmarks, x2, x1, y2, y1):
    d = ((((landmarks.part(54).y - landmarks.part(66).y) ** 2) ** 0.5)) / (
                (((x2 - x1) ** 2 + (y2 - y1) ** 2)) ** 0.5)
    f = (((((landmarks.part(50).y - landmarks.part(58).y) ** 2 + (
            landmarks.part(50).x - landmarks.part(58).x) ** 2)) ** 0.5) + ((((landmarks.part(51).y - landmarks.part(57).y) ** 2 + (
            landmarks.part(51).x - landmarks.part(57).x) ** 2)) ** 0.5) + ((((landmarks.part(52).y - landmarks.part(56).y) ** 2 + (
            landmarks.part(52).x - landmarks.part(56).x) ** 2)) ** 0.5)) / (((((landmarks.part(48).y - landmarks.part(54).y) ** 2 + (
            landmarks.part(48).x - landmarks.part(54).x) ** 2)) ** 0.5) * 3)
    if (d * 1000) >= 25 and (f * 1000) < 500:
        return True
    elif (d * 1000) < 10:
        return False
    # return d * 1000

# Функция для четвертого упражнения(правая сторона)
def func4_2(landmarks, x2, x1, y2, y1):
    d = ((((landmarks.part(48).y - landmarks.part(66).y) ** 2) ** 0.5)) / (
                (((x2 - x1) ** 2 + (y2 - y1) ** 2)) ** 0.5)
    f = (((((landmarks.part(50).y - landmarks.part(58).y) ** 2 + (
            landmarks.part(50).x - landmarks.part(58).x) ** 2)) ** 0.5) + ((((landmarks.part(51).y - landmarks.part(57).y) ** 2 + (
            landmarks.part(51).x - landmarks.part(57).x) ** 2)) ** 0.5) + ((((landmarks.part(52).y - landmarks.part(56).y) ** 2 + (
            landmarks.part(52).x - landmarks.part(56).x) ** 2)) ** 0.5)) / (((((landmarks.part(48).y - landmarks.part(54).y) ** 2 + (
            landmarks.part(48).x - landmarks.part(54).x) ** 2)) ** 0.5) * 3)
    if (d * 1000) >= 40 and (f * 1000) < 500:
        return True
    elif (d * 1000) < 10:
        return False
    # return d * 1000

    
# Функция для пятого упражнения(левая сторона)
def func5_1(landmarks, x2, x1, y2, y1):
    f = (((((landmarks.part(50).y - landmarks.part(58).y) ** 2 + (
            landmarks.part(50).x - landmarks.part(58).x) ** 2)) ** 0.5) + (
                     (((landmarks.part(51).y - landmarks.part(57).y) ** 2 + (
                             landmarks.part(51).x - landmarks.part(57).x) ** 2)) ** 0.5) + (
                     (((landmarks.part(52).y - landmarks.part(56).y) ** 2 + (
                             landmarks.part(52).x - landmarks.part(56).x) ** 2)) ** 0.5)) / (
                    ((((landmarks.part(48).y - landmarks.part(54).y) ** 2 + (
                            landmarks.part(48).x - landmarks.part(54).x) ** 2)) ** 0.5) * 3)
    d = (((((landmarks.part(54).y - landmarks.part(14).y) ** 2)  + ((
            landmarks.part(54).x - landmarks.part(14).x) ** 2))** 0.5) ) / (
            (((x2 - x1) ** 2 + (y2 - y1) ** 2)) ** 0.5)
    if (d * 1000) <= 210 and (f * 1000) > 500:
        return True
    elif (d * 1000) > 220:
        return False

# Функция для пятого упражнения(правая сторона)
def func5_2(landmarks, x2, x1, y2, y1):
    f = (((((landmarks.part(50).y - landmarks.part(58).y) ** 2 + (
            landmarks.part(50).x - landmarks.part(58).x) ** 2)) ** 0.5) + (
                     (((landmarks.part(51).y - landmarks.part(57).y) ** 2 + (
                             landmarks.part(51).x - landmarks.part(57).x) ** 2)) ** 0.5) + (
                     (((landmarks.part(52).y - landmarks.part(56).y) ** 2 + (
                             landmarks.part(52).x - landmarks.part(56).x) ** 2)) ** 0.5)) / (
                    ((((landmarks.part(48).y - landmarks.part(54).y) ** 2 + (
                            landmarks.part(48).x - landmarks.part(54).x) ** 2)) ** 0.5) * 3)
    d = (((((landmarks.part(48).y - landmarks.part(2).y) ** 2)  + ((
            landmarks.part(48).x - landmarks.part(2).x) ** 2))** 0.5) ) / (
            (((x2 - x1) ** 2 + (y2 - y1) ** 2)) ** 0.5)
    if (d * 1000) <= 210 and (f * 1000) > 500:
        return True
    elif (d * 1000) > 220:
        return False
