#!/usr/bin/env Rscript
# SPDX-License-Identifier: MIT. Copyright (c) Quarterdeck.
#
# Confirmatory factor analysis of pilot data for an OL profile.
#
#     Rscript profiles/pilot/factor_analysis.R ITEM_BANK.csv PILOT.csv
#
# PILOT.csv has the form that analysis.py reads: the column "respondent" and one
# column for each item id, with a response from 1 to 5 or empty.
#
# The model has one factor for each scale, and the factors can correlate. The
# responses are treated as ordered categories (estimator WLSMV). The output is
# the fit of the model, the standardised loading of each item, the correlations
# between the factors, and coefficient omega for each scale.
#
# Omega here is computed from the standardised loadings: (sum of loadings)^2 /
# ((sum of loadings)^2 + sum of residual variances). With ordered responses it
# describes the underlying continuous responses, so it is usually higher than
# the alpha of the 1 to 5 scores that analysis.py reports.
#
# Needs R and the package lavaan: install.packages("lavaan")

suppressPackageStartupMessages(library(lavaan))

args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 2) {
  stop("Usage: Rscript factor_analysis.R ITEM_BANK.csv PILOT.csv")
}

bank <- read.csv(args[1], stringsAsFactors = FALSE)
data <- read.csv(args[2], stringsAsFactors = FALSE)

missing_columns <- setdiff(bank$id, names(data))
if (length(missing_columns) > 0) {
  stop("The pilot file has no column for: ", paste(missing_columns, collapse = ", "))
}

scales <- unique(bank$scale)
model <- paste(
  sapply(scales, function(s) paste0(s, " =~ ", paste(bank$id[bank$scale == s], collapse = " + "))),
  collapse = "\n"
)

fit <- cfa(model, data = data[, bank$id], ordered = bank$id, estimator = "WLSMV", std.lv = TRUE)

cat("Respondents with complete answers:", lavInspect(fit, "nobs"), "\n\n")

cat("Fit (scaled values). Guide values: CFI and TLI 0.90 or more, RMSEA 0.08 or less, SRMR 0.08 or less.\n")
measures <- fitMeasures(fit, c("chisq.scaled", "df.scaled", "cfi.scaled", "tli.scaled", "rmsea.scaled", "srmr"))
print(round(measures, 3))

solution <- standardizedSolution(fit)
loadings <- solution[solution$op == "=~", c("lhs", "rhs", "est.std")]
names(loadings) <- c("scale", "item", "loading")
loadings$keyed <- bank$keyed[match(loadings$item, bank$id)]

# Point each factor in the direction of its scale, so that a + item has a positive loading.
direction <- sapply(scales, function(s) {
  rows <- loadings$scale == s
  sign(sum(loadings$loading[rows] * ifelse(loadings$keyed[rows] == "+", 1, -1)))
})
loadings$loading <- round(loadings$loading * direction[loadings$scale], 3)

cat("\nStandardised loadings. An item keyed - has a negative loading. Look at an item below 0.40 in size.\n")
print(loadings, row.names = FALSE)

cat("\nCoefficient omega for each scale.\n")
for (s in scales) {
  rows <- loadings$scale == s
  # In the direction of the key, so that an item with the wrong sign lowers omega.
  l <- loadings$loading[rows] * ifelse(loadings$keyed[rows] == "+", 1, -1)
  omega <- sum(l)^2 / (sum(l)^2 + sum(1 - l^2))
  cat(sprintf("  %-12s %.3f\n", s, omega))
}

cat("\nCorrelations between the factors. A value above 0.85 in size means that two scales are hard to separate.\n")
factor_correlations <- lavInspect(fit, "cor.lv")[scales, scales] * outer(direction, direction)
print(round(factor_correlations, 3))
