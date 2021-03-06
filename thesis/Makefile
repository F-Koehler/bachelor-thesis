TEX=./buildtex.sh
PY=python3

HEADERS=$(wildcard header/*.tex)
SECTIONS=$(wildcard sections/*.tex)
SLIDES=$(wildcard slides/*.tex)
PSEUDOCODE=$(wildcard pseudocode/*.tex)
MATPLOTLIB=matplotlibrc header/matplotlib.tex
PLOTS=plot/runtime-theo/runtime.pdf plot/runtime-theo/comparison.pdf plot/runtime-sieve/plot.pdf plot/kbguess/time.pdf plot/runtime/time.pdf plot/runtime2/time.pdf plot/factorization/time.pdf plot/parallelization/plot.pdf
FIGS=$(wildcard fig/*.tex)
BIB=literature.bib

all: build/thesis.pdf build/thesis-print.pdf build/talk.pdf

# analyse data
data/runtime-theo/data.txt: data/runtime-theo/runtime.py
	$(PY) $<
data/runtime-sieve/data.txt: data/runtime-sieve/runtime.py
	$(PY) $<
data/kbguess/data/0.txt: data/kbguess/concatenate.py data/kbguess/data1/0.txt
	$(PY) $<
data/kbguess2/data/0.txt: data/kbguess2/concatenate.py data/kbguess2/data1/0.txt
	$(PY) $<
data/runtime/results.txt: data/runtime/analyse.py data/runtime/data/0.txt
	$(PY) $<
data/runtime2/results.txt: data/runtime2/analyse.py data/runtime2/data/0.txt
	$(PY) $<
data/factorization/results.txt: data/factorization/analyse.py data/factorization/data/0.txt
	$(PY) $ $<

# create plots
plot/runtime-theo/runtime.pdf: plot/runtime-theo/runtime.py data/runtime-theo/data.txt $(MATPLOTLIB)
	$(PY) $<
plot/runtime-theo/comparison.pdf: plot/runtime-theo/comparison.py data/runtime-theo/data.txt $(MATPLOTLIB)
	$(PY) $<
plot/runtime-sieve/plot.pdf: plot/runtime-sieve/plot.py data/runtime-sieve/data.txt $(MATPLOTLIB)
	$(PY) $<
plot/kbguess/time.pdf: plot/kbguess/plot.py data/kbguess/data/0.txt data/kbguess2/data/0.txt
	$(PY) $<
plot/runtime/time.pdf: plot/runtime/plot.py data/runtime/results.txt $(MATPLOTLIB)
	$(PY) $<
plot/runtime2/time.pdf: plot/runtime2/plot.py data/runtime2/results.txt $(MATPLOTLIB)
	$(PY) $<
plot/factorization/time.pdf: plot/factorization/plot.py data/factorization/results.txt $(MATPLOTLIB)
	$(PY) $<
plot/parallelization/plot.pdf: plot/parallelization/plot.py data/parallelization/1.txt $(MATPLOTLIB)
	$(PY) $<
plot/dummy/dummy.pdf: plot/dummy/plot.py $(MATPLOTLIB)
	$(PY) $<

# build thesis
build/thesis.pdf: thesis.tex $(HEADERS) $(SECTIONS) $(PSEUDOCODE) $(BIB) $(PLOTS)
	$(TEX) $< thesis
build/thesis-print.pdf: thesis.tex $(HEADERS) $(SECTIONS) $(PSEUDOCODE) $(BIB) $(PLOTS)
	$(TEX) $< thesis-print

# build talk
build/talk.pdf: talk.tex $(HEADERS) $(SLIDES) $(PSEUDOCODE) $(BIB) $(PLOTS) $(FIGS)
	$(TEX) $< talk

.PHONY: clean
clean:
	rm -rf build $(PLOTS)
