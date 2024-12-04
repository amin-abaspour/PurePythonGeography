# Custom square root function using Newton's method
def sqrt(x, tolerance=1e-10):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number")
    guess = x / 2
    while abs(guess * guess - x) > tolerance:
        guess = (guess + x / guess) / 2
    return guess

# Factorial function for use in Taylor series
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Custom sine function
def sine(x, terms=10):
    x %= 2 * 3.141592653589793  # Reduce x to the range [0, 2π]
    result = 0
    for n in range(terms):
        coef = (-1) ** n
        result += coef * (x ** (2 * n + 1)) / factorial(2 * n + 1)
    return result

# Custom cosine function
def cosine(x, terms=10):
    x %= 2 * 3.141592653589793  # Reduce x to the range [0, 2π]
    result = 0
    for n in range(terms):
        coef = (-1) ** n
        result += coef * (x ** (2 * n)) / factorial(2 * n)
    return result

# Custom arctangent function
def arctan(x, terms=10):
    if x > 1:
        return 3.141592653589793 / 2 - arctan(1 / x, terms)
    elif x < -1:
        return -3.141592653589793 / 2 - arctan(1 / x, terms)
    result = 0
    for n in range(terms):
        coef = (-1) ** n
        result += coef * (x ** (2 * n + 1)) / (2 * n + 1)
    return result

# Custom haversine function
def haversine(lat1, lon1, lat2, lon2):
    def to_radians(deg):
        return deg * 3.141592653589793 / 180

    R = 6371  # Radius of the Earth in kilometers
    lat1, lon1, lat2, lon2 = map(to_radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sine(dlat / 2) ** 2 + cosine(lat1) * cosine(lat2) * sine(dlon / 2) ** 2
    c = 2 * arctan(sqrt(a) / sqrt(1 - a))

    return R * c

# Example usage
# point1 = (52.5200, 13.4050)  # Berlin
# point2 = (48.8566, 2.3522)   # Paris

# distance = haversine(point1[0], point1[1], point2[0], point2[1])
# print(f"Distance between Berlin and Paris: {distance:.2f} km")


# Calculate bounding box for a set of points
def calculate_bounding_box(points):
    min_lat = min(point[0] for point in points)
    max_lat = max(point[0] for point in points)
    min_lon = min(point[1] for point in points)
    max_lon = max(point[1] for point in points)
    return (min_lat, max_lat, min_lon, max_lon)

# Example usage
# locations = [
#     (52.5200, 13.4050),  # Berlin
#     (48.8566, 2.3522),   # Paris
#     (51.5074, -0.1278)   # London
# ]
# bbox = calculate_bounding_box(locations)
# print("Bounding Box:", bbox)

def create_ascii_map(points, grid_size=10):
    min_lat, max_lat, min_lon, max_lon = calculate_bounding_box(points)
    lat_step = (max_lat - min_lat) / grid_size
    lon_step = (max_lon - min_lon) / grid_size

    # Create empty grid
    grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]

    for lat, lon in points:
        row = int((lat - min_lat) / lat_step)
        col = int((lon - min_lon) / lon_step)
        row = max(0, min(grid_size - 1, row))  # Clamp within bounds
        col = max(0, min(grid_size - 1, col))  # Clamp within bounds
        grid[row][col] = "X"

    # Print grid
    for row in grid:
        print("".join(row))

# Example usage
# locations = [
#     (52.5200, 13.4050),  # Berlin
#     (48.8566, 2.3522),   # Paris
#     (51.5074, -0.1278)   # London
# ]
# create_ascii_map(locations)
