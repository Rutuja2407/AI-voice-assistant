import requests

url = "https://official-joke-api.appspot.com/random_joke"
json_data = requests.get(url).json()

arr=["",""]
arr[0]=json_data["setup"]
arr[1]=json_data["punchline"]
def joke():
    return arr
    # print(arr)

# # Example usage: Print the joke
# joke_arr = joke()
# print(joke_arr[0])  # Print setup
# print(joke_arr[1])  # Print punchline