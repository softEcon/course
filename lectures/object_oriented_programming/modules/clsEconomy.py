""" This module contains the class representation of economy.
"""

__all__ = ['EconomyCls']
# This restricts the imported names to the EconomyCls when
# -- from package import * -- is encountered.

# standard library
import numpy as np

# external function in an external file.
from _checks import integrity_checks


class EconomyCls(object):

    def __init__(self, agent_objs):
        """ Initialize instance of economy class and attach the agent
            population as a class attribute.
        """
        # Antibugging
        integrity_checks('__init__', agent_objs)

        # Attach initialization attributes
        self.population = agent_objs

    ''' Public Methods'''

    def get_aggregate_demand(self, p1, p2):
        """ Aggregate demand of the individual agents to the overall demand
            for each good in the economy.
        """

        raise NotImplementedError('Not implemented ...')