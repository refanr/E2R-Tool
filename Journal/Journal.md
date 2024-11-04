# Journal

### 4.11 2024 
Data collection and a plan of action. I have been collecting the text from e2r news and "normal" news in seperate files. The plan is to use word frequency on a large corpus of icelandic text to find more/less commonly used words and use that as a complexity measure of the words, the rationale being that more commonly used words are less complex than their more seldom used counterparts. What I want to do is to run a sentence through my system and if it detects a word with a certain level of complexity, it will suggest a replacement from the word embeddings.
Next thing I want to do is to use Greynir to analyze the sentence structure of e2r news compared to "normal" news. Maybe there is a sentence structure that is more used than others in the e2r news, and I can somehow use that to suggest a simpler sentence structure in the system.

### 3.11 2024
Another thought came to mind. Use all the text from the e2r news items and analyze the sentences, words per sentence, number of syllables in words, type-token ratio TTR, to measure the "richness" of the language used. At least I will start by scraping all the text from all the news items in the e2r section.


### 2.11 2024
It is kind of getting to a crunch time in this project, others too but that is besides the point. What I am focusing on the next few days is collecting data from the e2r news at ruv.is. I am not sure I can use the model from the l2 dataset, but we'll see. So I've just spend an hour and a half collecting data, this is really slow and I am not able to use any automation for this since the e2r news and the "normal" news are not completely the same, sometimes there are paragraphs in the "normal" version that have no corresponding paragraph in the e2r, and there are more definitions in the e2r versions.

### 23.10 2024
Working on the dataset from class. I trained a BERT transformer model on this dataset, and am testing it out at the moment. If I can use this model to predict the competency level of the sentence input, maybe I can use the e2r news data to simplify the "normal" sentences, using the e2r sentences as a benchmark.

### 14.10 2024
Downloading the MIM-GOLD and MIM datasets from clarin. I want to try out word embedding with word2vec using this data. 

### 13.10 2024
Keep working on extracting the text from the ruv.is/audskilid news items. I am trying to do this programmatically, but its not working out. I am thinking of extracting some manually, just to get started. 

### 10.10 2024

I started gathering data last night and this morning. From what I can gather, I will need to pretrain a model on general text. I have available to me a lot of resources on clarin, Gigaword corpus, word frequency data, sentence standardization, etc. What I am missing is complex-to-simplified dataset, ruv.is produces some news items in an e2r form, which links to the news item in the original form, which might be a good starting point. This seems like it is about 39 e2r items, so it is quite tiny, maybe I can contact someone over at ruv to get access to more material.
I have also started thinking about how I can create an RNN or model to assess the simplicity of a sentence, to somehow grade text on how simple it is. I was kind of fired up about this paper that I read last night, *Were RNNs All We Needed?* about methods to minimize and simplify LSTMs and GRUs which made them hundreds of times faster compared to older, full versions. I thought to myself, maybe I can use this to help with the text simplification.

### 29.9 2024
Today and last night, I was researching papers and methods to accomplish my task. I found a few resources, papers for me to read and look into: *[Automatic Simplification of Scientific Texts...](https://ceur-ws.org/Vol-3497/paper-242.pdf)* and *[Simplex: a lexical text simplification architecture](https://arxiv.org/pdf/2304.07002)*  

I found out about **SARI**, a way to measure the complexity of sentences in NLP tasks, and I tried writing down the problems and challenges I can imagine for each task, *Lexical simplification*, *Syntactical simplification* and *Stylistic simplification*. I made some decision about the UI of the finished "product".  

I feel it is better for me to write things out to "think" about them, kind of like thinking outloud. I have also gotten into the habit of "chatting" with chatgpt about my thoughts and ideas, maybe get some insight as well as shedding some light on challenges I had not thought of before.  

I've decided to keep a bit of a log here on Github to try to document my process through this project.