grep -oHE ' [a-z][a-z\_A-Z0-9]+\(' -R . | awk -F': ' '{print $2}' | sed 's/(//g' | sort --uniq | grep -v -E 'str.+|pthread|free|.*alloc|mem.+|.*[Pp]rint|usleep'
