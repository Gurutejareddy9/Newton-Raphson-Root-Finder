def f(x):
    return x**2 - 2*x - 5

def f_prime(x):
    return 2*x - 2

def newton_raphson(initial_guess, tolerance=1e-10, max_iterations=100):
    x = initial_guess
    iteration = 0
    while True:
        fx = f(x)
        f_prime_x = f_prime(x)
        x_new = x - (fx / f_prime_x)  # Corrected line
        iteration += 1
        print(f"Iteration {iteration}: x = {x_new}")
        if abs(fx) < tolerance or iteration >= max_iterations:
            break
        x = x_new
    return x_new

# Take initial guess from the user
initial_guess = float(input("Enter initial guess: "))

root = newton_raphson(initial_guess)
print("Approximately", root)
