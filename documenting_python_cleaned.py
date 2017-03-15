#For PRJNA335821 md5 analysis
#cleaned version; outputs unsorted md5, ftp, alias information
greyskull = "By the power of Greyskull!"

#open command for PRJNA335821 filepath:
upotato = open('C:\\Users\Isaiah\Superior_haploids\ObsExp\PRJNA335821-expected.txt', 'r+')
#open command for file you're gonna write to:
dopen = open('C:\\Users\Isaiah\Superior_haploids\ObsExp\md5-expected-all-go.txt','w')

value = []									#will have everything of value stashed within

for line in upotato:
	
	l = line.split('\t')
	
	sup = l[8].split('_')[0:3]				#grabbing from column 9 (ugh), splitting it according to _ and taking columns 1-3 from it = "vt_sup_h<><>"
	md51 = l[-2].split(';')[0]				#grabbing from column 11, splitting by ';' and grabbing the first column contents
	md52 = l[-2].split(';')[-1]				#as above but grabbing column 2's stuff - that is, the md5 thingers, yo
	ftp1 = l[-1].split(';')[0].split('/')[-1]	#grabbing contents of final column and splitting its contents by ';' and taking the first column and splitting it by '/' and taking -1th column
	ftp2 = l[-1].split(';')[-1].split('/')[-1]	#as above but for the second URL of the last column, taking again the last element of the list
	
	supr = '_'.join(sup)					#joins elements of sup separated by _
	
	refer1 = md51 + '\t' + supr + '/' + ftp1	#should output as: "MD51 value	<tab here>	vt_sup_h<><>/ftp value corresponding to same sup
	refer2 = md52 + '\t' + supr + '/' + ftp2	#as above
		
	value.append(refer1)					#take value and add refer1 - all md5, sup, and ftp as one element of the list
	value.append('\n')
	value.append(refer2)					#then add refer2 as a separate element
	
upotato.close()

md5 = ''.join(value)						#value is a long list; join it into a string
greyskull
dopen.write(md5)
dopen.close()