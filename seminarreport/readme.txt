%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
User Guide for seminar.tex and seminar.bib

% Prepared By : Dept of CSE, MESCE, Kuttippuram
% Date        : 12th July 2011, 6:53 PM
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


This bundle contains a template to be followed for the seminar papers. 

1. seminar.tex  => the tex file for seminar report.
2. seminar.cls  => class files. This file SHOULD NOT be modified.
3. seminar.bib  => bibliography database for references

% =====================================================================
% How to use seminar.tex

1. This is the "base" file for your seminar report.
2. Make a copy of this file, rename it to your roll number, and start working on it.
3. Open your tex file (created as said in step 2).
4. Go to the section named "%%%%%%%%%%%% Parameters To be populated by the author START %%%%%%%%%%%%%". 
5. Add your own entries for title, author, advisor (guide), roll nmuber and academic year, in this section. 
6. Go to the section named "%%%%%%%%%%%% Add your abstract here! START %%%%%%%%%%%%%" and add the 
   abstract in the \abstract{} section.
7. Save seminar.tex.


8. Now, prepare the chapters of your report as ch1.tex (introduction),.......
9. Include these chapters in seminar.tex as follows:
   9.1) Go to the section named "%%%%%%%%%%%% BEGIN DOCUMENT...  %%%%%%%%%%%%%"
   9.2) Locate the command "\input ch1.tex" and replace ch1.tex with your chapter name (For e.g.,  
        if you have given intro.tex as the file name for your introduction part, repalce "ch1.tex" 
        with "intro.tex").
   9.3) Add other chapters also in the same way.

10. When you add a citation, first it is to be added to the seminar.bib file. Later it can be cited in your tex file.
% =====================================================================
