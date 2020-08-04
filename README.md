<h1>Prediction of Youtube Video Type using the Naive Bayes Algorithm</h1>

<p>Youtube provides several video types. It is effortless to predict Youtube video types based on the training data of youtube.</p>

<h2>How to build?</h2>

<p> docker build -t predictheartdisease:latest .</p>

<h2>How to Run?</h2>

<p>
docker run -d -p 5000:5000 predictheartdisease



</p>

<h2>How to use?</h2>

<p>
Post:</br>
http://hostip:5000/api/v1/predict

</p>
<p>

<br/>
Body request: </br>

{
    "data":["Barking dog plays with toy",
        "Best fashion looks for Spring 2018",
        "Olympics opening ceremony highlights",
        "Warriors basketball game versus the cavs",
        "CNN world news on donald trump",
        "Police Chase in Hollywood",
        "Ed Sheeran - Perfect (Official Music Video)",
        "how to do eyeshadow",
        "How To Become A Data Scientist In India (in 2020)",
        "Germany High Speed Train 2020 | ICE Train Berlin Nuremberg",
        "Agar Tum Saath Ho",
        "A squirrel begged a man to help her baby, who was in trouble",
        "Why Religious Beliefs Aren't Just Silly",
        "Dr. Gulati Trips On The Stage | The Kapil Sharma Show | SET India Rewind"
         ]
}

</P>

<h2>Example of prediction output</h2>

<p>

[
    {
        "Predicted Video Type": "Entertainment",
        "Video Title": "Barking dog plays with toy"
    },
    {
        "Predicted Video Type": "People & Blogs",
        "Video Title": "Best fashion looks for Spring 2018"
    },
    {
        "Predicted Video Type": "Sports",
        "Video Title": "Olympics opening ceremony highlights"
    },
    {
        "Predicted Video Type": "Sports",
        "Video Title": "Warriors basketball game versus the cavs"
    },
    {
        "Predicted Video Type": "News & Politics",
        "Video Title": "CNN world news on donald trump"
    },
    {
        "Predicted Video Type": "News & Politics",
        "Video Title": "Police Chase in Hollywood"
    },
    {
        "Predicted Video Type": "Music",
        "Video Title": "Ed Sheeran - Perfect (Official Music Video)"
    },
    {
        "Predicted Video Type": "Howto & Style",
        "Video Title": "how to do eyeshadow"
    },
    {
        "Predicted Video Type": "Education",
        "Video Title": "How To Become A Data Scientist In India (in 2020)"
    },
    {
        "Predicted Video Type": "News & Politics",
        "Video Title": "Germany High Speed Train 2020 | ICE Train Berlin Nuremberg"
    },
    {
        "Predicted Video Type": "Music",
        "Video Title": "Agar Tum Saath Ho"
    },
    {
        "Predicted Video Type": "Entertainment",
        "Video Title": "A squirrel begged a man to help her baby, who was in trouble"
    },
    {
        "Predicted Video Type": "Education",
        "Video Title": "Why Religious Beliefs Aren't Just Silly"
    },
    {
        "Predicted Video Type": "Entertainment",
        "Video Title": "Dr. Gulati Trips On The Stage | The Kapil Sharma Show | SET India Rewind"
    }
]

</p>
