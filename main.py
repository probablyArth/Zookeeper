# Create a dictionary of names and assign numbers to them
names_dict = {"1": "Bats", "2": "Bears", "3": "Birds", "4": "Camels", "5": "Cats"}

# Create a dictionary of Their respective ASCII ART and assign numbers to them
img_dict = {
    "1": """    =/\                 /\=
              / \'._   (\_/)   _.'/ \
             / .''._'--(o.o)--'_.''. \
            /.' _/ |`'=/ " \='`| \_ `.\
           /` .' `\;-,'\___/',-;/` '. '\
          /.-' jgs   `\(-V-)/`       `-.\
          `            "   "            `
        """
        ,
    "2": ''' __         __
          /  \.-"""-./  \
          \    -   -    /
           |   o   o   |
           \  .-"""-  /
            '-\__Y__/-'
               `---`
        '''
        ,
    "3": """
           ___     ___
          (o o)   (o o)
         (  V  ) (  V  ) 
        /--m-m- /--m-m-
        """
        ,
    "4": """
       _v   ,,
      /`|   &&.
      `-\`-&&&&&.
         \&&&&&&&\
          &&#""&& \
         / |   |\  x
         \ |  / /
        """
        ,
    "5": '''
     _._     _,-'""`-._
    (,-.`._,'(       |\`-/|
        `-.-' \ )-`( , o o)
              `-    \`_`"'-
        '''
}

# Print The list of Animals

print(f""" ================= Enter the respective number to see the image of that animal and type exit to quit ================""")
for i in range(1, 6):
    print(f'{str(i)}. {names_dict[str(i)]}')


while True:
    inp = input("Animal number or exit to quit: ")
    if inp == "exit":
        break
    elif inp in names_dict:
        print(img_dict[inp])
    else:
        print("Enter a valid input")