for f in $(ls tasks/*); do
	 perl -0pi -e "s/\R*\z//g" $f
   done

for f in $(ls for_compression/*); do
	 perl -0pi -e "s/\R*\z//g" $f
   done

for f in $(ls finals/*); do
	 perl -0pi -e "s/\R*\z//g" $f
   done

for f in $(ls compressed/*); do
	 perl -0pi -e "s/\R*\z//g" $f
   done