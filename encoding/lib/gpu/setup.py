from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name='enclib_gpu',
    ext_modules=[
        CUDAExtension('enclib_gpu', [
            'operator.cpp',
            'activation_kernel.cu',
            'syncbn_kernel.cu',
            ],
            extra_compile_args={'cxx':['-g'] ,'nvcc': ['--extended-lambda']}
            ),
    ],
    cmdclass={
        'build_ext': BuildExtension
    })
