# Distilled-Bert-Search-using-Attention-based-Sentence-Transformers
The evolution of digital communication technology and innovative Machine
learning tasks, the ability to offer high quality support to clinicians has stemmed 
magnificent new capabilities. The success is subjected to understand the intrinsic
processes being used in classical pathway by which clinicians make decisions.Clinical
decision making is a balanced known best exercise in terms of evidence and study,
it deals with awareness of the current situation and environment, and familiarity of a patient.
Since every day Clinical,Doctors tries to obtain information which needs to be precised and for that 
they search for Article and for that they use General Search Engine such as Google. I built a web 
based application in which user will upload the Query and result will be given to him as a NCTID of Article 
with links and Score of the Article. I am utilizing TREC PRECISION MEDICINE 2018
dataset which is basically a CLINICAL TRIAL SNAPSHOT. There were 2410000(Two Lakhs fourty one
thousand approx) article. And for it to be precised I have used a Attention based classifier 
which will first classify the article into Human precision medicine or not .After that total number 
of article are reduced and in other words more precised.
There were 2410000(Two Lakhs fourty one thousand approx) articles in Clinical Trial Trec Dataset. 
Since these are to large And for it to be precised I have used a Attention based classifier which 
will first classify the article into Human PM or  NOT PM.After that total number of PM articles
are reduced to 10 thousand (more precised) . I Extracted atricle Title and Summary in Text formatand
then used a attention based sentence transformer in order to calculate the contextual embeddings.

Also I got  query from the user in flask application and  converted with the same Sentence 
Transformer embedder and using the BM25 score calculation method I used both the article embeddings
and query embedding to get the score for top 10 Articles(we can increase /Decrease this) .And Finally 
presented them as output to user
