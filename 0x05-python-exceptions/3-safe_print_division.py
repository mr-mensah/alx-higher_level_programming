#!/usr/bin/python3

def safe_print_division(a, b):
    
    try:
        end = a / b
    except (TypeError, ZeroDivisionError):
        end = None
    finally:
        print("Inside end: {}".format(end))
    return end
