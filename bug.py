def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except TypeError:
        print("Type Error: Cannot divide string by number")
        return None
    except ZeroDivisionError:
        print("ZeroDivisionError: Cannot divide by zero")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
print(function_with_uncommon_error(10, 2))
print(function_with_uncommon_error(10, 0))
print(function_with_uncommon_error(10, "2"))
print(function_with_uncommon_error(10, [2,3]))