# [ISWC 2024](https://iswc2024.semanticweb.org/) Challenge:</br> Anomaly Detection on Dynamic Knowledge Graphs

[![slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)](https://join.slack.com/t/addkgiswcchallenge/shared_invite/zt-2f4pbtfmu-1SyIPzVnRBNeeXFpSgIysA) [Join our Slack channel for more updates!](https://join.slack.com/t/addkgiswcchallenge/shared_invite/zt-2f4pbtfmu-1SyIPzVnRBNeeXFpSgIysA)



## Dynamic Knowledge Graphs: Unveiling the Evolution of Knowledge

Dynamic knowledge graphs (DKGs) are increasingly recognized for their ability to depict the ever-changing nature of knowledge over time. Harnessing the power to capture topological transformations, DKGs offer invaluable insights into the evolution of knowledge across various domains such as open KGs, social media dynamics, industrial advancements (Industry 4.0), and healthcare innovations. Despite their versatility and advantages, the absence of comprehensive benchmark datasets hinders the evaluation of machine learning techniques utilizing DKGs.

## The data
Within the Data folder in this reposity, you will find DKGs seperated by timestamp. Each graph is represented in ttl format and the UTC timestamp of the graph is provided in the filename. They are placed in different folders per day to make this clear. Each KG can be represented as a set of triples where subject and object nodes are linked to eachother using a relationship. If this new for you, more information about the ttl or turtle format can be found [here](https://www.youtube.com/watch?v=PADwVsHA7H0&ab_channel=OpenHPITutorials).

### Origin of data
This data was constructed from a e-commerce microservice platform. In a microservice cluster, different services work together to achieve the best possible way to adapt different software components to new unkown behaviour. 


## <img src="https://eval.ai/dist/images/evalai-logo-single.png" alt="Track 1" width="25"/> [Track 1](https://eval.ai/web/challenges/challenge-page/2267/overview)
The goal of this track is to predict occuring anomalies within an unseen test set. The data can be found in the Track 1 folder. For each round, both the knowledge graphs, a label.csv file and an example submission can be found.</br>
Submissions can be made using the [challenge eval.ai platform](https://eval.ai/web/challenges/challenge-page/2267/overview)
### Round 1
In this round, training labels for 3 days are provided within this repository. The goal is to make predictions for the last two days within this dataset. Evaluation criterea can be found at the evalai competition platform, which will host this challenge.

### Round 2
To be announced

## Track 2
The objective of Track 2 is to identify anomalies promptly as they emerge. In the realm of dynamic knowledge graphs, new graphs are continuously generated over time. For each graph, a detector is tasked with assessing whether it exhibits anomalous behavior. Your challenge in this track is to create detectors capable of analyzing incoming graphs and detecting anomalies at each timestamp. </br>
</br>
To do this, we provide participants with a full system to replay dynamic graphs. The code can be found within the Track 2 folder.
Our system exists out of 3 components:
    * A replayer, which is responsible for replay a dynamic graphs dataset
    * A detector, anamoly detection module
    * A montior, which is responbsile for scoring the detector against the ground truth labels

The whole system is based upon Kafka to send and receive messages. By doing this, the replayer functionality produces knowledge graph events at defined time intervals. The detector can listen or consume these knowledge graphs and produces new events based on the detectors' outcome (anomalous or not). The monitor consumes then these anomaly messages and compares them against the ground truth (a real operator or a predefined ground truth set). The monitor outputs the true positive, true negative and average time till detection</br>

To make sure everything works harmoniously together, all components are provided in Docker containers and a docker-compose.yaml file is available to automate all necessary building steps.

**While we have implemented the replayer and monitor, the goal for the participants is to create a detector Docker container.**
They can either extend the provided detector with new functionality or create a new one based on the provided template.

We would like to ask the participants to host their detector containers in a public repository (e.g., using Docker Hub) and send us this link through the provided Google submission forms. Evaluation against a hidden replay dataset for each round will be performed after the defined submission dates.

### Round 1
Submission can be made using [this form](https://forms.gle/sQDAZAzNdRZBt4SXA)

### Round 2
To be announced



