# Veritastimmy shell aliases
# Customize this file with your preferred shortcuts.

# Safer defaults
alias cp='cp -i'
alias mv='mv -i'
alias rm='rm -i'

# Navigation
alias ..='cd ..'
alias ...='cd ../../../'
alias ....='cd ../../../../'
alias .....='cd ../../../../'

# Listing
alias ls='ls --color=auto'
alias l.='ls -d .* --color=auto'
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Search with color
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias grep='grep --color=auto'

# Git helpers
alias gs='git status -sb'
alias ga='git add'
alias gc='git commit'
alias gp='git push'
alias gpl='git pull --rebase'
alias gd='git diff'
alias gco='git checkout'

# Conda helpers
alias cact='conda activate'
alias cdeact='conda deactivate'
alias cenv='conda env list'
alias cclean='conda clean -ay'
alias can='conda activate new-env'
alias cand='conda activate new-env && cd ~/Documents'

# Convenience
alias cx='chmod +x '
alias prl='perl -wMstrict -MData::Dump'
alias pt='perltidy -i=2 -b -utf8 '
alias scm='sudo cpanm '
alias sc='sudo cpan'
alias deps='scm --installdeps .'
alias xclip='xclip -selection c'

# System
alias update='sudo apt-get update && sudo apt-get upgrade'
alias bounce='sudo service network-manager restart '
alias halt='sudo /sbin/halt'
alias reboot='sudo /sbin/reboot'
alias shutdown='sudo /sbin/shutdown'
alias poweroff='sudo /sbin/poweroff'
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Process info
alias meminfo='free -m -l -t'
alias pscpu='ps auxf | sort -nr -k 3 | more'
alias pscpu10='ps auxf | sort -nr -k 3 | head -10'
alias psmem='ps auxf | sort -nr -k 4 | more'
alias psmem10='ps auxf | sort -nr -k 4 | head -10 | more'

# Media
alias music='mplayer --shuffle *'
alias nplaymp3='for i in /nas/multimedia/mp3/*.mp3; do mplayer "$i"; done'
alias nplayogg='for i in /nas/multimedia/ogg/*.ogg; do mplayer "$i"; done'
alias nplaywave='for i in /nas/multimedia/wave/*.wav; do mplayer "$i"; done'
alias playavi='mplayer *.avi'
alias playmp3='for i in *.mp3; do mplayer "$i"; done'
alias playmp4='for i in *.mp4; do mplayer "$i"; done'
alias playogg='for i in *.ogg; do mplayer "$i"; done'
alias playwave='for i in *.wav; do mplayer "$i"; done'
alias vlc='vlc *.avi'
