#For PRJNA335821 md5 analysis
#cleaned version; outputs unsorted md5, ftp, alias information
greyskull = "By the power of Greyskull!"

#open command for PRJNA335821 you're interested in examining
upotato = open('C:\\Users\Isaiah\Superior_haploids\ObsExp\PRJNA335821-expected.txt', 'r+')
#open command for file you're interested in writing in
dopen = open('C:\\Users\Isaiah\Superior_haploids\ObsExp\md5-expected-all-go.txt','w')
#open command to edit the md5-observed-all file
obsven = open('C:\\Users\Isaiah\Superior_haploids\ObsExp\copy\md5-observed-all-sorted.txt','r+')


value = []
#vajue = []
#vajuk = []
#values = []
#refer1 = []
#refer2 = []

for line in upotato:
	
	l = line.split('\t')
	
	sup = l[8].split('_')[0:3]				#grabbing from column 9 (ugh), splitting it according to _ and taking columns 1-3 from it = "vt_sup_h<><>"
	md51 = l[-2].split(';')[0]				#grabbing from column 11, splitting by ';' and grabbing the first column contents
	md52 = l[-2].split(';')[-1]				#as above but grabbing column 2's stuff - that is, the md5 thingers, yo
	ftp1 = l[-1].split(';')[0].split('/')[-1]	#grabbing contents of final column and splitting its contents by ';' and taking the first column and splitting it by '/' and taking -1th column
	ftp2 = l[-1].split(';')[-1].split('/')[-1]	#as above but for the second URL of the last column, taking again the last element of the list
	
#	print(sup)								#prints '['run', 'alias']'
											#this is a list- make it a string!
	supr = '_'.join(sup)					#joins elements of sup separated by _
											#this should only affect it if run_alias is multiple long!
#	print(supr)								#prints 'run_alias'
#	print(md51)								#prints 'fastq_md5'
#	print(md52)								#prints 'fastq_md5'
#	print(ftp1)								#prints 'fastq_ftp'
#	print(ftp2)								#prints 'fastq_ftp' - i am grabbing the right columns!
	
	refer1 = md51 + '\t' + supr + '/' + ftp1	#should output as: "MD51 value	<tab here>	vt_sup_h<><>/ftp value corresponding to same sup
	refer2 = md52 + '\t' + supr + '/' + ftp2	#as above
	
#	refer1 = supr + '/' + ftp1 + '\t' + md51	#strange, doesn't change the output - the md51 is still in column 0
#	refer2 = supr + '/' + ftp2 + '\t' + md52
	
	value.append(refer1)					#take value and add refer1 - all md5, sup, and ftp as one element of the list
	value.append('\n')
	value.append(refer2)					#then add refer2 as a separate element
	
#	value.append('\n')						#don't need another return here

#value=sorted(value)						#bad results, loss of structure - refer1\refer2 retain same elemtn status and are sorted together :(
upotato.close()

#md5 = '\n'.join(value)						#weird results - why are their so many extra spaces?
#md5 = ''.join(vajuk)						#awful results
#values = value.sort						#sort darn you
md5 = ''.join(value)
greyskull
dopen.write(md5)
#dopen.write(values)						
dopen.close()

#
#fun facts:
#I'm using negative numbers in md51/2 because I got index errors with positive ones
#I'm using negative numbres in ftp2 because using 1 after first split got me index errors

#new error: cannot change 'list' object to str implicitly; gonna comment out refer1 & refer2 initial definitions
#nope, didn't fix that --- wait, sup is a list, make it a string!
#EUREKA!
#It's working and running fast and hard...don't know if it looks quite right though.
#
#Output in IDLE:
#['vt', 'sup']
#vt_sup
#751dcbc87bb3fa9608ce860e7bda402e
#16b05012dc1cbd16e08cdee35df5bae3
#SRR3994196_1.fastq.gz
#SRR3994196_2.fastq.gz

#these are perfect, but I need to see if the refers and appendices are fine.

#need to:
#figure out how to print this into a new .txt file so I can check this...
#Kirk has effortlessly solved that with <>.write()

#weird results: if I join (value) w/ new lines, I get double spaces between
#solved: added: value.append('\n') between the two reference additionn and got rid of the '\n'.join
#still need to sort it!
#previous cruddy effort was...complicated.
		#	vajue = '\n'.join(value)
		#	vajuk.append(vajue)						#vajue/k resulted in 85Mb txt files.  Nope.

####SORTING!####
#dopen.write(md5.sort)
	#nope: 'str' object has no attribute 'sort'
#md5 = ''.join(value.sort)
	#nope: TypeError: can only join an iteratble
#values = value.sort
	#nope: TypeError: can only join an iterable...so sorting destroys iteratbles?
		#nope: write() argument must be str, not builtin_function_or_method		
#md5 = ''.join(sorted(values))
	#HECK NO!  Strangest one so far, is absolutely bizarre sorting pattern...
#
#new sorting method: redo it, refer1 start w/ supr so that I can sort by supr
	#got strange double column setup again ARG
#Okay, I can only sort lists, not strings; on joining, I am back in a string
	#so i need to sort before I do that
	#but sorting before gets me strange results and has the bad habit of causing or deleting carriage drops


#okay, new-new: Kirk suggests sorting in Unix, by second column, effortlessly.
	#can sort by -h (human numeric sort (so 100 comes after 3), sort by column -k2 (or is it -k1?).
	#cat md5-expected-all.txt | sort -k2				#result: perfect
	#output it cat md5-expected-all.txt | sort -k2 > md5-expected-all-sort.txt
														#result: starts w/ h1-->h10-->h100
														#also has 25 lines of misplaced text...
	#cat md5-observed-all.txt | sort -k2 > md5-observed-all-sorted.txt
														#so they match sorting pattern
#remove first 25 lines using sed in unix
	#sed 'm,nd' file - m and n are min and max range, so
	#sed '1,25d' md5-expected-all-sort.txt > md5-expected-all-sorted.txt

#note: md5-observed-all.txt (and .sorted.txt) uses '  ' (two spaces) between the columns.
	#change that?  again, can use sed, this time sed 's' - sed substitution
	#sed 's/"  "/\"t"' md5-observed-all-sorted.txt > md5-observed-all-sortab.txt
	#this isn't working, sed s isn't recognizing the spaces as being something to replace.  curious.
	#python method:

obsven = open('C:\\Users\Isaiah\Superior_haploids\ObsExp\copy\md5-observed-all-sorted.txt','r+')

for line in obsven:
	line.replace('  ','/t')								#should replace '  ' with tab in each line
obsven.close
#result 1: nope, not changing it.

#found more sed stuff:
	#sed 's/[[:space:]]*/TAB/g' md5-observed-all-sorted.txt > md5-observed-all-sortab.txt
		#WAHAHAHAHAHA!  This has put TAB right before every single character!  Nope nope nope.
#found an awk...oh awk, you...
	#awk '{gsub("  ","\t");print}' md5-observed-all-sorted.txt > md5-observed-all-sortab.txt
		#works perfectly.  Awk, all is forgiven.

	
#and get the differences between file (there will be, there are differences in file
	#diff - md5-observed-all-sortab.txt md5-expected-all-sorted.txt > md5-dif-01.txt
	#option:	-I == ignore matching lines
	#			-y == output in two columns
	#not being recognized, do simple.
	
	#diff md5-observed-all-sortab.txt md5-expected-all-sorted.txt > md5-dif-01.txt
		#the output is...unreadable.  Well, I can *try* but I can't make heads or tails.
		#need options.

	#diff -qy md5-observed-all-sortab.txt md5-expected-all-sorted.txt > md5-dif-02.txt
		#-q = brief (only when files differ)
		#-y = output in two columns, side by side
		#...lol, q makes it only do "they differ" in the file :p
		#do without -q yo
	#diff -y md5-observed-all-sortab.txt md5-expected-all-sorted.txt > md5-dif-03.txt
		#okay, so there are some differences and they are true differences (not just a line misplaced elsewhere in the file).
		#output is convenient but I will make another to just output the exact differences
	#diff --suppress-common-lines md5-observed-all-sortab.txt md5-expected-all-sorted.txt > md5-dif-04.txt
		#...is this outputing the left (observed) or right (expected) columns?  both?
	#diff -y --suppress-common-lines md5-observed-all-sortab.txt md5-expected-all-sorted.txt > md5-dif-05.txt

		
#