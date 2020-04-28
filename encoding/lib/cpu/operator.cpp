#include "operator.h"

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
  m.def("batchnorm_forward", &BatchNorm_Forward_CPU, "BatchNorm forward (CPU)");
  m.def("batchnorm_backward", &BatchNorm_Backward_CPU, "BatchNorm backward (CPU)");
}
