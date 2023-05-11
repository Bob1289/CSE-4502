import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

if __name__ == "__main__":
    points = [(2,5,9)]

    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    distance = []

    count = 1

    for point in points:
        print(str(count) + " Distance from (%.1f, %.1f) to (%.1f, %.1f) is %.2f" % (point[0], point[1], x2, y2, euclidean_distance(point[0], point[1], x2, y2)))
        count += 1