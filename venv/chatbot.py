import tensorflow as tf
import json
var=inputm.get()
print(tf.version)
data={
    "version": "v2.0",
    "data": [
        {
            "title": "your_title",
            "paragraphs": [
                {
                    "qas": [
                        {
                            "question": var,
                            "id": "1",

                        },

                    ],
                    "context": "Hiii, how can i help?:). fine hope you're doing well too. sundar pichai is the ceo of google. I am a chatbot. I was developed by HRITIK GUPTA and DIVYAM PAL. Google was founded in 1998 by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University in California.Together they own about 14 percent of its shares and control 56 percent of the stockholder voting power through supervoting stock. They incorporated Google as a privately held company on September 4, 1998. An initial public offering (IPO) took place on August 19, 2004, and Google moved to its headquarters in Mountain View, California, nicknamed the Googleplex. In August 2015, Google announced plans to reorganize its various interests as a conglomerate called Alphabet Inc. Google is Alphabet's leading subsidiary and will continue to be the umbrella company for Alphabet's Internet interests. Sundar Pichai was appointed CEO of Google, replacing Larry Page who became the CEO of Alphabet. A chatbot is a software application used to conduct an on-line chat conversation via text or text-to-speech, in lieu of providing direct contact with a live human agent. Designed to convincingly simulate the way a human would behave as a conversational partner, chatbot systems typically require continuous tuning and testing, and many in production remain unable to adequately converse or pass the industry standard Turing test"
              }
            ]
        }
    ]
}
with open("input_file.json", "w") as outfile:
    json.dump(data,outfile)
    print("done")

exec(open("run_squad.py").read())
