import csv

'''
with open('neighbors-states.csv', 'rb') as nbf, open('out.txt', 'w') as o:
        neighs = csv.reader(nbf , delimiter='\n')

        next(neighs, None)

        
'''

with open('russia_federal_subjects.csv', 'rb') as nbf, open('out.txt', 'w') as o:
        neighs = csv.reader(nbf, delimiter=',')

        next(neighs, None)

        for row in neighs:
                o.write ("self.S{}.neighbours.append(self.S".format(row[0]))
                o.write ("{})\n".format(row[1].replace(' ', '')))
 


# o.write("self.{}.neighbours.append(self.{})\n".format(row[0].replace(' ', ''), row[1].replace(' ', '')))