import csv

'''
with open('neighbors-states.csv', 'rb') as nbf, open('out.txt', 'w') as o:
        neighs = csv.reader(nbf , delimiter='\n')

        next(neighs, None)

        for row in neighs:
                # self.Kharkiv.neighbours.append(self.Luhansk)
                o.write("self.{}.neighbours.append(self.{})\n".format(states[row[0]].replace(' ', ''), states[row[1]].replace(' ', ''))
                o.write("self.{}.neighbours.append(self.{})\n".format(states[row[1]].replace(' ', ''), states[row[0]].replace(' ', 
'''

with open('Federal subjects.tsv', 'rb') as nbf, open('out.txt', 'w') as o:
        countryelement = csv.reader(nbf, delimiter=',')

        next(countryelement, None)

        for row in countryelement:
                o.write("self.{} = CountryElement('{}')\n".format(countryelement[row[0]].replace(' ', ''), countryelement[row[0]])) 

