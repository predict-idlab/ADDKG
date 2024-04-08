## Track 2

Within each round folder, you will find a detector, monitor, and replayer folder containing all necessary code to create a streaming knowledge graph environment.

Inside the replayer folder, the functionality of replay.py can be customized to suit your requirements. You can:

* Load different data segments based on regions where anomalies occur.
* Adjust the time between knowledge graph events to expedite local evaluations.

Please note that the challenge organizers will use the default replayer functionality to score the different systems.

Two Docker Compose YAML files are also provided:

* A full-application file that can build and run the detector, monitor, replayer, and Kafka altogether.
* A simpler Docker Compose file that only utilizes the Kafka functionality for local development. Running this Docker Compose file enables participants to initiate the replayer, monitor, and detector as individual Python runs, for debugging purposes outside the Docker environment.

Participants can expand upon or create a new detector using the code within the detector folder. Participants are permitted to use languages other than Python for their detectors. For additional assistance, please contact the challenge organizers through Slack.
