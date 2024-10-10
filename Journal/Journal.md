# Journal

### 10.10 2024

I started gathering data last night and this morning. From what I can gather, I will need to pretrain a model on general text. I have available to me a lot of resources on clarin, Gigaword corpus, word frequency data, sentence standardization, etc. What I am missing is complex-to-simplified dataset, ruv.is produces some news items in an e2r form, which links to the news item in the original form, which might be a good starting point. This seems like it is about 39 e2r items, so it is quite tiny, maybe I can contact someone over at ruv to get access to more material.
I have also started thinking about how I can create an RNN or model to assess the simplicity of a sentence, to somehow grade text on how simple it is. I was kind of fired up about this paper that I read last night, *Were RNNs All We Needed?* about methods to minimize and simplify LSTMs and GRUs which made them hundreds of times faster compared to older, full versions. I thought to myself, maybe I can use this to help with the text simplification.

### 29.9 2024
Today and last night, I was researching papers and methods to accomplish my task. I found a few resources, papers for me to read and look into: *[Automatic Simplification of Scientific Texts...](https://ceur-ws.org/Vol-3497/paper-242.pdf)* and *[Simplex: a lexical text simplification architecture](https://arxiv.org/pdf/2304.07002)*  

I found out about **SARI**, a way to measure the complexity of sentences in NLP tasks, and I tried writing down the problems and challenges I can imagine for each task, *Lexical simplification*, *Syntactical simplification* and *Stylistic simplification*. I made some decision about the UI of the finished "product".  

I feel it is better for me to write things out to "think" about them, kind of like thinking outloud. I have also gotten into the habit of "chatting" with chatgpt about my thoughts and ideas, maybe get some insight as well as shedding some light on challenges I had not thought of before.  

I've decided to keep a bit of a log here on Github to try to document my process through this project.