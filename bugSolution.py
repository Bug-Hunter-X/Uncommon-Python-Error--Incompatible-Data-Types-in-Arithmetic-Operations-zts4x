def function_with_uncommon_error(a, b):
    try:
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            result = a / b
            return result
        else:
            print("Type Error: Cannot perform this operation")
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