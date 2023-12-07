import subprocess


def add_client(filename, filename2, number_of_clients):
    file = open(filename, "a")
    file.write('version: "3"\n')
    file.write('services: \n')
   
    for i in range(0, number_of_clients):
        file.write('  vlc-client-' + str(i) + ':\n')
        file.write('    image: quay.io/galexrt/vlc:latest\n')
        file.write('    environment:\n')
        file.write('      - DISPLAY=$DISPLAY\n')
        file.write('      - PULSE_SERVER=unix:/run/user/1000/pulse/native\n')
        file.write('    volumes:\n')
        file.write('      - /tmp/.X11-unix:/tmp/.X11-unix\n')
        file.write('      - /run/user/1000/pulse:/run/user/1000/pulse\n')
        file.write('    ports:\n')
        file.write('      - "' + str(4568 + i) + ':8080"\n')

    file2 = open(filename2, "a")
    file2.write("#!/bin/bash\n")
    for i in range(0, number_of_clients):
        file2.write(f'docker exec $CONTAINERS_DIR-vlc-client-{i}-1 cvlc http://$SERVER_IP:8080/stream & \n')


add_client(filename="docker-compose.yml", filename2="run_cvlc", number_of_clients=40)
