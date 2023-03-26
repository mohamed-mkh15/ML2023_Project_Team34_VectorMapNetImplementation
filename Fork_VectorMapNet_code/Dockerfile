FROM nvidia/cuda:11.6.2-base-ubuntu20.04

ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"
RUN apt-get update

RUN apt-get install -y wget unzip git gcc && rm -rf /var/lib/apt/lists/*

RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-py38_23.1.0-1-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-py38_23.1.0-1-Linux-x86_64.sh -b \
    && rm -f Miniconda3-py38_23.1.0-1-Linux-x86_64.sh \
    RUN conda --version
# RUN wget \
#     https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
#     && mkdir /root/.conda \
#     && bash Miniconda3-latest-Linux-x86_64.sh -b \
#     && rm -f Miniconda3-latest-Linux-x86_64.sh \
# RUN conda --version

# RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py38_23.1.0-1-Linux-x86_64.sh
# RUN bash Miniconda3-py38_23.1.0-1-Linux-x86_64.sh -y
# RUN conda create --name hdmap-opensource python==3.8  
#    && conda init bash \

#RUN conda run -n hdmap-opensource     
# RUN bash -c "source ${HOME}/.bashrc" 
#SHELL ["conda", "run", "-n", "hdmap-opensource", "/bin/bash", "-c"]  

RUN mkdir hdmv
ADD configs hdmv/configs
ADD plugin hdmv/plugin
ADD tools hdmv/tools
COPY requirements.txt hdmv
COPY vectormapnet.pth hdmv
COPY entrypoint.sh hdmv
#ENTRYPOINT [ "hdmv/entrypoint.sh" ]
# Activate the environment, and make sure it's activated:
# RUN conda init --all 

# SHELL ["/bin/bash", "--login", "-c"]
# SHELL ["bash", "-lc"]
# RUN echo "conda activate hdmap-opensource" > ~/.bashrc  

# RUN conda activate hdmap-opensource
# RUN export CUDA_HOME=/usr/local/cuda

RUN pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 -f https://download.pytorch.org/whl/torch_stable.html 
#    -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN pip install mmcv-full==1.3.9 -f https://download.openmmlab.com/mmcv/dist/cu111/torch1.9.0/index.html \
    && pip install mmdet==2.14.0 \
    && pip install mmsegmentation==0.14.0 \
    && pip install --upgrade setuptools

ENV CUDA_HOME='/usr/local/cuda-11'
ENV CUDA_TOOLKIT_ROOT_DIR=$CUDA_HOME
ENV FORCE_CUDA="1"
ENV LD_LIBRARY_PATH="$CUDA_HOME/extras/CUPTI/lib64:$LD_LIBRARY_PATH"
ENV LIBRARY_PATH=$CUDA_HOME/lib64:$LIBRARY_PATH
ENV LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH
ENV CFLAGS="-I$CUDA_HOME/include $CFLAGS"

RUN wget https://github.com/open-mmlab/mmdetection3d/archive/refs/tags/v0.17.3.zip \ 
    && ls && unzip v0.17.3.zip && ls && cd mmdetection3d-0.17.3 \ 
    && pip install -v -e .


RUN pip install -r hdmv/requirements.txt
