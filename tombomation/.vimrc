set tags+=../.git/tags
let g:vim_tags_project_tags_command = "{CTAGS} -R {OPTIONS} {DIRECTORY} ~/.pyenv/versions/tombomation/lib 2>/dev/null"
au FileType python compiler pyunit
au FileType python setlocal makeprg=python\ manage.py\ test
