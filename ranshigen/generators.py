import numpy
import xml.etree.ElementTree

def _hasChildren(element):
    return bool(len(element))

class GeneratorParser:

    referenceEvaluation = None

    def __init__(self, referenceEvaluation):
        self.referenceEvaluation = referenceEvaluation

    def parse(self, definitionString):
        return self._parseGenerator(xml.etree.ElementTree.fromstring(definitionString))

    def  _parseGenerator(self, element):
        if element.tag == 'random':
            return self._parseRandomGenerator(element)
        elif element.tag == 'reference':
            return self.referenceEvaluation(element.attrib['id'], self)

    def _parseRandomGenerator(self, element):
        values = []
        probabilities = []
        for child in element:
            if child.tag == 'item':
                item = self._parseItem(child)
                values.append(item['value'])
                if 'probability' in item:
                    probabilities.append(float(item['probability']))
                else:
                    probabilities.append(1)
        #Probabilities are normalized
        probabilities = [float(i)/sum(probabilities) for i in probabilities]
        return __RandomGenerator__(values, probabilities)

    def _parseItem(self, element):
        d = {}
        d.update(element.attrib)
        if _hasChildren(element):
            v = self._parseGenerator(element[0])
        else :
            v = element.text
        d['value'] = v
        return d

class __Generator__:
    def _evaluate_result(self, result):
        for x in range(0, result.size):
            if isinstance(result[x], __Generator__):
                result[x] = result[x].generate(1)[0];

    def generate(self, count):
        return None

class __RandomGenerator__(__Generator__):
    v = None
    p = None

    def __init__(self, values=None, probabilities=None):
        __Generator__.__init__(self)
        self.v = values
        self.p = probabilities

    def generate(self, count):
        result = numpy.random.choice(self.v, p=self.p, size=count)
        self._evaluate_result(result)
        return result
