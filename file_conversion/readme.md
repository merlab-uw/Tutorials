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

#### ``radiator`` in R


#### Custom scripts