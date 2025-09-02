for f in $(ls *.py); do
	 perl -0pi -e "s/\R*\z//g" $f
   done
