# Parent class that all dataset classes must follow. Forces dataset classes to have a load() function, similar to ModelConfig.

class BaseDataset:
  def load(self):
    raise NotImplementedError
