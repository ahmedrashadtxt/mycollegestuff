#open a file
fo = open('abc.txt','r+')
fo.write( 'My favourite subject is Programming and Program Design \n')
fo.write('Programming is one of the most important subject in my course \n')
fo.write('My main aim is to get an "A" grade for programming \n')
#close open file
fo.close()


#open a file
fo = open('abc.txt','a')
fo.write( 'UCSC is a H/E institute affiliated to the University of Colombo \n')
fo.write( 'UCSC is providing CS and ICT education \n')
fo.write( 'Address : 35 Philip Gunawardena Mawatha, Colombo 7 \n')
#close open file
fo.close()
