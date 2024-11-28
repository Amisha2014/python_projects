emoji_dict = {
    "❤️" : "Red heart",
    "🦄"  : "Metalic unicorn",
    "🦩" : "Pink flamingo"
}

def emoji_to_text_converter (emoji):
    return emoji_dict.get (emoji, "unknown")

print ("Welcome to emoji to text converter")
input_emoji = input("enter an emoji")


emoji_text = emoji_to_text_converter(input_emoji)
print (f"Text for the emoji is {emoji_text}")