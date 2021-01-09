# lazera Minecraft Server
Minecraft server support telegram bot as notification and gmail, so if some stranger join your server? it automate for send notification using telegram and gmail

### [ Preparation ] setup docker as container
- you can googling about docker installation guide, after installed :
use [nimmis/spigot](https://hub.docker.com/r/nimmis/spigot) as image we used for

```shell
docker pull nimmis/spigot
```
- build docker container from that image
```shell
docker run --name lazera -e EULA=true  -e SPIGOT_VER=1.16.2 -e MC_MAXMEM=3.75g -e MC_MINMEM=2g -e SPIGOT_AUTORESTART=yes -v ~/minecraft/DATA:/minecraft -d -p 25565:25565 -p 25575:25575 -p 8123:8123 nimmis/spigot 
```
- you can follow the output from the compilation with then command (assume that you given the container the name spigot)

```shell
docker logs -f spigot
*** open logfile
*** Run files in /etc/my_runonce/
*** Running /etc/my_runonce/set_timezone...
*** Run files in /etc/my_runalways/
*** Running /etc/my_runalways/do_build_spigot...
--2016-12-04 13:17:37--  https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar
Resolving hub.spigotmc.org (hub.spigotmc.org)... 104.27.195.96, 104.27.194.96, 2400:cb00:2048:1::681b:c360, ...
Connecting to hub.spigotmc.org (hub.spigotmc.org)|104.27.195.96|:443... connected.
HTTP request sent, awaiting response... 200 OK
```

Then the compilation is completed the server will start and you will see something like :

```shell
*** Log: Success! Everything compiled successfully. Copying final .jar files now.
*** Log: Copying craftbukkit-1.11-R0.1-SNAPSHOT.jar to /minecraft/build/.
*** Log:   - Saved as craftbukkit-1.11.jar
*** Log: Copying spigot-1.11-R0.1-SNAPSHOT.jar to /minecraft/build/.
*** Log:   - Saved as spigot-1.11.jar
*** Running /etc/my_runalways/eula...
*** Running /etc/rc.local...
*** Booting supervisor daemon...
*** Supervisor started as PID 4820
*** Started processes via Supervisor......
crond                            RUNNING    pid 4824, uptime 0:00:03
spigot                           RUNNING    pid 4825, uptime 0:00:03
syslog-ng                        RUNNING    pid 4823, uptime 0:00:03
```
you can then exit from the log with CTRL-C

- after compilation was completed, you can watch runing process by hit this command
```shell
docker exec spigot mc_log
```
- and you will see the last 10 lines from the output, this is what you will see after startup
```shell
Abort with CTRL-C
[13:02:15 INFO]: Zombie Aggressive Towards Villager: true
[13:02:15 INFO]: Experience Merge Radius: 3.0
[13:02:15 INFO]: Preparing start region for level 0 (Seed: 506255305130990210)
[13:02:16 INFO]: Preparing spawn area: 22%
[13:02:17 INFO]: Preparing spawn area: 99%
[13:02:17 INFO]: Preparing start region for level 1 (Seed: 506255305130990210)
[13:02:18 INFO]: Preparing spawn area: 95%
[13:02:18 INFO]: Preparing start region for level 2 (Seed: 506255305130990210)
[13:02:18 INFO]: Server permissions file permissions.yml is empty, ignoring it
[13:02:18 INFO]: Done (3.650s)! For help, type "help" or "?"
```
It will continue to output everything from the console until you press CTRL-C

#### you can start to install all plugins by refering volume drive (-v ~/minecraft/DATA)
```shell
cd ~/minecraft/DATA
```
and you will see the minecraft directory :
```shell
README.md            bukkit.yml    help.yml   ops.json         plugins            spigot-1.16.2.jar  start.sh    usercache.json  world_nether
banned-ips.json      commands.yml  input.con  output.con       server-icon.png    spigot.jar         trunks      whitelist.json  world_the_end
banned-players.json  eula.txt      logs       permissions.yml  server.properties  spigot.yml         trunks_form world
```

#### dont forget to open and firewalling port
- 25565 for minecraft connection
- 25575 if you using RCON
- 8123 if you planning to use maps feature like DynMaps

### [ Preparation ] setup telegram bot and gmail mailer




## Thanks To :
- [nimmis](https://github.com/nimmis/docker-spigot)
