class ConversionNotPossible(Exception):
    pass

def _normalize(u: str) -> str:
    return u.strip().lower()

# ----- Temperature (pivot: Kelvin) -----
def _to_kelvin(unit: str, value: float) -> float:
    if unit == "celsius":
        return value + 273.15
    if unit == "fahrenheit":
        return (value - 32.0) * 5.0 / 9.0 + 273.15
    if unit == "kelvin":
        return value
    raise ConversionNotPossible(f"Unknown temperature unit: {unit}")

def _from_kelvin(unit: str, k: float) -> float:
    if unit == "celsius":
        return k - 273.15
    if unit == "fahrenheit":
        return (k - 273.15) * 9.0 / 5.0 + 32.0
    if unit == "kelvin":
        return k
    raise ConversionNotPossible(f"Unknown temperature unit: {unit}")

# ----- Distance (pivot: meters) -----
_METERS_PER = {
    "meters": 1.0, "meter": 1.0,
    "miles": 1609.344, "mile": 1609.344,
    "yards": 0.9144, "yard": 0.9144,
}

def _to_meters(unit: str, value: float) -> float:
    if unit in _METERS_PER:
        return value * _METERS_PER[unit]
    raise ConversionNotPossible(f"Unknown distance unit: {unit}")

def _from_meters(unit: str, meters: float) -> float:
    if unit in _METERS_PER:
        return meters / _METERS_PER[unit]
    raise ConversionNotPossible(f"Unknown distance unit: {unit}")

def convert(fromUnit: str, toUnit: str, value: float) -> float:
    """Convert value between units (C/F/K and Miles/Yards/Meters)."""
    f, t = _normalize(fromUnit), _normalize(toUnit)
    v = float(value)

    if f == t:
        return v

    temps = {"celsius", "fahrenheit", "kelvin"}
    dists = set(_METERS_PER.keys())

    if f in temps and t in temps:
        k = _to_kelvin(f, v)
        return _from_kelvin(t, k)

    if f in dists and t in dists:
        m = _to_meters(f, v)
        return _from_meters(t, m)

    raise ConversionNotPossible(f"Incompatible units: {fromUnit} -> {toUnit}")
