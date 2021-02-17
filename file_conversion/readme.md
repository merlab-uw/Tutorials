# File conversion

When embarking upon your population genetic analyses, you will quickly find that changing file formats is a big part of the work. Changing file formats can be be really time-consuming, esecially when first getting started on your analyses. To help, we've synthesized resources for doing so quickly and reproducibly! Here, we'll cover PGD Spider, the R package ``radiator``, and some custom scripts our lab has put together.


## [1] PGD Spider

![logo](https://github.com/merlab-uw/Tutorials/blob/master/imgs_for_repo/pgd_spider_logo.PNG?raw=true)

[PGD Spider](http://www.cmpg.unibe.ch/software/PGDSpider/) is a Java program for converting among filetypes, to help you work across programs in population genetics. It has both a GUI version and a command line version. First, we'll walk through the GUI version.

Once you open the application, you'll need to specificy the path to your input and output files, as well as the file formats for each (e.g., VCF, genepop, structure, etc.). You'll also need to specificy a bunch of options, which you can save in a SPID file. Here's what the application window looks like.

![app_window](https://github.com/merlab-uw/Tutorials/blob/master/imgs_for_repo/pgd_app_orientation.PNG?raw=true)

As an example, let's convert a VCF file to a Genepop file. First, I specify the input file format (VCF) and the output file format (Genepop) from the drop down windows. I also specify the input and output paths. You can see here that I have a VCF file called ``really_fun_genotypes.vcf`` (a girl can dream) on my desktop, and I've made a path to the output file that will get written in the same location with the same name, just a different file extension (Genepop files get ``.gen`` or ``.txt`` depending on the program).

![input_output](https://github.com/merlab-uw/Tutorials/blob/master/imgs_for_repo/pgd_input_output.PNG?raw=true)

Now it's time to pick some conversion options, which get stored in a SPID file. You'll get prompted to edit the SPID file if you try to click ``Convert`` before specifying the options.  If you don't already have a SPID file with the desired options specificed, you can click ``Create /Edit SPID`` and specify those options manually. Otherwise, you can read in an existing SPID file.  Using saved SPID files is handy if you always convert files the same way, or want to be sure you're being consistent in how you convert files. Here's what the app looks like when you're creating or editing a SPID file, and note that there's a tab for parsing the input format and writing the output format. These options differ based on format.

![options](https://github.com/merlab-uw/Tutorials/blob/master/imgs_for_repo/pgd_vcf_options.PNG?raw=true)

Then you're ready to convert! Click ``Save and Apply`` if you want to save this SPID file for future use, or to remember what options you chose. Otherwise, click ``Apply``. Here's what my log window looked like after running.

![log](https://github.com/merlab-uw/Tutorials/blob/master/imgs_for_repo/pgd_log.PNG?raw=true)

Simple enough, right? There are some few other things to note, like not all file formats can be converted to all file formats. You can read more in the original documentation [here](http://www.cmpg.unibe.ch/software/PGDSpider/).

Now, check out [this notebook](https://github.com/merlab-uw/Tutorials/blob/master/file_conversion/using_PGDSpider_at_commandline.ipynb) to see how to use PGD Spider at the command line! This is extra handy if you'd like to use PGD Spider to convert file formats within a pipeline. Here's what the call looks like this.

![cl](https://github.com/merlab-uw/Tutorials/blob/master/imgs_for_repo/pgd_command_line.PNG?raw=true)



## [2] Radiator 


[Radiator](https://thierrygosselin.github.io/radiator/index.html) is an R package that is "designed and optimized for fast computations of diploid data using Genomic Data Structure (GDS) file format and data science packages in the (mighty) [tidyverse](https://www.tidyverse.org/). Radiator handles VCF files with millions of SNPs and files of several GB." It also has a nifty command called  ``` genomic_converter ``` that can be used to convert files into formats (e.g., plink, vcf, stacks haplotype file, genepop, genind, genlight, etc.) used by different analytical programs.

To install Radiator, [follow the instructions provided on the program's GitHub page](https://thierrygosselin.github.io/radiator/index.html)

Let's walk through the R script for a file conversion together. In this example, we will convert a small [vcf file containing genotypes](herring.vcf) into a *genlight* file format using radiator. To do this, we will also need a [tab-delimited text file](herring_strata.tsv) that has two columns: INDIVIDUALS and STRATA. The INDIVIDUALS column contains individual sample names, while the STRATA column designates the population (or whatever hierarchical grouping) of origin for each individual sample.  

Here is the example R script:

``` r

# Load the necessary libraries
library(radiator)
library(SeqVarTools)
library(rlang)

# I am going to specify the working directory where I have saved the vcf file ("herring.vcf")
# and the strata file ("herring_strata.tsv") that are our input data.

DIR <- "C:/Users/Eleni/Documents/radiator"

setwd(DIR)


# I am going to specify the name of my vcf and strata files:
my_vcf <- "herring.vcf"
my_strata <- "herring_strata.tsv" 


# Let's verify that our vcf file is detected by radiator as the correct format:
radiator::detect_genomic_format(data = "herring.vcf")


# Lets convert the data into "genlight" format (used by R package adegenet) using radiator's genomic_converter function

herring_data <- genomic_converter(
  data = my_vcf, 
  strata = my_strata,
  output = c("genlight"))


#Get the content of the herring_data object created using:
names(herring_data)

#To isolate and work with the genlight object:
genlight <- herring_data$genlight

```


## [3] Custom scripts

There are a couple of situations in which you might need to use a custom script to achieve your file conversion goals. 

It might be that the file format you have is very close to what is required by one of the major file conversion programs like PGD Spider, but needs a couple of 'tweaks' before the program will accept it. For instance, genepop outputs a file with a list of the loci (one locus per line) at the beginning of the file, but most programs require the genepop format to be completely tabular, with these loci in one row, like the header or column names for the data. 

Or because of your bioinformatics pipeline, you end up with several files, all of the same type, that need to be combined into one larger file for downstream analysis. You can do this fairly easily in R, but you might also want to quickly combine them with a custom script before using a file conversion program to change the file to another format for further analysis. 

We have had success writing custom scripts to acheive goals such as these in python, but there are other ways to do it too, and anything that gets the job done in the time frame you want is a good way to do it. 

Here is an example of a custom script that combines VCF files. These have to have the same loci in the same order: 

```
#This is a script to combine VCF files, it appends a VCF to the end of an existing VCF, both VCFs must have the same loci in the same order. 
#this runs with: python name_of_the_script.py vcf_file1_name.vcf vcf_file2_name.vcf

import io
import re
import sys

#f1 = sys.argv[1] File to be appended to
#f2 = sys.argv[2] File being appended to the first 

f1 = open(sys.argv[1], 'a')
with io.open(sys.argv[2], 'r') as f2:
	for line in f2:
		if '#CHROM' in line:
			continue #if line contains('#CHROM') skip it, this is the header
		else: 
			f1.write(line)
f1.close()
f2.close()

```
To test that you have the number of lines you would expect in your new vcf file, you could use this script that counts the number of lines: 

```
#This is a script to check the combined length of any file, especilly handy for files too large to open in text editors. 
#this runs with with: python name_of_the_script.py file_to_count_lines_of.txt

import io
import re
import sys

i = 0
with open(sys.argv[1]) as f:
	for i, l in enumerate(f):
		pass
	i + 1

print i

```

Here is an example of a custom script that takes a file in the genepop format that has each locus name on its own line, and reformats it so that all the locus names are tab separated on one line and re-formats the file it to be easily opened in R. 

```
#This is a script to take one genepop file that does not have one locus per line, and edit the formatting so that it can be imported to R as a table. 
#this runs with with: python name_of_the_script.py genepop_file_to_reformat.genepop genepop_output_name.txt

import io
import re
import sys


#f2 = sys.argv[2] Output file
#f1 = sys.argv[1] Genepop file to edit
f2 = open(sys.argv[2], "w+")
with io.open(sys.argv[1], 'r') as f1:
	for line in f1:
		if 'Stacks' in line:
			continue #if line contains('Stacks') skip it
		if re.match(r'pop', line): #if the line contains pop, skip it
			continue
		if re.match(r'P', line): #if the line contains a sample, 
			f2.write(line) #write it to the output file unchanged
		else: 
			f2.write("\t" + re.sub(r',', "\t", line))
		#if it is the second line, (no pops or population name or stacks) write a tab, then split the remainder by replacing the , with tabs
	f1.close()
	f2.close()
  
  ```


This is a script that edits all the genepop formatted output files that have written by Stacks, and formats them so you can easily open them in R for filtering and downstream analysis. This is useful if you have split your analysis up in Stack using the option "whitelist" or "blacklist". The file names should all follow the same naming scheme. This script was inspired by one Garrett McKinney wrote in Perl to accomplish a similar thing. 

```
#This is a script to take the genepop files that are made with iterative runs of populations and edit them so they are formatted for R
#the files are not combined, they are individually edited, you will still have the same number you started with. 

import io
import re

for i in range(1,30): #change this to the # of whitelists/blacklists you have

	#this opens your output file and it creates the file if it doesnt exist
	f2 = open("whitelist_" + str(i) + ".genepop", "w+")
  
	with io.open(r'whitelist_' + str(i) + r'\batch_4.genepop', 'r') as f1: #change the name of the file to suit your needs
		for line in f1:
			if 'Stacks' in line: #if line contains('Stacks') skip it
				continue 
			if re.match(r'pop', line): #if the line contains pop, skip it
				continue
			if re.match(r'P', line): #if the line contains a sample, #change this to match your sample names
				f2.write(line) #write it to the output file unchanged
			else: 
				f2.write("\t" + re.sub(r',', "\t", line))
			#if it is the second line, (no pops or population name or stacks) write a tab, then split the remainder by replacing the comma with tabs
		f1.close()
		f2.close()
    
    ```

