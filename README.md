# Assignment 2 of Programming in Python

The task in this assignment is to develop a simulation involving a wolf that tries to catch sheep scattered in a meadow, which uses text mode.

The simulation involves two animal species: a single wolf and a herd of sheep. These animals move around an infinite meadow with no terrain obstacles: the wolf chases the sheep, trying to catch them and then eat them, while the sheep try (rather clumsily) to escape from the wolf. According to these stipulations, the meadow is represented as an infinite two-dimensional space with the center located at the point (0.0; 0.0), thus using a Cartesian coordinate system, whereas the position of each animal in the meadow is defined as a pair of floating-point numbers (the coordinates can take on both positive and negative values).

At the beginning of the simulation, the initial positions of all animals are determined. The initial position of each sheep is chosen randomly, with each coordinate being drawn from a range that extends symmetrically around 0 over positive and negative numbers, and where chosen values are floating-point numbers, which need not be whole. Given that the range is symmetrical around 0, its specification is governed by a single predefined value that is the absolute value of the limit imposed on the coordinates (hence the range spans from the negative of this value to this value). The initial position of the wolf is the center of the meadow, that is the point (0.0; 0.0).

The simulation is advanced in rounds. In the first stage of every round, all alive sheep move one by one, and afterwards, in the second stage, the wolf moves. During its movement, a sheep first randomly chooses one of the four directions: north (up), south (down), east (right), or west (left), and then moves a predefined distance in the chosen direction. In turn, the wolf first determines which sheep is closest to it in terms of the Euclidean distance, and subsequently checks whether this sheep is within the range of its attack, that is whether the Euclidean distance to the sheep is not greater than the distance that the wolf moves when chasing a sheep; if this is the case, the wolf eats the sheep, which means that the sheep disappears and the wolf takes its position, whereas if this is not the case, the wolf starts chasing the sheep, moving a predefined distance towards it (if there are more than one sheep within the same closest distance, the wolf takes its actions with respect only to the first one). The simulation ends either when all sheep have been eaten or when a predefined maximum number of rounds has been reached.

Requirements for the maximum grade of 4

1.  Implement a simulation as described above. The code should be written in object-oriented manner and should comprise at least two classes: one encapsulating the behavior of a single sheep and the other encapsulating the behavior of the wolf. Create other classes as needed. Adopt the following values:
    -   the maximum number of rounds: 50;
    -   the number of sheep: 15;
    -   the absolute value of the limit imposed on each coordinate of the initial positions of sheep: 10.0 (which implies that the respective range is [-10.0; 10.0]);
    -   the distance of sheep movement: 0.5;
    -   the distance of wolf movement: 1.0.To generate random numbers, use the *random* module from the standard library. If more advanced mathematical calculations are necessary, use the *math* module from the standard library.
2.  Implement displaying basic information about the status of the simulation at the end of each round. The information should include:
    -   the round number;
    -   the position of the wolf (to the third decimal place of each coordinate);
    -   the number of alive sheep;
    -   if the wolf is chasing a sheep - a statement of this fact along with an indication which sheep is being chased (its sequence number);
    -   if a sheep was eaten - a statement of this fact along with an indication which sheep it was (its sequence number).Displaying the above information should not pause the simulation as no interaction with the user is necessary.
3.  Using the *json* package from the standard library, implement saving the position of every animal at the end of each round to a `pos.json` file. The file should contain a list of dictionaries, each of which should correspond to an individual round and comprise the following elements:
    -   `'round_no'` - the round number (an integer);
    -   `'wolf_pos'` - the position of the wolf (a pair of floating-point numbers);
    -   `'sheep_pos'` - the positions of all sheep (a list containing as many elements as the number of sheep, with each element being either a pair of floating-point numbers in the case of an alive sheep or the `null` value, obtained owing to an automatic conversion from the `None` value, in the case of a sheep that has been eaten).It is desirable for the content of the file to be nicely formatted, that is divided into successive lines that are appropriately indented. If a `pos.json` file already exists, it should be overwritten.
4.  Using the *csv* module from the standard library, implement saving the number of alive sheep at the end of each round to an `alive.csv` file. The file should contain two columns storing the following values:
    1.  the round number (an integer);
    2.  the number of alive sheep (an integer).Each row in the file should correspond to an individual round. If an `alive.csv` file already exists, it should be overwritten.

Requirements for the maximum grade of 5

1.  All requirements for the maximum grade of 4 should be satisfied.
2.  Using the *argparse* module from the standard library, implement handling the following command-line arguments:
    -   `-c/--config FILE` - an auxiliary configuration file, where `FILE` stands for a filename;
    -   `-h/--help` - showing the program help message;
    -   `-l/--log LEVEL` - recording events to a log, where `LEVEL` stands for a log level (*DEBUG*, *INFO*, *WARNING*, *ERROR*, or *CRITICAL*);
    -   `-r/--rounds NUM` - the maximum number of rounds, where `NUM` denotes an integer;
    -   `-s/--sheep NUM` - the number of sheep, where `NUM` denotes an integer;
    -   `-w/--wait` - introducing a pause after displaying basic information about the status of the simulation at the end of each round until a key is pressed.All command-line arguments should be optional and should adhere to the following specification.
    -   The option `-c/--config` specifies a configuration file in which an absolute value of the limit imposed on each coordinate of the initial positions of sheep, a distance of sheep movement, and a distance of wolf movement are defined. The format of the configuration file is described below. If this option is not supplied, the default values (provided in the requirements for the maximum grade of 4) should be used.
    -   The option `-h/--help` results in displaying the program help message, which includes a brief program description and information about its parameters. If this option is supplied, the program should terminate after displaying the help message and the simulation should not be performed.
    -   The option `-l/--log` specifies a log level that determines which events should be recorded to a log. If this option is supplied, a `chase.log` file should be created in the current directory and relevant events during program execution should be logged to this file. If a `chase.log` file already exists, it should be overwritten. If this option is not supplied, a `chase.log` file should not be created and no events should be logged.
    -   The option `-r/--rounds` specifies the maximum number of rounds. If this option is not supplied, the default value (provided in the requirements for the maximum grade of 4) should be used.
    -   The option `-s/--sheep` specifies the number of sheep. If this option is not supplied, the default value (provided in the requirements for the maximum grade of 4) should be used.
    -   The option `-w/--wait` specifies that after displaying basic information about the status of the simulation at the end of each round, the simulation should be paused until the user presses any key. If this option is not supplied, the simulation should not be paused at the end of each round and should continue uninterrupted (as described in the requirements for the maximum grade of 4).All arguments should be properly validated (e.g., the maximum number of rounds must be an integer greater than zero). In case of validation failure, an error should be reported through raising an appropriate exception.
3.  Using the *configparser* module from the standard library, implement loading an absolute value of the limit imposed on each coordinate of the initial positions of sheep, a distance of sheep movement, and a distance of wolf movement from a configuration file whose name is specified as part of the `-c/--config` command-line argument. The configuration file should be an INI file with the following structure (the actual values below correspond to the default values, provided in the requirements for the maximum grade of 4):

    [Sheep]
    InitPosLimit = 10.0
    MoveDist = 0.5

    [Wolf]
    MoveDist = 1.0

    All values should be properly validated (e.g., the distance of wolf movement must be a positive number). In case of validation failure, an error should be reported through raising an appropriate exception.
4.  Using the *logging* package from the standard library, implement logging events to a `chase.log` file. Events should be logged depending on the log level specified as part of the `-l/--log` command-line argument. The following log levels are defined:
    -   *DEBUG* (10) - provides detailed information intended for a developer typically to help diagnose a problem;
    -   *INFO* (20) - provides general information about the progress of program execution;
    -   *WARNING* (30) - indicates that something unexpected happened, yet the program is working as expected;
    -   *ERROR* (40) - indicates that a problem occurred and the program may not be able to perform some of its functions;
    -   *CRITICAL* (50) - indicates that a serious problem occurred and the program may not be able to continue running.Events whose severity level is equal to or higher than the specified log level should be logged according to the following specification.
    -   The *DEBUG* (10) level requires the following events to be logged with the corresponding information:

    -   when values from a configuration file were loaded - a statement of this fact along with the actual loaded values;
    -   when an initial position of a sheep was determined - the sequence number of the sheep and the initial position of the sheep;
    -   when an alive sheep randomly chose a direction of movement - the sequence number of the sheep and the chosen direction;
    -   when an alive sheep moved - the sequence number of the sheep and the new position of the sheep;
    -   when the wolf determined which sheep is closest to it - the sequence number of the sheep and the distance to the sheep;
    -   when the wolf moved - the new position of the wolf;
    -   when information were saved to a `pos.json` file - a statement of this fact;
    -   when information were saved to an `alive.csv` file - a statement of this fact.

    -   The *INFO* (20) level requires the following events to be logged with the corresponding information:

    -   when initial positions of all sheep were determined - a statement of this fact;
    -   when a new round was started - a statement of this fact along with the round number;
    -   when all alive sheep moved - a statement of this fact;
    -   when the wolf is chasing a sheep - a statement of this fact along with the sequence number of the sheep;
    -   when the wolf moved - a statement of this fact;
    -   when a sheep was eaten - a statement of this fact along with the sequence number of the sheep;
    -   when a round is about to end - the number of alive sheep (i.e., at the end of the round);
    -   when the simulation terminated - a statement of this fact along with the cause (either all sheep have been eaten or the predefined maximum number of rounds has been reached).

    -   The exact events to be logged and the corresponding information at the *WARNING* (30), *ERROR* (40), and *CRITICAL(50)* levels depend on how the program is implemented and should be chosen accordingly; if no events seem appropriate for logging at a particular level, it is not required to log anything at that level.