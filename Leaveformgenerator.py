from xml.dom import DomstringSizeErr


Name=str(input("Student name:"))
Department=str(input("Department name:"))
Teacher=str(input("Teacher name:"))
Subject=str(input("Subject:"))
Reason=str(input("Reason:"))
day=str(input("How much days:"))
Date=str(input("Date:"))
Place=str(input("Place:"))
Final= f'''
From
    {Name}
    {Department}

To
  {Teacher}
  {Department}

Respected Sir,
    Sub:{Subject}
      Hi sir Im {Name} studying in {Department} as i needed a leave because {Reason} so I request you to grant me a leave for {day} and I hope you understand my situation.

Yours Sincerely
{Name}

Date:{Date}
Place:{Place}
'''
print(Final)