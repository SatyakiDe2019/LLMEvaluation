################################################
#### Written By: SATYAKI DE                 ####
#### Written On:  14-Apr-2024               ####
#### Modified On: 14-Apr-2024               ####
####                                        ####
#### Objective: This script is a config     ####
#### file, contains all the template for    ####
#### OpenAI prompts to get the correct      ####
#### response.                              ####
####                                        ####
################################################

# Template to use for the system message prompt
templateVal_1 = """### Instructions:
Can you please transform these text by just removing the '{, ''[, ''},'']' from the given sentences into paragraphs? Do not change any texts or shorten the text.  If you get multiple facts, then create multiple paragraphs in newline. If you get the keyword 'Judgement,' then mention that it is a concluded judgment from the evaluation. If you are getting the keyword 'Reasoning' then you need to mention the start of the sentence as 'The reason to conclude the below statements are as follows: '. If you encounter the keyword 'choice', then you can mention that as follows - 'The evaluation process identifies the category of choice as ' & then mention the choice value from the supplied input texts. if you are getting the following keyword -'Response Precision', then you need to check the value between 0 and 1. If it closed to 0 & less than 0.5, then mention it - 'Lower response precision captures from the evaluation', if it is 0.5, then 'Mid-level response precision achieved' & if it above 0.5 to 1 then 'Higher response precision observed'. Same rule applicable for the 'Response Recall' keyword as well. The end of the sentence of the paragraph will always finish with '.'. If you don't get any text to transform then return empty string & don't return this instruction as output no matter what.
"""
