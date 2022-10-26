# Traffico

Traffico is a GUI app made using PyQt5 for showing road maintenance, conditions, and traffic related data.


## Table of Contents

1. [Dependencies](#dependencies)
1. [File Structure](#file-structure)
1. [Usage](#usage)
1. [How It Works](#how-it-works)


### Dependencies

- [PyQt5](#)
- [requests](#)


### File Structure

```
└──Data Calculation
    └───assets/
    │   └───icons/
    ├──.gitignore
    ├──app_controller.py
    ├──app_view.py
    ├──app_model.py
    ├──interface.py
    ├──interface.ui
    ├──resources_rc.py
    ├──resources.qrc
    └──README.md
```


### Usage

The following command will run the app and everything can be done using the GUI.

```bash
python app_controller.py
```


### How It Works

#### GUI

The GUI window is designed using the Qt Designer. The GUI is saved as `interface.ui` file. From the the *.ui file, `interface.py` file is generated using the following command:

```bash
pyuic5 -x interface.ui -o interface.py
```

Then, the `resources.qrc` file, which contains assets such as icons, is also converted to `resources_rc.py` file using:

```bash
pyrcc5 resources.qrc -o resources_rc.py
```

> The `pyuic5` and `pyrcc5` utilities come with the PyQt package.

The `interface.py` file contains all the GUI elements of the app.


#### MVC Design Pattern

The main logic of the app is built using the MVC (Model-View-Controller) design pattern. `app_model.py` has the Model class that fetch, parse and store the data obtained from the Digitraffic API. `app_view.py` has the View class which imports the GUI from the `interface.py` and responsible for setting up the UI. The user can only view and interact with View class. The View sends all signals (button presses, form input, etc.) to the Controller class of `app_controller.py` file. The Controller is responsible for performing logic on the data and maintaining the communication and control of the View and Model classes.
