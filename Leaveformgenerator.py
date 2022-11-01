from xml.dom import DomstringSizeErr

#Leave Letter Generator

Name=str(input("Student name : "))
Department=str(input("Department name : "))
College_name=str(input("College Name :"))
College_Place=str(input("COllege Place : "))
Teacher=str(input("Teacher name : "))
Subject=str(input("Subject : "))
Reason=str(input("Reason : "))
day=str(input("How much days : "))
date_of_leave=str(input("Dates of Leave : "))
Date=str(input("Date : "))
Place=str(input("Place : "))
Final= f'''
From
    {Name}
    {Department}
    {College_name}    
    {College_Place}

To
  {Teacher}
  {Department}
  {College_name}
  {College_Place}

Respected Sir,
    Sub:{Subject}
      I am {Name}. Studying in {Department}. I'm not able attend my class today
due to {Reason}.I want a permission to take a leave for {day} days {date_of_leave} . kindly give permission 
to take a leave.
                                    Thank You
Yours Sincerely
{Name}

Date:{Date}
Place:{Place}
'''
print(Final)
