def main() -> None:
    # Python has lists, many other languages have arrays. They're similar.
    l = [15, 12, 7]

    # It also has sets. A set is a collection of unique objects. It is
    # non-sequential. Sets are VERY FAST at value-based lookups.
    s = set(l)

    if 1000 in l:
        print('1000 is in the list!')

    if 1000 in s:
        print('1000 is in the set!')

if __name__ == '__main__':
    main()
