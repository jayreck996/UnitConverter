import argparse

def convert_units(value, from_unit, to_unit):
    conversions = {
        'km': {'miles': lambda x: x * 0.621371, 'meters': lambda x: x * 1000},
        'miles': {'km': lambda x: x * 1.60934, 'meters': lambda x: x * 1609.34},
        'meters': {'km': lambda x: x / 1000, 'miles': lambda x: x / 1609.34},
        'celsius': {'fahrenheit': lambda x: x * 9/5 + 32, 'kelvin': lambda x: x + 273.15},
        'fahrenheit': {'celsius': lambda x: (x - 32) * 5/9, 'kelvin': lambda x: (x - 32) * 5/9 + 273.15},
        'kelvin': {'celsius': lambda x: x - 273.15, 'fahrenheit': lambda x: (x - 273.15) * 9/5 + 32}
    }

    if from_unit not in conversions or to_unit not in conversions[from_unit]:
        raise ValueError("Unsupported unit conversion")

    return conversions[from_unit][to_unit](value)

def main():
    parser = argparse.ArgumentParser(description='Unit Converter CLI Tool')
    parser.add_argument('-v', '--value', type=float, required=True, help='Value to convert')
    parser.add_argument('-f', '--from', dest='from_unit', required=True, help='Unit to convert from')
    parser.add_argument('-t', '--to', dest='to_unit', required=True, help='Unit to convert to')

    args = parser.parse_args()

    try:
        result = convert_units(args.value, args.from_unit, args.to_unit)
        print(f"{args.value} {args.from_unit} is equal to {result} {args.to_unit}")
    except ValueError as e:
        print(str(e))

if __name__ == '__main__':
    main()