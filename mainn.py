#
# try:
#     file=open("a_file.txt")
#     a_dictionary={"key":"value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file=open("a_file.txt","w")
#     file.write("Something")
#     file.write("I am sahil chalke")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content=file.read()
#     print(content)
# finally:
#     raise TypeError("the message is an error")

height=float(input("Height:"))
weigth=float(input("Weight:"))

if height>3:
    raise ValueError("Human height should not be over then 3m")
bmi=weigth/(height*height)
print(bmi)







