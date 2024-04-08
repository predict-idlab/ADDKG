## Track 2

Within each round folder, you will find a detector, monitor and replay folder containing all necessary code to create a streaming knowledge graph environment. 

Within the replayer folder, the replay.py functionality can be adapted to your needs.
You can:
* Load different data segments based on regions where anomalies do occur
* Change the time between knowledge graph events, to speed up local evaluations.

Do take into account that the challenge organizers will us the default replayer functionality to score the different systems.</br>

Two docker compose yaml files are also made available:
* a full-application file, that can build and run the detector, monitor and replayer + kafka in one 
* a simpler docker compose file, that only exploits the kafka functionality for local development. Running this docker compose file enables participants to start the replayer, monitor and detector as individual python runs, for debugging purposes outisde the docker environment.

Participants can extend or create a new detector based on the code within the detector folder. Participants are allowed to use other languages than Python to create their detectors. Please contact the challenge organizers through slack if you need additional assitance.
