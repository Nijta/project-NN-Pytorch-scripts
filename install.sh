conda_url=https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
venv_dir=$PWD/venv

echo 'Making python virtual environment'
name=$(basename $conda_url)

if [ ! -f $name ]; then
  wget $conda_url || exit 1
fi

sh $name -b -p $venv_dir || exit 1
. $venv_dir/bin/activate

conda env create -f env.yml
conda activate pytorch-1.6

