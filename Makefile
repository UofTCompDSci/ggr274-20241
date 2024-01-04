TERM=20241

# By default, build local versions of book
all: book

book:
	jupyter-book build ${TERM}

publish-source:
	python software/publish.py ${TERM}

clean-publish-source:
	rm -rf _publish

book-publish:
	jupyter-book build .
