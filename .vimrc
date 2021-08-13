syntax on

set tabstop=2

set shiftwidth=2

set expandtab

set ai

set number

set hlsearch

set ruler

colorscheme peachpuff

highlight Comment ctermfg=green



call plug#begin('~/.vim/plugged')
Plug 'https:///github.com/jiangmiao/auto-pairs.git'
Plug 'preservim/nerdcommenter'
Plug 'vimwiki/vimwiki'
Plug 'altercation/vim-colors-solarized'
Plug 'tomtom/tcomment_vim'
Plug 'kien/ctrlp.vim'
Plug 'suan/vim-instant-markdown'
Plug 'christoomey/vim-tmux-navigator'
Plug 'scrooloose/nerdtree'
Plug 'bling/vim-airline'

call plug#end()
