# ISWC Challenge: Anomaly Detection on Dynamic Knowledge Graphs

[![slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)](https://join.slack.com/t/addkgiswcchallenge/shared_invite/zt-2f4pbtfmu-1SyIPzVnRBNeeXFpSgIysA)



## Dynamic Knowledge Graphs: Unveiling the Evolution of Knowledge

Dynamic knowledge graphs (DKGs) are increasingly recognized for their ability to depict the ever-changing nature of knowledge over time. Harnessing the power to capture topological transformations, DKGs offer invaluable insights into the evolution of knowledge across various domains such as open KGs, social media dynamics, industrial advancements (Industry 4.0), and healthcare innovations. Despite their versatility and advantages, the absence of comprehensive benchmark datasets hinders the evaluation of machine learning techniques utilizing DKGs.

## The data
Within the Data folder in this reposity, you will find DKGs seperated by timestamp. Each graph is represented in ttl format and the UTC timestamp of the graph is provided in the filename. They are placed in different folders per day to make this clear. Each KG can be represented as a set of triples where subject and object nodes are linked to eachother using a relationship. If this new for you, more information about the ttl or turtle format can be found [here](https://www.youtube.com/watch?v=PADwVsHA7H0&ab_channel=OpenHPITutorials).

### Origin of data
This data was constructed from a e-commerce microservice platform. In a microservice cluster, different services work together to achieve the best possible way to adapt different software components to new unkown behaviour. 

## Track 1
The goal of this track is to predict occuring anomalies within an unseen test set. The data can be found in the Track 1 folder. For each round, both the knowledge graphs, a label.csv file and an example submission can be found.
### Round 1
In this round, training labels for 3 days are provided within this repository. The goal is to make predictions for the last two days within this dataset. Evaluation criterea can be found at the evalai competition platform, which will host this challenge.