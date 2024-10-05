

docker.run:
	docker run -it --name tty-container ubuntu /bin/bash

docker.container:
	docker run --name finsight-app fisnight-image:v1.0 /bin/bash -c "echo 'Hello World'; sleep infinity"