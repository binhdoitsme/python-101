import sys

# getting input from user
num_cakes = 10
is_valid_value_entered = False
while not is_valid_value_entered:
    try: # try-block: if expected error is raised then move to `except`
        num_ppl = int(input("how many people to share: "))
        m = num_cakes / num_ppl
        is_valid_value_entered = True
    except Exception: # handle only `non-exit exceptions`
        print("invalid num of people, please retry")
        ...
        ...
        ...
        ...
        ...
        ...
    except KeyboardInterrupt: # handle a specific type of exception
        print("gracefully exited")
        sys.exit()

print(f"each person will receive {m} cakes")

