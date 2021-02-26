# tp_ros_diksha
Ce package contient plusieurs noeuds qui sont un bouton, un publisher, un subscriber et un fichier launch.

Pour souscrire et publire, les codes se trouvent dans un seul noeud nommé publisher.py

Le but de ce projet est de manipuler le mouvement du PoseStamped et le faire bouger et arreter sur rviz en se servant d'un bouton

Pour lancer le projet, il suffit de lancer le launch file button.launch

# Installation
Pour installer ce package, il faut le cloner dans le dossier src de votre catkin workspace
```
cd catkin_ws/src
git clone https://github.com/diksha002/tp_ros_diksha.git
catkin build
cd ..
source devel/setup.bash
```
# Execution
Pour executer les noeuds:

## roscore
Ouvrez un terminal et lancer le roscore.

Dans un terminal, typez:
```
roscore
```

## roslaunch
Pour executer les noeuds, il faut lancer que le fichier launch

Ouvrez un terminal
```
cd catkin_ws
source devel/setup.bash
roslaunch tp_ros_diksha button.launch
```

Une petite fenetre avec un bouton toggle va apparaitre et aussi l'interface rviz sera lancé automatiquement

Cliquez sur le bouton toggle

## rviz
Sur rviz, ajoutez le topic nommé `chatter`
Vous devrez voir un PoseStamped qui suit le trajectoire d'un huit.

Quand le bouton est appuis initialement, l'état du topic est false, donc le PoseStamped reste immobile.

Pour que le PoseStamped fait le trajectoire de huit, il faut juste re-appuyer sur le bouton pour que l'état du topic devient true.

Chaque fois l'état du topic devient false, le PoseStamped s'arretera.

## Rostopic
Si vous voulez voir l'état du topic chaque fois vous appuyez sur le bouton, 

Ouvrez un terminal,
```
source devel/setup.bash
rostopic echo /button_state
```

