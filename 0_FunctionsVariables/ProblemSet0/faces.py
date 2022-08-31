def main():
    stmt = input()
    print(convert(stmt))

def convert(stmt):
    smiling = stmt.replace(":)", "🙂")
    frowning = smiling.replace(":(", "🙁")
    return frowning

main()
