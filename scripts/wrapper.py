from MatterSim import Simulator 

class SimulatorWrapper(Simulator):

    def init(self):
        super(Simulator, self).initialize()

    def newEpisode(self, scanId, viewpointId, heading, elevation):
        super(Simulator, self).newEpisode([scanId], [viewpointId], [heading], [elevation])

    def getState(self, scanId, viewpointId, heading, elevation):
        return super(Simulator, self).getState()[0]

    def makeAction(self, index, heading, elevation):
        super(Simulator, self).makeAction([index], [heading], [elevation])