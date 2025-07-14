from csv import reader

# Define function to retrieve prices colum in to a list
def get_prices(data):
    """
    Retrieves prices column in to a list

    Args:
        data (str): CSV format data

    Returns:
        list: list of prices
    """
    f = open(data)
    f = reader(f)
    for i in f:
        print(i[2])
print(get_prices("data.csv"))


def get_products(data):
    """
    Retrieves products column in to a list

    Args:
        data (str): CSV format data

    Returns:
        list: list of products
    """
    f = open(data)
    f = reader(f)
    for i in f:
        print(i[0])
print(get_products("data.csv"))
def get_expensive(prices):
    """
    Finds the most expensive product of index

    Args:
        prices (list): list of prices

    Returns:
        int: index of most expensive product
    """
    f = open(prices)
    f = reader(f)
    s = 0.0
    for i in f:
        a = i[2][1::]
        if a.isdigit():
            if a>s:
                s = a
    return a
print(get_expensive("data.csv"))

# Read data from file
f = open("data.csv")
data = f.read()
