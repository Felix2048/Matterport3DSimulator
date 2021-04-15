git submodule update --init --recursive 
sudo apt install libjsoncpp-dev libepoxy-dev libglm-dev libosmesa6 libosmesa6-dev libglew-dev
sudo apt install libgl1-mesa-dev libegl*
mkdir build && cd build
cmake -DEGL_RENDERING=ON ..
make -j12
