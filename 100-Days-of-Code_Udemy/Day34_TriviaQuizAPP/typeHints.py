# Define variable data type
age: int
name: str
height: float
is_human: bool

# -> Define function output type
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(12):
    print("You may pass")
else:
    print("Pay a fine.")







