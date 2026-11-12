from Basilisk.utilities import SimulationBaseClass
from TestModule import TestPythonModule
from Basilisk.utilities import macros


def run():
    """
    Illustration of Basilisk process and task creation
    """

    #  Create a sim module as an empty container
    scSim = SimulationBaseClass.SimBaseClass()

    #  create the simulation process
    dynProcess = scSim.CreateNewProcess("dynamicsProcess")
    fswProcess = scSim.CreateNewProcess("fswProcess")

    # create the dynamics task and specify the integration update time
    dynProcess.addTask(scSim.CreateNewTask("dynamicsTask", macros.sec2nano(5.)))
    dynProcess.addTask(scSim.CreateNewTask("sensorTask", macros.sec2nano(10.)))
    fswProcess.addTask(scSim.CreateNewTask("fswTask", macros.sec2nano(10.)))

    mod4 = TestPythonModule()
    mod4.ModelTag = "pythonModule4"
    scSim.AddModelToTask("dynamicsTask", mod4, 10)

    #  initialize Simulation:
    scSim.InitializeSimulation()

    #   configure a simulation stop time and execute the simulation run
    scSim.ConfigureStopTime(macros.sec2nano(200.0))
    scSim.ExecuteSimulation()

    return


if __name__ == "__main__":
    run()