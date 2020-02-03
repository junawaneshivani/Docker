### Create your first swarm
In this section, you will create your first swarm by using [Play-with-Docker](https://labs.play-with-docker.com/).

Navigate to Play-with-Docker. You're going to create a swarm with three nodes.

Click Add new instance on the left side three times to create three nodes.
```
Initialize the swarm on node 1:
$ docker swarm init --advertise-addr eth0
Swarm initialized: current node (vq7xx5j4dpe04rgwwm5ur63ce) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join \
    --token SWMTKN-1-50qba7hmo5exuapkmrj6jki8knfvinceo68xjmh322y7c8f0pj-87mjqjho30uue43oqbhhthjui \
    10.0.120.3:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
```
You can think of Docker Swarm as a special mode that is activated by the command: `docker swarm init`. The `--advertise-addr` option specifies the address in which the other nodes will use to join the swarm.

This docker swarm init command generates a join token. The token makes sure that no malicious nodes join the swarm. You need to use this token to join the other nodes to the swarm. For convenience, the output includes the full command docker swarm join, which you can just copy/paste to the other nodes.

On both node2 and node3, copy and run the docker swarm join command that was outputted to your console by the last command.
You now have a three-node swarm!

Back on node1, run docker node ls to verify your three-node cluster:
```
$ docker node ls
ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS
7x9s8baa79l29zdsx95i1tfjp     node3               Ready               Active
x223z25t7y7o4np3uq45d49br     node2               Ready               Active
zdqbsoxa6x1bubg3jyjdmrnrn *   node1               Ready               Active              Leader
```
This command outputs the three nodes in your swarm. The asterisk (*) next to the ID of the node represents the node that handled that specific command (docker node ls in this case).

Your node consists of one manager node and two workers nodes. Managers handle commands and manage the state of the swarm. Workers cannot handle commands and are simply used to run containers at scale. By default, managers are also used to run containers.
