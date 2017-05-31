from structures.basenum import BaseNum
from prngs.prng import PRNG
from utils.constants import Constants

class RC4(PRNG):
  def __init__(self, seed):
    super(RC4, self).__init__(seed)
    self.key = self._RC4__key_scheduling()
    self.i = self.j = 0

  # @return [Array<Integer>] The result of the RC4 key-scheduling algorithm
  def __key_scheduling(self):
    key = range(Constants.MAX_BYTE)
    shuffle = 0
    for index in xrange(Constants.MAX_BYTE):
      byte = self.seed.get_byte(index % max(1, self.seed.bytes())).to_integer()
      shuffle = (shuffle + key[index] + byte) % Constants.MAX_BYTE
      key[index], key[shuffle] = key[shuffle], key[index]
    return key

  # @param bits [Integer] The number of bits to return.
  # @return [BaseNum] The next n-bits of RC4's output for the given seed.
  def generate_output(self, bits):
    result = self.seed.__class__('')
    while len(result.bits()) < bits:
      self.i = (self.i + 1) % Constants.MAX_BYTE
      self.j = (self.j + self.key[self.i]) % Constants.MAX_BYTE
      self.key[self.i], self.key[self.j] = self.key[self.j], self.key[self.i]
      index = (self.key[self.i] + self.key[self.j]) % Constants.MAX_BYTE
      byte = self.seed.__class__.from_integer(self.key[index])
      result = result.append(byte.pad(byte.byte_length()))
    self.bits += bits
    return result
