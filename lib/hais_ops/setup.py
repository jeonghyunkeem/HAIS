import os
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

os.environ["TORCH_CUDA_ARCH_LIST"] = "3.7+PTX;5.0;6.0;6.1;6.2;7.0;7.5"
setup(
    name='HAIS_OP',
    ext_modules=[
        CUDAExtension('HAIS_OP', [
            'src/hais_ops_api.cpp',

            'src/hais_ops.cpp',
            'src/cuda.cu'
        ], extra_compile_args={'cxx': ['-g'], 'nvcc': ['-O3']})
    ],
    cmdclass={'build_ext': BuildExtension}
)