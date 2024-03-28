import pandas as pd

people = {

'age' :[15,16,16,15],

'name' :['Adam','Bob','Dave','Fred'],

'teacher' :['Ashby','Ashby','Jones','Jones']

}

people = pd.DataFrame(people)
print(people)