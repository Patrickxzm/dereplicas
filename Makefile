title : title.txt
	iconv -c -f 'gb18030' -t 'utf-8' $< > $@ || echo 'Some illegal characters'
	dos2unix $@
replicas : title
	sed -n '2,4000p' $< | python dereplicas.py > replicas 2>/dev/null
replicas.txt : replicas
	iconv -c -f 'utf-8' -t 'gb18030' $< > $@ || echo 'Some illegal characters'
	unix2dos $@
