'''
                                Encapsulation
Encapsulation allows you to hide the internal state of an object from the outside world. This
means that the Object's attributes can only be accessed/modified through its methods. This prevents
external entities from damaging the object

TLDR: Hidding attributes from code outside the class
        They become inaccessible from outside the class
'''

# class ytChannel:
#     def __init__(self, name, vids, subs, aName):
#         self.chName = name
#         self.vidCount = vids
#         self.subCount = subs
#         self.adminName = aName


# channel1 = ytChannel('Zainematics', 1300, "134k", "Bakhtawar")
# print(channel1.chName)
# 'I wanted to write KGM as an admin name, but I accidentally wrote it as chName'
# channel1.chName = "KGM"
# print(channel1.chName)



# PRIVATE chName : STRING
class ytChannel:
    def __init__(self, name, vids, subs, aName):
        '''
        - we will always write as parameter self in any function made within a class
        - we will NEVER pass self as an argument while calling any function from a class
        '''
        self.__chName = name
        self.vidCount = vids
        self.subCount = subs
        self.adminName = aName

    def get_chName(self):
        return(self.__chName)
    def set_chName(self, newName):
        self.__chName = newName


'A getter is a function that returns a private variable outside a class'



'DOES NOT LET ME MAKE SUCH MISTAKES BY GIVING AN ERROR'
channel1 = ytChannel('Zainematics', 1300, "134k", "Bakhtawar")
# print(channel1.chName)
# 'I wanted to write KGM as an admin name, but I accidentally wrote it as chName'
# channel1.chName = "KGM"
# print(channel1.chName)

'BUT I STILL MIGHT WANT TO PRINT THE CHANNEL NAME  -> Make a getter in your class'
name = channel1.get_chName()
print(name)


'What if I genuinely want yo edit my private variable name'
channel1.set_chName("KGM")

name = channel1.get_chName()
print(name)



# MAKING A NEW OBJECT
channel2 = ytChannel('pewdiepie', 13000, "100M", "Bakhtawar")
name = channel2.get_chName()
print(name)
