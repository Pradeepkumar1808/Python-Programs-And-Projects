def create_profile(**kwargs):
    print("Profile")
    for key,value in kwargs.items():
        print(f"{key} : {value}")
create_profile(Name='Pradeep',Age=20,Occupation='Data Engineer')