#!/bin/bash

rm -R -f output/*
rm -R -f fifo/*
rm -R -f work/*


mkfifo fifo/il_P1

mkfifo fifo/il_S1_summary_P1
mkfifo fifo/il_S1_summarypltcalc_P1
mkfifo fifo/il_S1_pltcalc_P1


# --- Do insured loss kats ---

kat fifo/il_S1_pltcalc_P1 > output/il_S1_pltcalc.csv & pid1=$!

# --- Do ground up loss kats ---


# --- Do insured loss computes ---

pltcalc < fifo/il_S1_summarypltcalc_P1 > fifo/il_S1_pltcalc_P1 &

tee < fifo/il_S1_summary_P1 fifo/il_S1_summarypltcalc_P1  > /dev/null & pid2=$!
summarycalc -f -1 fifo/il_S1_summary_P1  < fifo/il_P1 &

# --- Do ground up loss  computes ---


eve 1 1 | getmodel | gulcalc -S100 -L100 -r -i - | fmcalc > fifo/il_P1  &

wait $pid1 $pid2 



rm fifo/il_P1

rm fifo/il_S1_summary_P1
rm fifo/il_S1_summarypltcalc_P1
rm fifo/il_S1_pltcalc_P1
