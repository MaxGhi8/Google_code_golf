for f in $(ls tasks/*); do
	 perl -0pi -e "s/\R*\z//g" $f
   done
