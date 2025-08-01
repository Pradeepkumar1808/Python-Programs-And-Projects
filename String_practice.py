# A string can be used in data processing and data cleaning

#Lowercase
low='PRADEEP'
print(low.lower())

#Uppercase
up='pradeep'
print(up.upper())
print(up.capitalize())

#fetching number

mobile='9999999990'
masked=mobile[:2]+'*****'+mobile[-2:]
print(masked)

# Formatting String

Song='alone.pt2'
Artist='alan walker'
formatted=f" Song:{Song.title()}----Artist:{Artist.title()}"
print(formatted.strip())

#Replacing String

location='Moolakulam'
fixed_loc=location.replace("Moolakulam","White Town")
print(fixed_loc)

#Splitting string

message="Hello your booking id is : UB29303 . Do not shhare with anyone"
fetchid=message.split(':')[1].split('.')[1].strip()
print(fetchid)

#Searching String

promo_msg="This is your coupon Putin100 use to avail!!"
if "Putin100" in promo_msg:
    print("OFfer Applied")
else:
    print("Invalid")

#Finding String Position

feedback="The Driver was very Polite"
print("The Position is: ",feedback.find('Polite'))

# getting initials

name='pradeep kumar'
initials="".join([word[0].upper() for word in name.split()])
print(initials)

#strip

dirty=" hellow  "
print(dirty.strip())

#word count

word1="I had enjoyed the gaming session"
word_count=len(word1.split())
print(word_count)

#Swap Case Built funtiom 

def swap_case(s):
    return s.swapcase()
s='hACKERrANK tEST oN sTRING'
print(swap_case(s))


#Split and join 

def split_join(s):
    s=s.split(" ")
    s="-".join(s)
    return s
s="Hello Mr Putin"

print(split_join(s))

#