# Uncomment to generate error
# import pandas as pd  # Unused import to generate F401

sentence_wrong_place = "It should be caught by ruff as E402"

# Uncomment to generate error
# import numpy as np  # Another F401


# Add more lines to generate E303 too many blank lines
if __name__ == "__main__":
    # Put everything in one line to generate error
    really_long_variable_name_to_reach_the_end_of_the_line = (
        sentence_wrong_place.capitalize().strip().lower().join("another string")
    )

    # Put everything in one line to generate error
    print(
        really_long_variable_name_to_reach_the_end_of_the_line
    )  # The previous was a very long line, this one too but let's see what happens

    unused_var = 37

    print("Some random text")
    # Uncomment to generate error
    # print(f"Some other text with unnecessary f-string")
