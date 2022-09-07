
locations = ["sofa", "garage", "chair", "table", "closet"]

key_location = "chair"

for location in locations:
    if location == key_location:
        print("Key is found at ", location)
        break
    else:
        print("Key is not found at ", location)