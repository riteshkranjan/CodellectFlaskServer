__author__ = 'Ritesh_Ranjan'

class CodellectServerException(Exception):
    def __init__(self, value, message):
        self.value = value
        self.message = message
    def __init__(self, message):
            self.message = message
    def __str__(self):
        return repr(self.value)

#try:
#    raise CodellectServerException(2*2)
#    except CodellectServerException as e:
#   print 'CodellectServerException occurred, value:', e.value