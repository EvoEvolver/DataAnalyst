# 🤖🔎 DataAnalyst

Data Analyst is a program that leverages machine learning to perform automatic data analysis on JSON files. Simply feed it a schema JSON to show it how your files are structured, and it will be able to automatically generate a data analysis pipeline that answers any questions you throw at it!

## 📁 Project Structure

```text
.
├── mockData
│   ├── fewshot_examples    
|   ├── Level 1  
|   ├── Level 2  
|   └── Level 3    
├── pipeline
│   ├── pipeline_asteroids.ipynb
│   ├── pipeline.ipynb   
│   ├── examples_info.txt
│   ├── regular-gpt.ipynb
│   └── shortener.py
└── README.md                       # You are here! :)
```

The `mockData` directory contains, you guessed it, mock data. 
 - `Level 1`: contains easy to analyze JSONs
 - `Level 2`: contains somewhat difficult JSONs that are closer to real-life applications of Data Analyst
- `Level 3`: contains very difficult JSONs that can be used to ask open-ended, more insightful questions.

The `pipeline` directory contains the ML-driven pipeline that automatically generates a data analysis pipeline.

 - `examples_info.txt`: contains the questions to use for each example, as well as the paths to the input and JSON schemas so you can easily copy and paste :)

 - `pipeline_asteroids.ipynb`: an ML-driven pipeline that contains some hacks to make the Level 2 > asteroids example work correctly

 - `pipeline.ipynb`: the ML-driven pipeline that works for all examples (but not so well for the Level 2 > asteroids example)

 - `regular-gpt.ipynb`: a pipeline that just asks GPT to write code to answer the user query in a straightforward manner. This is used for comparison.

## 🔧 Hacks (temporary)

- There is a separate pipeline specifically for the asteroids example, since it needed a couple changes to the pipeline. In the validation step, there is an additional check and fewshot example. The check is to see if all the keys GPT identified actually exist in the JSON, and the fewshot example is to show GPT that if you can't find a property, then you should see if you can calculate it using other keys. Additionally, in the Generate Answer section, first we ask the model to think about how to write the function, then we make the model write it. This seemed to help when I tested it, as opposed to just asking it to write the function.

- In the `pipeline` file's second cell (the setup cell), there is a block of code that is commented out. Uncomment it when using the NBA example, since it does some JSON shortening

 - The second cell of `pipeline` and `pipeline_asteroids` has a `shortenJSON` flag that can be used to turn on/off JSON shortening. Turn it off for the mental health example, otherwise it may not work correctly.

## ❗ Current issues (hopefully temporary)

- Currently the JSON shortener simply truncates strings that are above a certain length. This does not work well for a few reasons
<br><br>1. It can remove important information. For example, in the mental health example, survey questions are stored like so:<br><br>
```"question": "<strong id=\"docs-internal-guid-5fe31601-29b5-cdd7-9eab-ac5384b8bb15\" style=\"font-weight: normal;\">Does your employer provide mental health benefits<strong id=\"docs-internal-guid-3c0f58bf-4d33-e6ee-c1bd-70bba80db500\" style=\"font-weight: normal;\"> as part of healthcare coverage</strong>?</strong>"```
<br><br> As such, if we cut off the string, we might lose the actual question buried in the middle, and thus we can't perform the analysis correctly.<br><br> 2. Shortening the values isn't enough. Some JSONS will simply have too many keys, resulting in a context length error from OpenAI. For example, the NBA example has a large amount of keys, and no amount of string shortening will fix this. We have to delete unnecessary keys if we don't want a context length error.<br><br>As for solutions, we could:
<br><br>1. Split the JSON up into parts, and feed each part to a model. These models would determine what keys from its part it thinks might be useful in answering the user query. The results are then sent to another model, which looks at all the possibly useful keys and determines which are actually necessary. Then, all the other unnecessary keys are deleted.
<br><br>2. Look into tools like LLMLingua that perform compression on prompts.

- The asteroid example is not working as well as when I tested it. It seems that it often either errors or gives an incorrect answer.

## 🗒️Other Notes

 - If the pipeline does not produce a correct result for an example 100% of the time, that's okay. We can run the pipeline multiple times for an example (maybe have a multi-threaded app with each thread running one instance of the pipeline) and then choose the majority result as the final result.