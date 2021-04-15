from MatterSim import Simulator

class SimulatorWrapper(Simulator):

    def init(self):
        super(SimulatorWrapper, self).initialize()

    def newEpisode(self, scanId, viewpointId, heading, elevation):
        super(SimulatorWrapper, self).newEpisode([scanId], [viewpointId], [heading], [elevation])

    def getState(self, scanId, viewpointId, heading, elevation):
        return super(SimulatorWrapper, self).getState()[0]

    def makeAction(self, index, heading, elevation):
        super(SimulatorWrapper, self).makeAction([index], [heading], [elevation])
