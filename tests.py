from math import isclose
from conversions import (
    convertCelsiusToKelvin, convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius, convertFahrenheitToKelvin,
    convertKelvinToCelsius, convertKelvinToFahrenheit
)
from conversions_refactored import convert, ConversionNotPossible

TOL = 1e-3

def check(actual, expected, label):
    ok = isclose(actual, expected, rel_tol=0, abs_tol=TOL)
    print(f"{'PASS' if ok else 'FAIL'} | {label} -> got {actual:.4f}, expected {expected:.4f}")
    return ok

def test_c_to_k():
    print("\n[convertCelsiusToKelvin]")
    cases = [(0.0, 273.15), (100.0, 373.15), (300.0, 573.15), (-40.0, 233.15), (37.0, 310.15)]
    return all(check(convertCelsiusToKelvin(c), k, f"C={c}") for c, k in cases)

def test_c_to_f():
    print("\n[convertCelsiusToFahrenheit]")
    cases = [(0.0, 32.0), (100.0, 212.0), (300.0, 572.0), (-40.0, -40.0), (37.0, 98.6)]
    return all(check(convertCelsiusToFahrenheit(c), f, f"C={c}") for c, f in cases)

def test_f_to_c():
    print("\n[convertFahrenheitToCelsius]")
    cases = [(32.0, 0.0), (212.0, 100.0), (572.0, 300.0), (-40.0, -40.0), (98.6, 37.0)]
    return all(check(convertFahrenheitToCelsius(f), c, f"F={f}") for f, c in cases)

def test_f_to_k():
    print("\n[convertFahrenheitToKelvin]")
    cases = [(32.0, 273.15), (212.0, 373.15), (572.0, 573.15), (-40.0, 233.15), (0.0, 255.372)]
    return all(check(convertFahrenheitToKelvin(f), k, f"F={f}") for f, k in cases)

def test_k_to_c():
    print("\n[convertKelvinToCelsius]")
    cases = [(273.15, 0.0), (373.15, 100.0), (573.15, 300.0), (233.15, -40.0), (310.15, 37.0)]
    return all(check(convertKelvinToCelsius(k), c, f"K={k}") for k, c in cases)

def test_k_to_f():
    print("\n[convertKelvinToFahrenheit]")
    cases = [(273.15, 32.0), (373.15, 212.0), (573.15, 572.0), (233.15, -40.0), (255.372, 0.0)]
    return all(check(convertKelvinToFahrenheit(k), f, f"K={k}") for k, f in cases)

def test_refactored_temperature():
    print("\n[refactor] temperature conversions via convert()")
    cases = [
        ("celsius", "kelvin", 300.0, 573.15),
        ("celsius", "fahrenheit", 300.0, 572.0),
        ("fahrenheit", "celsius", 98.6, 37.0),
        ("fahrenheit", "kelvin", 0.0, 255.372),
        ("kelvin", "celsius", 310.15, 37.0),
        ("kelvin", "fahrenheit", 233.15, -40.0),
        ("Celsius", "Celsius", 12.34, 12.34),
    ]
    return all(check(convert(f, t, v), exp, f"{f}->{t} {v}") for f, t, v, exp in cases)

def test_refactored_distance():
    print("\n[refactor] distance conversions via convert()")
    cases = [
        ("miles", "meters", 1.0, 1609.344),
        ("yards", "meters", 1.0, 0.9144),
        ("meters", "yards", 1.0, 1.0936133),
        ("meters", "miles", 1609.344, 1.0),
        ("Yards", "Yards", 123.456, 123.456),
    ]
    return all(check(convert(f, t, v), exp, f"{f}->{t} {v}") for f, t, v, exp in cases)

def test_refactored_incompatible():
    print("\n[refactor] incompatible units raise ConversionNotPossible")
    try:
        _ = convert("celsius", "meters", 1.0)
    except ConversionNotPossible:
        print("PASS | celsius -> meters raised ConversionNotPossible")
        return True
    print("FAIL | celsius -> meters should have raised ConversionNotPossible")
    return False

def main():
    print("Running tests...")
    results = [
        test_c_to_k(), test_c_to_f(), test_f_to_c(), test_f_to_k(),
        test_k_to_c(), test_k_to_f(),
        test_refactored_temperature(), test_refactored_distance(), test_refactored_incompatible(),
    ]
    passed = sum(bool(x) for x in results)
    total = len(results)
    print(f"\nSummary: {passed}/{total} groups passed.")
    if passed == total:
        print(" All tests passed!")
    else:
        print(" Some tests failed.")

if __name__ == "__main__":
    main()
