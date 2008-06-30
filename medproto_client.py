#!/usr/bin/env python
#
# network.py: contact with server
# author: Wu Zhe <jessewoo at gmail.com>
# license: GPL

from twisted.internet.protocol import ReconnectingClientFactory
from twisted.protocols.basic import LineReceiver
from twisted.inetnet import reactor


class MedicalookClientProtocol(LineReceiver):

    def lineReceived(self, line):
        pass

    def connectionMade(self):
        print "server connected"

    def connectionLost(self, reason):
        print "connection lost"


class MedicalookClientFactory(ReconnectingClientFactory):
    def startedConnecting(self, connector):
        print 'Started to connect.'

    def buildProtocol(self, addr):
        print 'Connected.'
        print 'Resetting reconnection delay'
        self.resetDelay()
        return MedicalookClientProtocol()

    def clientConnectionLost(self, connector, reason):
        print 'Lost connection.  Reason:', reason
        ReconnectingClientFactory.clientConnectionLost(self,
                                                       connector,
                                                       reason)

    def clientConnectionFailed(self, connector, reason):
        print 'Connection failed. Reason:', reason
        ReconnectingClientFactory.clientConnectionFailed(self,
                                                         connector,
                                                         reason)
